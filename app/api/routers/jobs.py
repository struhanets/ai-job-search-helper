import logging

from fastapi import APIRouter
from fastapi.params import Query

from app.models.domain.vacancy import Vacancy
from app.scrapers.dou.dou_scraper import DouScraper
from app.services.vacancy_parse_service import VacancyParseService


logger = logging.getLogger(__name__)
router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/search", response_model=list[Vacancy])
async def search_jobs(
    query: str = Query(..., description="Search query request"),
):
    scraper = DouScraper()
    ai_parse_service = VacancyParseService()

    # Get vacancies from the scraper
    vacancies = await scraper.scrape(query, limit=2)

    # Enrich vacancies with AI data
    enriched_vacancies = []

    for vacancy in vacancies:
        try:
            enriched = await ai_parse_service.enrich(vacancy)
            enriched_vacancies.append(enriched)
        except Exception as e:
            logger.exception(
                "Failed to enrich vacancy: %s",
                vacancy.source_url
            )
            enriched_vacancies.append(vacancy)

    return enriched_vacancies
