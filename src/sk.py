import httpx
from .config import SK_APP_KEY

# API endpoints
API_ENDPOINT = "https://apis.openapi.sk.com"

API_HEADERS = {
    "appKey": SK_APP_KEY,
}

# https://transit.tmapmobility.com/docs/routes


async def search_transit_route_detail(
    startX: float,
    startY: float,
    endX: float,
    endY: float,
    count: int = 5,
):
    """
    Search for detailed transit routes between two points.

    This function retrieves comprehensive information about transit routes, including
    detailed route names, transfer details, station information, specific bus/subway lines,
    and estimated travel time. Unlike search_transit_route which provides only basic summaries,
    this function returns the complete journey information with step-by-step waypoints.

    The 'pathType' in the response indicates the transit mode:
    1 - Subway, 2 - Bus, 3 - Bus+Subway, 4 - Express/Intercity Bus, 
    5 - Train, 6 - Air, 7 - Maritime

    Args:
        startX (float): Starting longitude coordinate.
        startY (float): Starting latitude coordinate.
        endX (float): Destination longitude coordinate.
        endY (float): Destination latitude coordinate.
        count (int, optional): Number of route alternatives to return. Range: 1-10. Defaults to 5.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{API_ENDPOINT}/transit/routes",
            headers=API_HEADERS,
            json={
                "startX": startX,
                "startY": startY,
                "endX": endX,
                "endY": endY,
                "count": count,
            },
        )

    result = response.json()

    # Remove specific fields from plan.legs to reduce response size

    if "metaData" in result and "plan" in result["metaData"] and "itineraries" in result["metaData"]["plan"]:
        for itinerary in result["metaData"]["plan"]["itineraries"]:
            if "legs" in itinerary:
                for leg in itinerary["legs"]:
                    if "steps" in leg:
                        del leg["steps"]
                    if "passShape" in leg:
                        del leg["passShape"]
                    if "passStopList" in leg:
                        del leg["passStopList"]

    return result


async def search_transit_route(
    startX: float,
    startY: float,
    endX: float,
    endY: float,
    count: int = 5,
):
    """
    Search for transit routes between two points with summarized information.

    This function retrieves basic information about transit routes, including
    transit type, estimated travel time, number of transfers, walking distance, and fare.
    It provides a lightweight summary compared to search_transit_route_detail, making it
    more suitable for initial route comparisons and overview displays.

    The 'pathType' in the response indicates the transit mode:
    1 - Subway, 2 - Bus, 3 - Bus+Subway, 4 - Express/Intercity Bus, 
    5 - Train, 6 - Air, 7 - Maritime

    Args:
        startX (float): Starting longitude coordinate.
        startY (float): Starting latitude coordinate.
        endX (float): Destination longitude coordinate.
        endY (float): Destination latitude coordinate.
        count (int, optional): Number of route alternatives to return. Range: 1-10. Defaults to 5.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{API_ENDPOINT}/transit/routes/sub",
            headers=API_HEADERS,
            json={
                "startX": startX,
                "startY": startY,
                "endX": endX,
                "endY": endY,
                "count": count,
            },
        )

    return response.json()
