import os
import httpx
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("KiMCP", dependencies=["httpx"])

NAVER_CLIENT_ID = os.environ.get("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.environ.get("NAVER_CLIENT_SECRET")
api_headers = {
    "X-Naver-Client-Id": NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
}

API_ENDPOINT = "https://openapi.naver.com/v1"


@mcp.tool()
# https://developers.naver.com/docs/serviceapi/search/blog/blog.md
async def search_blog(
    query: str,
    display: int = 10,
    start: int = 1,
    sort: str = "sim",
):
    """
    Search for blog posts on Naver

    Args:
        query (str): Search query string.
        display (int, optional): Number of results to return. Range: 1-100. Defaults to 10.
        start (int, optional): Starting position for search results. Range: 1-1000. Defaults to 1.
        sort (str, optional): Sort order. Options: "sim" (relevance), "date" (recent). Defaults to "sim".
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/search/blog.json",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=api_headers,
        )

        response.raise_for_status()
        return response.text
