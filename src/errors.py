import functools

import httpx
from mcp.server.mcpserver.exceptions import ToolError


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
        raise ToolError(
            f"{response.status_code} {response.reason_phrase} for {response.url}: "
            f"{response.text.strip()[:500]}"
        )
