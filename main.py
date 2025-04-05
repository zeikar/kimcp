from mcp.server.fastmcp import FastMCP
from src.naver import get_naver_blog_details_link, search_blog, search_cafe_article, search_image, search_kin, search_local, search_news, search_shopping
from src.config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET

# Create an MCP server
mcp = FastMCP("KiMCP", dependencies=["httpx", "beautifulsoup4"])


# Register all Naver API tools only if credentials are set
if NAVER_CLIENT_ID and NAVER_CLIENT_SECRET:
    mcp.add_tool(get_naver_blog_details_link)
    mcp.add_tool(search_blog)
    mcp.add_tool(search_news)
    mcp.add_tool(search_cafe_article)
    mcp.add_tool(search_kin)
    mcp.add_tool(search_local)
    mcp.add_tool(search_image)
    mcp.add_tool(search_shopping)
else:
    print("Warning: Naver API credentials are not set. Naver API tools will not be available.")
