import httpx
import pytest
from mcp.server.mcpserver.exceptions import ToolError

from src.errors import raise_for_status


def response(status, body):
    return httpx.Response(status, text=body, request=httpx.Request("GET", "https://api.example.com/search?query=x"))


def test_error_status_shows_the_api_error_body():
    with pytest.raises(ToolError) as e:
        raise_for_status(response(403, '{"errorType": "ApiError", "message": "SuspendedAppException"}'))
    assert "403 Forbidden" in str(e.value)
    assert "https://api.example.com/search?query=x" in str(e.value)
    assert "SuspendedAppException" in str(e.value)


def test_long_error_body_is_cut():
    with pytest.raises(ToolError) as e:
        raise_for_status(response(502, "<html>" + "x" * 5000 + "</html>"))
    assert len(str(e.value)) < 1000


def test_success_status_passes():
    raise_for_status(response(200, "{}"))


SECRET = "SECRETKEY1234567890"


@pytest.fixture
def kakao_key(monkeypatch):
    monkeypatch.setattr("src.config.KAKAO_REST_API_KEY", SECRET)


def test_api_key_echoed_in_error_body_is_masked(kakao_key):
    # Kakao echoes a malformed key back in its 401 body.
    body = f'{{"errorType": "AccessDeniedError", "message": "wrong appKey({SECRET}) format"}}'
    with pytest.raises(ToolError) as e:
        raise_for_status(response(401, body))
    assert SECRET not in str(e.value)
    assert "wrong appKey(***) format" in str(e.value)


def test_api_key_cut_by_truncation_is_masked(kakao_key):
    with pytest.raises(ToolError) as e:
        raise_for_status(response(401, "x" * 495 + SECRET))
    assert SECRET[:5] not in str(e.value)
