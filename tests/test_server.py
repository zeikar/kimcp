"""
Run the server the way Claude Desktop does (`mcp run main.py` over stdio) and
talk raw JSON-RPC to it, so these tests don't depend on the MCP SDK's client API.
"""

import json
import os
import queue
import socket
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
MCP_CLI = Path(sys.executable).parent / ("mcp.exe" if os.name == "nt" else "mcp")
KEY_VARS = ["NAVER_CLIENT_ID", "NAVER_CLIENT_SECRET", "KAKAO_REST_API_KEY", "SK_APP_KEY"]
DUMMY_KEYS = {var: "dummy" for var in KEY_VARS}

WEB_TOOLS = {
    "get_webpage_content": ["link"],
}
NAVER_TOOLS = {
    "search_naver_blog": ["query", "display", "start", "sort"],
    "search_news": ["query", "display", "start", "sort"],
    "search_naver_cafe_article": ["query", "display", "start", "sort"],
    "search_kin": ["query", "display", "start", "sort"],
    "search_naver_local": ["query", "display", "start", "sort"],
    "search_naver_image": ["query", "display", "start", "sort", "filter"],
    "search_shopping": ["query", "display", "start", "sort", "filter", "exclude"],
}
KAKAO_TOOLS = {
    "search_daum_blog": ["query", "sort", "page", "size"],
    "search_daum_cafe": ["query", "sort", "page", "size"],
    "search_kakao_local": ["query", "page", "size"],
    "search_car_directions": [
        "origin_x", "origin_y", "destination_x", "destination_y", "origin_name",
        "destination_name", "waypoints", "priority", "alternatives", "summary",
    ],
}
SK_TOOLS = {
    "search_transit_route": ["startX", "startY", "endX", "endY", "count"],
    "search_transit_route_detail": ["startX", "startY", "endX", "endY", "count"],
}


