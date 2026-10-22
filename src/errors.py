import functools

import httpx
from mcp.server.mcpserver.exceptions import ToolError


def http_errors_as_tool_errors(fn):
    """
    MCP SDK v2 shows the model only "Error executing tool <name>" for unexpected
    exceptions. Re-raise httpx failures as ToolError so the model still sees what
    went wrong: an error status from raise_for_status() (Naver, web pages), a
    connection error, or an invalid URL.
    """

    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        try:
            return await fn(*args, **kwargs)
        # InvalidURL is not an HTTPError subclass.
        except (httpx.HTTPError, httpx.InvalidURL) as e:
            raise ToolError(f"{type(e).__name__}: {e}") from e

    return wrapper
