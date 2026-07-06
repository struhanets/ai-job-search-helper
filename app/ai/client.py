import logging
from typing import Type, TypeVar
from pydantic import BaseModel
# from openai import AsyncOpenAI
from google import genai
from google.genai import types
from app.config.settings import settings

T = TypeVar("T", bound=BaseModel)
logger = logging.getLogger(__name__)


class AIClient:
    def __init__(self) -> None:
        # Ініціалізація клієнта через правильний шлях імпорту
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )
        self.model_name = settings.LLM_MODEL
        self.temperature = settings.TEMPERATURE

    async def get_structured_data(self, prompt: str, response_model: Type[T], system_prompt: str = None) -> T:
        """
        Використовує Google GenAI SDK для отримання структурованих даних.
        """
        config = types.GenerateContentConfig(
            temperature=self.temperature,
            response_mime_type="application/json",
            response_schema=response_model,
            system_instruction=system_prompt
        )

        try:
            # Використовуємо асинхронний клієнт aio
            response = await self.client.aio.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=config
            )

            # Якщо SDK зміг розпарсити відповідь автоматично
            if response.parsed:
                return response.parsed

            # Запасний варіант парсингу
            return response_model.model_validate_json(response.text)

        except Exception as e:
            logger.error(f"Error with Gemini GenAI: {e}")
            raise