from app.config.settings import settings
from app.scrapers.dou.dou_client import DouClient
from app.parsers.dou_parser import DouParser


class DouScraper:
    def __init__(self) -> None:
        self.client = DouClient()
        self.parser = DouParser()
    async def scrape(self, query: str, limit: int | None = None):
        html = await self.client.fetch(
            url=f"{settings.DOU_BASE_URL}/vacancies",
            params={"category": query}
        )

        vacancies = self.parser.parse_vacancy(html)

        if limit:
            vacancies = vacancies[:limit]

        for vacancy in vacancies:
            detail_html = await self.client.fetch(vacancy.source_url)

            self.parser.parse_single_vacancy(detail_html, vacancy)


        return vacancies
