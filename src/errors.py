import functools

import httpx
from mcp.server.mcpserver.exceptions import ToolError

from . import config


def http_errors_as_tool_errors(fn):
    """
    MCP SDK v2 shows the model only "Error executing tool <name>" for unexpected
    exceptions. Re-raise httpx failures as ToolError so the model still sees what
    went wrong: a web page's error status, a connection error, or an invalid URL.
    """

    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        try:
            return await fn(*args, **kwargs)
        # InvalidURL is not an HTTPError subclass.
        except (httpx.HTTPError, httpx.InvalidURL) as e:
            raise ToolError(f"{type(e).__name__}: {e}") from e

    return wrapper


def raise_for_status(response: httpx.Response) -> None:
    """
    Raise a ToolError for an API error status. Unlike httpx's own
    raise_for_status(), the message keeps the API's error body, which says more
    than the status line (e.g. Naver's "SE05", TMAP's "INVALID_API_KEY").
    """
    if response.is_error:
        # Mask before cutting, so a key split at the cut can't leak its first half.
        body = mask_api_keys(response.text.strip())[:500]
        raise ToolError(f"{response.status_code} {response.reason_phrase} for {response.url}: {body}")


def mask_api_keys(text: str) -> str:
    """Replace configured API keys with ***. Kakao, for one, echoes a malformed key in its error body."""
    for key in (config.NAVER_CLIENT_ID, config.NAVER_CLIENT_SECRET, config.KAKAO_REST_API_KEY, config.SK_APP_KEY):
        if key:
            text = text.replace(key, "***")
    return text
