import httpx
from bs4 import BeautifulSoup


async def get_webpage_content(link: str) -> str:
    """
    Fetch the full content of a webpage.
    This function retrieves the content of a webpage and removes HTML tags.

    Args:
        link (str): The URL of the webpage to fetch.

    Returns:
        str: The full content of the webpage with HTML tags removed.
    """
    async with httpx.AsyncClient(follow_redirects=True) as client:
        # Convert Naver blog links to mobile version for better parsing
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
