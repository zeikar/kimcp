import httpx
from .config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
from .errors import raise_for_status

# API endpoints
API_ENDPOINT = "https://naverapihub.apigw.ntruss.com/search/v1"

API_HEADERS = {
    "X-NCP-APIGW-API-KEY-ID": NAVER_CLIENT_ID,
    "X-NCP-APIGW-API-KEY": NAVER_CLIENT_SECRET,
}

# https://api.ncloud-docs.com/docs/naver-api-hub-search-blog


async def search_naver_blog(
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
            f"{API_ENDPOINT}/blog",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )

        raise_for_status(response)
        return response.text

# https://api.ncloud-docs.com/docs/naver-api-hub-search-news


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
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/news",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )

        raise_for_status(response)
        return response.text

# https://api.ncloud-docs.com/docs/naver-api-hub-search-cafearticle


async def search_naver_cafe_article(
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
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/cafearticle",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )
        raise_for_status(response)
        return response.text

# https://api.ncloud-docs.com/docs/naver-api-hub-search-kin


async def search_kin(
    query: str,
    display: int = 10,
    start: int = 1,
    sort: str = "sim",
):
    """
    Search for Q&A articles on Naver Knowledge iN

    Args:
        query (str): Search query string.
        display (int, optional): Number of results to return. Range: 1-100. Defaults to 10.
        start (int, optional): Starting position for search results. Range: 1-1000. Defaults to 1.
        sort (str, optional): Sort order. Options: "sim" (relevance), "date" (recent), "point" (highly rated). Defaults to "sim".
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/kin",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )

        raise_for_status(response)
        return response.text

# https://api.ncloud-docs.com/docs/naver-api-hub-search-local


async def search_naver_local(
    query: str,
    display: int = 1,
    start: int = 1,
    sort: str = "random",
):
    """
    Search for local businesses on Naver

    Args:
        query (str): Search query string.
        display (int, optional): Number of results to return. Range: 1-5. Defaults to 1.
        start (int, optional): Starting position for search results. Range: 1-1. Defaults to 1.
        sort (str, optional): Sort order. Options: "random" (random), "comment" (comment count). Defaults to "random".
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/local",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )

        raise_for_status(response)
        return response.text

# https://api.ncloud-docs.com/docs/naver-api-hub-search-image


async def search_naver_image(
    query: str,
    display: int = 10,
    start: int = 1,
    sort: str = "sim",
    filter: str = "all",
):
    """
    Search for images on Naver

    Args:
        query (str): Search query string.
        display (int, optional): Number of results to return. Range: 1-100. Defaults to 10.
        start (int, optional): Starting position for search results. Range: 1-1000. Defaults to 1.
        sort (str, optional): Sort order. Options: "sim" (relevance), "date" (recent). Defaults to "sim".
        filter (str, optional): Image filter. Options: "all" (all images), "large" (large images), "medium" (medium images), "small" (small images). Defaults to "all".
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/image",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
                "filter": filter,
            },
            headers=API_HEADERS,
        )

        raise_for_status(response)
        return response.text
