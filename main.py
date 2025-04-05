from mcp.server.fastmcp import FastMCP
from src.naver import get_naver_blog_details_link, search_naver_blog, search_naver_cafe_article, search_naver_image, search_kin, search_naver_local, search_news, search_shopping
from src.kakao import search_daum_blog, search_daum_cafe
from src.config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, KAKAO_REST_API_KEY

# Create an MCP server
mcp = FastMCP("KiMCP", dependencies=["httpx", "beautifulsoup4"])


# Register all Naver API tools only if credentials are set
if NAVER_CLIENT_ID and NAVER_CLIENT_SECRET:
    mcp.add_tool(get_naver_blog_details_link)
    mcp.add_tool(search_naver_blog)
    mcp.add_tool(search_news)
    mcp.add_tool(search_naver_cafe_article)
    mcp.add_tool(search_kin)
    mcp.add_tool(search_naver_local)
    mcp.add_tool(search_naver_image)
    mcp.add_tool(search_shopping)
else:
    print("Warning: Naver API credentials are not set. Naver API tools will not be available.")

if KAKAO_REST_API_KEY:
    mcp.add_tool(search_daum_blog)
    mcp.add_tool(search_daum_cafe)
else:
    print("Warning: Kakao API credentials are not set. Kakao API tools will not be available.")
