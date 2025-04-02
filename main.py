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

    Returns:
        str: JSON string containing blog search results.

        Response fields:
            - lastBuildDate (str): Date and time when the response was generated
            - total (int): Total number of search results
            - start (int): Starting position of this result set
            - display (int): Number of items in this response
            - items (list): List of blog posts containing:
                - title (str): Blog post title (may contain HTML tags for highlighting)
                - link (str): URL of the blog post
                - description (str): Brief excerpt from the blog post (may contain HTML tags)
                - bloggername (str): Name of the blogger
                - bloggerlink (str): URL of the blogger's blog
                - postdate (str): Publication date in YYYYMMDD format

        Example:
        {
            "lastBuildDate":"Wed, 02 Apr 2025 22:27:51 +0900",
            "total":47185,
            "start":1,
            "display":10,
            "items":[
                {
                    "title":"<b>판교 회식 추천</b> 분당 고기집 됐소 판교점",
                    "link":"https://blog.naver.com/oyeoyewow/223816242569",
                    "description":"판교역 4번출구 도보20여분 거리 유스페이스2 건물 하나은행 판교지점 아래 1층 가족 모임이나 회식... 됐소 판교점 <b>판교 회식 추천</b>으로 분당 고기집 추천으로 많이 소개되는 이유를 실제 먹어보니 이해가... ",
                    "bloggername":"유쾌한오예씨'의 먹고 사는 이야기 ♬.",
                    "bloggerlink":"blog.naver.com/oyeoyewow",
                    "postdate":"20250331"
                },
                ...
            ]
        }
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


@mcp.tool()
# https://developers.naver.com/docs/serviceapi/search/news/news.md
async def search_news(
    query: str,
    display: int = 10,
    start: int = 1,
    sort: str = "sim",
):
    """
    Search for news articles on Naver

    Args:
        query (str): Search query string.
        display (int, optional): Number of results to return. Range: 1-100. Defaults to 10.
        start (int, optional): Starting position for search results. Range: 1-1000. Defaults to 1.
        sort (str, optional): Sort order. Options: "sim" (relevance), "date" (recent). Defaults to "sim".

    Returns:
        str: JSON string containing news search results.

        Response fields:
            - lastBuildDate (str): Date and time when the response was generated
            - total (int): Total number of search results
            - start (int): Starting position of this result set
            - display (int): Number of items in this response
            - items (list): List of news articles containing:
                - title (str): News title (may contain HTML tags for highlighting)
                - originallink (str): Original news article URL
                - link (str): News article URL provided by Naver
                - description (str): Brief excerpt from the news article (may contain HTML tags)
                - pubDate (str): Publication date and time

        Example:
        {
            "lastBuildDate":"Wed, 02 Apr 2025 22:21:56 +0900",
            "total":391881,
            "start":1,
            "display":10,
            "items":[
                {
                    "title":"국회, 윤 <b>탄핵</b> 질서 유지 조치…외부인 출입 제한 등",
                    "originallink":"https://www.newsis.com/view/NISX20250402_0003123714",
                    "link":"https://n.news.naver.com/mnews/article/003/0013159162?sid=100",
                    "description":"국회가 2일 헌법재판소의 <b>윤석열</b> 대통령 <b>탄핵</b> 심판과 관련해 경내 출입 제한 등 질서 유지를 위한 조치에 나선다. 김민기 국회 사무총장은 이날 '국회 안전과 질서유지에 대한 협조 요청' 공문을 통해 \"헌재 대통령 <b>탄핵</b>... ",
                    "pubDate":"Wed, 02 Apr 2025 14:42:00 +0900"
                },
                ...
            ]
        }
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/search/news.json",
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


@mcp.tool()
# https://developers.naver.com/docs/serviceapi/search/cafearticle/cafearticle.md
async def search_cafe_article(
    query: str,
    display: int = 10,
    start: int = 1,
    sort: str = "sim",
):
    """
    Search for cafe articles on Naver

    Args:
        query (str): Search query string.
        display (int, optional): Number of results to return. Range: 1-100. Defaults to 10.
        start (int, optional): Starting position for search results. Range: 1-1000. Defaults to 1.
        sort (str, optional): Sort order. Options: "sim" (relevance), "date" (recent). Defaults to "sim".

    Returns:
        str: JSON string containing cafe article search results.

        Response fields:
            - lastBuildDate (str): Date and time when the response was generated
            - total (int): Total number of search results
            - start (int): Starting position of this result set
            - display (int): Number of items in this response
            - items (list): List of cafe articles containing:
                - title (str): Cafe article title (may contain HTML tags for highlighting)
                - link (str): URL of the cafe article
                - description (str): Brief excerpt from the cafe article (may contain HTML tags)
                - cafename (str): Name of the cafe
                - cafeurl (str): URL of the cafe

        Example:
        {
            "lastBuildDate":"Wed, 02 Apr 2025 22:33:58 +0900",
            "total":9071,
            "start":1,
            "display":10,
            "items":[
                {
                    "title":"<b>유리카모메</b>, 3월 17일(월)부터 터치결제 승차 도입+QR 패스 발매",
                    "link":"http://cafe.naver.com/20daelee/869288",
                    "description":"린카이선과 더불어 오다이바의 유이한 철도 노선인 <b>유리카모메</b>에서 3월 17일부터 터치결제 승차 서비스를 개시합니다. 또한, <b>유리카모메</b> Enjoy Pass라는 QR코드 승차권 서비스도 개시합니다. 터치결제 가능한... ",
                    "cafename":"체크인데이#일본여행,도쿄여행,후쿠오...",
                    "cafeurl":"https://cafe.naver.com/20daelee"
                },
                ...
            ]
        }
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/search/cafearticle.json",
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
