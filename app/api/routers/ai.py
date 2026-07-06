from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.client import AIClient

router = APIRouter()

class TestResponse(BaseModel):
    message: str
    sentiment: str


@router.get("/test")
async def test_ai():
    client = AIClient()
    result = await client.get_structured_data(
        prompt="Tell me that you are ready to work in a very positive way.",
        response_model=TestResponse
    )
    return result
