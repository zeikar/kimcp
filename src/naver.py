import httpx
from .config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET

# API endpoints
API_ENDPOINT = "https://openapi.naver.com/v1"

API_HEADERS = {
    "X-Naver-Client-Id": NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
}

# https://developers.naver.com/docs/serviceapi/search/blog/blog.md


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
            f"{API_ENDPOINT}/search/blog.json",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )

        response.raise_for_status()
        return response.text

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
            headers=API_HEADERS,
        )

        response.raise_for_status()
        return response.text

# https://developers.naver.com/docs/serviceapi/search/cafearticle/cafearticle.md


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
            f"{API_ENDPOINT}/search/cafearticle.json",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )
        response.raise_for_status()
        return response.text

# https://developers.naver.com/docs/serviceapi/search/kin/kin.md


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
            f"{API_ENDPOINT}/search/kin.json",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )

        response.raise_for_status()
        return response.text

# https://developers.naver.com/docs/serviceapi/search/local/local.md


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
            f"{API_ENDPOINT}/search/local.json",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
            },
            headers=API_HEADERS,
        )

        response.raise_for_status()
        return response.text

# https://developers.naver.com/docs/serviceapi/search/image/image.md


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
            f"{API_ENDPOINT}/search/image.json",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
                "filter": filter,
            },
            headers=API_HEADERS,
        )

        response.raise_for_status()
        return response.text

# https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md


async def search_shopping(
    query: str,
    display: int = 10,
    start: int = 1,
    sort: str = "sim",
    filter: str = None,
    exclude: str = None,
):
    """
    Search for shopping items on Naver

    Args:
        query (str): Search query string.
        display (int, optional): Number of results to return. Range: 1-100. Defaults to 10.
        start (int, optional): Starting position for search results. Range: 1-1000. Defaults to 1.
        sort (str, optional): Sort order. Options: "sim" (relevance), "date" (recent), "asc" (price ascending), "dsc" (price descending). Defaults to "sim".
        filter (str, optional): Filter options. Options: None (all items), "naverpay" (Naver Pay items). Defaults to None.
        exclude (str, optional): Exclude options as colon-separated values (e.g., exclude=used:cbshop). Defaults to None. Options:
            - used: Used items
            - rental: Rental items 
            - cbshop: Overseas direct purchases and purchase agency items
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_ENDPOINT}/search/shop.json",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
                "filter": filter,
                "exclude": exclude,
            },
            headers=API_HEADERS,
        )

        response.raise_for_status()
        return response.text