class StdioServer:
    def __init__(self, keys):
        env = {k: v for k, v in os.environ.items() if k not in KEY_VARS}
        env.update(keys)
        # Unbuffered, a stray print() reaches stdout before the replies and breaks the protocol here.
        env["PYTHONUNBUFFERED"] = "1"
        self.stderr = tempfile.TemporaryFile(mode="w+", encoding="utf-8")
        self.proc = subprocess.Popen(
            [str(MCP_CLI), "run", "main.py"], cwd=REPO, env=env, text=True, encoding="utf-8",
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=self.stderr,
        )
        # A reader thread lets request() time out instead of hanging on a stuck server.
        self.lines = queue.Queue()
        self.reader = threading.Thread(target=self._read, daemon=True)
        self.reader.start()
        self.next_id = 0

    def initialize(self):
        reply = self.request("initialize", {
            "protocolVersion": "2025-06-18",
            "capabilities": {},
            "clientInfo": {"name": "kimcp-tests", "version": "0"},
        })
        assert reply["result"]["serverInfo"]["name"] == "KiMCP"
        self._send({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def _read(self):
        for line in self.proc.stdout:
            self.lines.put(line)
        self.lines.put(None)

    def _fail(self, reason):
        self.stderr.seek(0)
        pytest.fail(f"{reason}; server stderr:\n" + self.stderr.read()[-2000:])

    def _send(self, msg):
        try:
            self.proc.stdin.write(json.dumps(msg) + "\n")
            self.proc.stdin.flush()
        except BrokenPipeError:
            self._fail("server exited")

    def request(self, method, params=None):
        self.next_id += 1
        msg = {"jsonrpc": "2.0", "id": self.next_id, "method": method}
        if params is not None:
            msg["params"] = params
        self._send(msg)
        while True:
            try:
                line = self.lines.get(timeout=30)
            except queue.Empty:
                self._fail(f"no reply to {method} in 30s")
            if line is None:
                self._fail("server exited")
            try:
                reply = json.loads(line)
            except json.JSONDecodeError:
                self._fail(f"non-JSON line on stdout: {line!r}")
            if reply.get("id") == self.next_id:
                return reply

    def tools(self):
        tools = self.request("tools/list")["result"]["tools"]
        return {t["name"]: list(t["inputSchema"]["properties"]) for t in tools}

    def call(self, name, arguments):
        return self.request("tools/call", {"name": name, "arguments": arguments})

    def close(self):
        try:
            self.proc.stdin.close()
        except BrokenPipeError:
            pass  # already exited; the wait below reaps it
        try:
            self.proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.proc.kill()
            self.proc.wait()
        self.reader.join(timeout=5)
        self.proc.stdout.close()
        self.stderr.close()


@pytest.fixture
def server():
    servers = []

    def start(keys):
        s = StdioServer(keys)
        servers.append(s)  # before the handshake, so a failed one is still closed
        s.initialize()
        return s

    yield start
    for s in servers:
        s.close()


@pytest.fixture
def local_page():
    body = (
        "<html><head><style>p { color: red; }</style><script>var x = 1;</script></head>"
        "<body><p>안녕 KiMCP</p></body></html>"
    ).encode()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/missing":
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{httpd.server_port}/"
    httpd.shutdown()
    httpd.server_close()


@pytest.mark.parametrize("keys, expected", [
    ({}, WEB_TOOLS),
    ({"NAVER_CLIENT_ID": "dummy", "NAVER_CLIENT_SECRET": "dummy"}, {**WEB_TOOLS, **NAVER_TOOLS}),
    ({"KAKAO_REST_API_KEY": "dummy"}, {**WEB_TOOLS, **KAKAO_TOOLS}),
    ({"SK_APP_KEY": "dummy"}, {**WEB_TOOLS, **SK_TOOLS}),
    (DUMMY_KEYS, {**WEB_TOOLS, **NAVER_TOOLS, **KAKAO_TOOLS, **SK_TOOLS}),
], ids=["no-keys", "naver", "kakao", "sk", "all"])
def test_tools_registered_per_api_key(server, keys, expected):
    assert server(keys).tools() == expected


def test_call_with_missing_argument_is_an_error(server):
    result = server(DUMMY_KEYS).call("search_naver_blog", {})["result"]
    assert result["isError"]
    text = result["content"][0]["text"]
    assert "query" in text and "Field required" in text


def test_get_webpage_content_strips_html(server, local_page):
    s = server({})
    result = s.call("get_webpage_content", {"link": local_page})["result"]
    assert not result.get("isError")
    assert result["content"][0]["text"] == "안녕 KiMCP"
    # The page text goes out once, not again as structuredContent.
    assert "structuredContent" not in result
    [tool] = s.request("tools/list")["result"]["tools"]
    assert "outputSchema" not in tool


# MCP SDK v2 hides the text of unexpected exceptions, so these failures must be ToolErrors.
def test_http_error_reaches_the_model(server, local_page):
    result = server({}).call("get_webpage_content", {"link": local_page + "missing"})["result"]
    assert result["isError"]
    assert "404 Not Found" in result["content"][0]["text"]


def test_connection_error_reaches_the_model(server):
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        closed_port = s.getsockname()[1]
    result = server({}).call("get_webpage_content", {"link": f"http://127.0.0.1:{closed_port}/"})["result"]
    assert result["isError"]
    assert "ConnectError" in result["content"][0]["text"]


def test_invalid_url_reaches_the_model(server):
    result = server({}).call("get_webpage_content", {"link": "http://[::1"})["result"]
    assert result["isError"]
    assert "InvalidURL" in result["content"][0]["text"]


def test_waypoint_limit_reaches_the_model(server):
    result = server(DUMMY_KEYS).call("search_car_directions", {
        "origin_x": 127.0, "origin_y": 37.5, "destination_x": 127.1, "destination_y": 37.6,
        "waypoints": [{"x": 127.05, "y": 37.55}] * 6,
    })["result"]
    assert result["isError"]
    assert "Maximum 5 waypoints" in result["content"][0]["text"]


@pytest.mark.skipif(
    not (os.environ.get("NAVER_CLIENT_ID") and os.environ.get("NAVER_CLIENT_SECRET")),
    reason="live test: run with NAVER_CLIENT_ID and NAVER_CLIENT_SECRET set (uv run --env-file .env pytest)",
)
def test_naver_blog_search_live(server):
    keys = {k: os.environ[k] for k in ["NAVER_CLIENT_ID", "NAVER_CLIENT_SECRET"]}
    result = server(keys).call("search_naver_blog", {"query": "칫솔", "display": 1})["result"]
    assert not result.get("isError")
    assert '"items"' in result["content"][0]["text"]
