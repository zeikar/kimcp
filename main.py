import sys
from mcp.server.mcpserver import MCPServer
from src.naver import search_naver_blog, search_naver_cafe_article, search_naver_image, search_kin, search_naver_local, search_news, search_shopping
from src.kakao import search_daum_blog, search_daum_cafe, search_kakao_local, search_car_directions
from src.sk import search_transit_route, search_transit_route_detail
from src.web import get_webpage_content
from src.config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, KAKAO_REST_API_KEY, SK_APP_KEY
from src.errors import http_errors_as_tool_errors

# Create an MCP server
mcp = MCPServer("KiMCP", dependencies=["httpx", "beautifulsoup4"])


def add_tool(fn, **kwargs):
    mcp.add_tool(http_errors_as_tool_errors(fn), **kwargs)


# Register web utility tools
# Its page text is already in the result's content; structured output would send it twice.
add_tool(get_webpage_content, structured_output=False)

# Register all Naver API tools only if credentials are set
if NAVER_CLIENT_ID and NAVER_CLIENT_SECRET:
    add_tool(search_naver_blog)
    add_tool(search_news)
    add_tool(search_naver_cafe_article)
    add_tool(search_kin)
    add_tool(search_naver_local)
    add_tool(search_naver_image)
    add_tool(search_shopping)
else:
    print("Warning: Naver API credentials are not set. Naver API tools will not be available.", file=sys.stderr)

if KAKAO_REST_API_KEY:
    add_tool(search_daum_blog)
    add_tool(search_daum_cafe)
    add_tool(search_kakao_local)
    add_tool(search_car_directions)
else:
    print("Warning: Kakao API credentials are not set. Kakao API tools will not be available.", file=sys.stderr)

if SK_APP_KEY:
    add_tool(search_transit_route)
    add_tool(search_transit_route_detail)
else:
    print("Warning: SK API credentials are not set. SK API tools will not be available.", file=sys.stderr)
