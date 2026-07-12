import httpx
import logging
from app.config.settings import settings

logger = logging.getLogger(__name__)


class DouClient:
    def __init__(self):
        # Default HTTP headers sent with every request
        # User-Agent helps mimic a real browser and reduces the chance of being blocked
        self.headers = {
            "User-Agent": settings.USER_AGENT,
        }

    async def fetch(self, url: str, params: dict | None = None) -> str:
        """
        Fetch the HTML page with vacancies from DOU.
        Args:
            url (str): The target URL to fetch.
            params (dict | None): Optional query parameters for the GET request.
        Returns:
            Raw HTML content of the search results page.
        """


        # Create an asynchronous HTTP client
        async with httpx.AsyncClient(headers=self.headers, follow_redirects=True) as client:
            try:
                # Send GET request to DOU
                response = await client.get(url, params=params)
                response.raise_for_status()

                # Return raw HTML for further parsing
                return response.text
            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error occurred: {e.response.status_code}")
                raise
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                raise
