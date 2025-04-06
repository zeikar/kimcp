import httpx
from .config import KAKAO_REST_API_KEY

# API endpoints
API_ENDPOINT = "https://dapi.kakao.com/v2"
MOBILITY_API_ENDPOINT = "https://apis-navi.kakaomobility.com/v1"

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
    size: int = 5,
):
    """
    Search for local places on Daum

    Args:
        query (str): Search query string.
        page (int, optional): Page number for search results. Range: 1-45. Defaults to 1.
        size (int, optional): Number of results per page. Range: 1-15. Defaults to 5.
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

# https://developers.kakaomobility.com/docs/navi-api/directions/


async def search_car_directions(
    origin_x: float,
    origin_y: float,
    destination_x: float,
    destination_y: float,
    origin_name: str = None,
    destination_name: str = None,
    waypoints: list = None,
    priority: str = "RECOMMEND",
    alternatives: bool = False,
    summary: bool = True,
):
    """
    Get directions from origin to destination using car navigation.
    This function retrieves route information including distance, duration, fare, taxi fare, etc.

    Args:
        origin_x (float): Origin X coordinate (longitude)
        origin_y (float): Origin Y coordinate (latitude)
        destination_x (float): Destination X coordinate (longitude)
        destination_y (float): Destination Y coordinate (latitude)
        origin_name (str, optional): Origin name. Defaults to None.
        destination_name (str, optional): Destination name. Defaults to None.
        waypoints (list, optional): List of waypoints. Each waypoint should be a dict with x, y, and name keys. 
                                    Maximum 5 waypoints allowed. Defaults to None.
        priority (str, optional): Route search priority. 
                                  Options: "RECOMMEND" (recommended), "TIME" (fastest), "DISTANCE" (shortest). 
                                  Defaults to "RECOMMEND".
        alternatives (bool, optional): Whether to provide alternative routes. Defaults to False.
        summary (bool, optional): Whether to summarize the route. Defaults to True.
    """
    # Prepare origin and destination parameters
    origin = f"{origin_x},{origin_y}"
    destination = f"{destination_x},{destination_y}"

    if origin_name:
        origin += f",name={origin_name}"
    if destination_name:
        destination += f",name={destination_name}"

    # Prepare waypoints parameter if provided
    waypoints_param = None
    if waypoints and len(waypoints) > 0:
        if len(waypoints) > 5:
            raise ValueError("Maximum 5 waypoints allowed")

        waypoint_strings = []
        for wp in waypoints:
            wp_str = f"{wp['x']},{wp['y']}"
            if 'name' in wp:
                wp_str += f",name={wp['name']}"
            waypoint_strings.append(wp_str)

        waypoints_param = "|".join(waypoint_strings)

    # Prepare request parameters
    params = {
        "origin": origin,
        "destination": destination,
        "priority": priority,
        "alternatives": str(alternatives).lower(),
        "car_hipass": "true",
        "summary": str(summary).lower(),
    }

    # Add waypoints if provided
    if waypoints_param:
        params["waypoints"] = waypoints_param

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{MOBILITY_API_ENDPOINT}/directions",
            headers=API_HEADERS,
            params=params,
        )

    return response.json()
