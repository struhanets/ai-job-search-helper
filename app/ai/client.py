import logging
from typing import Type, TypeVar
from pydantic import BaseModel
from openai import AsyncOpenAI

from app.config.settings import settings

T = TypeVar("T", bound=BaseModel)
logger = logging.getLogger(__name__)

class AIClient:
    def __init__(self) -> None:
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL
        self.temperature = settings.TEMPERATURE

    async def get_structured_data(self, prompt: str, response_model: Type[T], system_prompt: str = None) -> T:
        messages = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt
                }
            )
        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        try:
            completion = await self.client.chat.completions.parse(
                model=self.model,
                messages=messages,
                response_format=response_model,
                temperature=self.temperature
            )
            return completion.choices[0].message.parsed
        except Exception as e:
            logger.error(f"Error parsing response: {e}")
            raise