import logging

from app.ai.client import AIClient
from app.models.domain.vacancy import VacancyAIData, Vacancy
from app.utils.prompt_loader import PromptLoader

logger = logging.getLogger(__name__)


class VacancyParseService:
    def __init__(self):
        self.ai_client = AIClient()
        self._system_prompt = PromptLoader()

    async def enrich(self, vacancy: Vacancy) -> Vacancy:
        prompt = (
            f"Please analyze the vacancy text below and extract the structured data:\n\n"
            f"--- VACANCY TEXT START ---\n"
            f"{vacancy.raw_text}\n"
            f"--- VACANCY TEXT END ---"
        )

        ai_data = await self.ai_client.get_structured_data(
            prompt=prompt,
            response_model=VacancyAIData,
            system_prompt=self._system_prompt.load("parse_vacancy_system_prompt.md")
        )

        for field, value in ai_data.model_dump(exclude_none=True).items():
            setattr(vacancy, field, value)

        return vacancy