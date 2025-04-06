import httpx
from .config import KAKAO_REST_API_KEY

# API endpoints
API_ENDPOINT = "https://dapi.kakao.com/v2"

API_HEADERS = {
    "Authorization": f"KakaoAK {KAKAO_REST_API_KEY}",
}


# https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide


async def search_daum_blog(
    query: str,
    sort: str = "accuracy",
    page: int = 1,
    size: int = 10,
):
    """
    Search for blog posts on Daum

    Args:
        query (str): Search query string.
        sort (str, optional): Sort order. Options: "accuracy" (relevance), "recency" (recent). Defaults to "accuracy".
        page (int, optional): Page number for search results. Range: 1-50. Defaults to 1.
        size (int, optional): Number of results per page. Range: 1-50. Defaults to 10.
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/search/blog",
            headers=API_HEADERS,
            params={
                "query": query,
                "sort": sort,
                "page": page,
                "size": size,
            },
        )

    return response.json()


async def search_daum_cafe(
    query: str,
    sort: str = "accuracy",
    page: int = 1,
    size: int = 10,
):
    """
    Search for cafe posts on Daum

    Args:
        query (str): Search query string.
        sort (str, optional): Sort order. Options: "accuracy" (relevance), "recency" (recent). Defaults to "accuracy".
        page (int, optional): Page number for search results. Range: 1-50. Defaults to 1.
        size (int, optional): Number of results per page. Range: 1-50. Defaults to 10.
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/search/cafe",
            headers=API_HEADERS,
            params={
                "query": query,
                "sort": sort,
                "page": page,
                "size": size,
            },
        )

    return response.json()

# https://developers.kakao.com/docs/latest/ko/local/dev-guide


async def search_kakao_local(
    query: str,
    page: int = 1,
    size: int = 15,
):
    """
    Search for local places on Daum

    Args:
        query (str): Search query string.
        page (int, optional): Page number for search results. Range: 1-45. Defaults to 1.
        size (int, optional): Number of results per page. Range: 1-15. Defaults to 10.
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/local/search/keyword.json",
            headers=API_HEADERS,
            params={
                "query": query,
                "page": page,
                "size": size,
            },
        )

    return response.json()
