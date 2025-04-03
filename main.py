import os
import httpx
from mcp.server.fastmcp import FastMCP
from bs4 import BeautifulSoup

# Create an MCP server
mcp = FastMCP("KiMCP", dependencies=["httpx", "beautifulsoup4"])

NAVER_CLIENT_ID = os.environ.get("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.environ.get("NAVER_CLIENT_SECRET")
api_headers = {
    "X-Naver-Client-Id": NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
}

API_ENDPOINT = "https://openapi.naver.com/v1"


@mcp.tool()
async def get_details_link(link: str) -> str:
    """
    Fetch the full content of a Naver blog post.
    This function retrieves the content of a webpage and removes HTML tags.

    Args:
        link (str): The URL of the webpage to fetch.

    Returns:
        str: The full content of the webpage with HTML tags removed.
    """
    async with httpx.AsyncClient() as client:
        # To mobile page
        if "https://blog.naver.com" in link:
            link = link.replace("blog.naver.com", "m.blog.naver.com")

        response = await client.get(link)
        response.raise_for_status()

        # Parse the response to get the text content only
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Get text content
        text = soup.get_text()

        # Clean up text: remove multiple newlines and whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip()
                  for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        return text


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


@mcp.tool()
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

    Returns:
        str: JSON string containing Q&A article search results.

        Response fields:
            - lastBuildDate (str): Date and time when the response was generated
            - total (int): Total number of search results
            - start (int): Starting position of this result set
            - display (int): Number of items in this response
            - items (list): List of Q&A articles containing:
                - title (str): Q&A article title (may contain HTML tags for highlighting)
                - link (str): URL of the Q&A article
                - description (str): Brief excerpt from the Q&A article (may contain HTML tags)
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
            headers=api_headers,
        )

        response.raise_for_status()
        return response.text


@mcp.tool()
# https://developers.naver.com/docs/serviceapi/search/local/local.md
async def search_local(
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

    Returns:
        str: JSON string containing local business search results.

        Response fields:
            - lastBuildDate (str): Date and time when the response was generated
            - total (int): Total number of search results
            - start (int): Starting position of this result set
            - display (int): Number of items in this response
            - items (list): List of local businesses containing:
                - title (str): Business name (may contain HTML tags for highlighting)
                - link (str): URL of the business page
                - category (str): Business category
                - description (str): Brief description of the business
                - telephone (str): Business phone number
                - address (str): Business address
                - roadAddress (str): Road address of the business
                - mapX (float): X coordinate on the map
                - mapY (float): Y coordinate on the map
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
            headers=api_headers,
        )

        response.raise_for_status()
        return response.text


@mcp.tool()
# https://developers.naver.com/docs/serviceapi/search/image/image.md
async def search_image(
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

    Returns:
        str: JSON string containing image search results.

        Response fields:
            - lastBuildDate (str): Date and time when the response was generated
            - total (int): Total number of search results
            - start (int): Starting position of this result set
            - display (int): Number of items in this response
            - items (list): List of images containing:
                - title (str): Image title (may contain HTML tags for highlighting)
                - link (str): URL of the image
                - thumbnail (str): Thumbnail URL of the image
                - sizeheight (int): Height of the image
                - sizewidth (int): Width of the image
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
            headers=api_headers,
        )

        response.raise_for_status()
        return response.text


@mcp.tool()
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

    Returns:
        str: JSON string containing shopping item search results.

        Response fields:
            - lastBuildDate (str): Date and time when the response was generated
            - total (int): Total number of search results
            - start (int): Starting position of this result set
            - display (int): Number of items in this response
            - items (list): List of shopping items containing:
                - title (str): Item title (may contain HTML tags for highlighting)
                - link (str): URL of the item
                - image (str): Image URL of the item
                - lprice (int): Lowest price of the item
                - hprice (int): Highest price of the item
                - mallName (str): Name of the shopping mall
                - productId (str): Product ID
                - productType (str): Product type
                - maker (str): Maker name
                - brand (str): Brand name
                - category1 (str): Category level 1 name
                - category2 (str): Category level 2 name
                - category3 (str): Category level 3 name
                - category4 (str): Category level 4 name
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
            headers=api_headers,
        )

        response.raise_for_status()
        return response.text
