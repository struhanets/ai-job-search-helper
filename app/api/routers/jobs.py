from fastapi import APIRouter
from fastapi.params import Query

from app.models.domain.vacancy import Vacancy

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/search", response_model=list[Vacancy])
async def search_jobs(
        query: str = Query(..., description="Search query request"),
):
    scraper = DouScraper
    return await scraper.search(query)

