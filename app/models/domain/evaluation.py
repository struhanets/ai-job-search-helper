from pydantic import BaseModel, Field

from app.models.domain.common import WorkFormat
from app.models.domain.vacancy import Salary


class SearchPreferences(BaseModel):
    """Це треба заповнювати руками, в резюме цього нема"""

    desired_role: list[str] = Field(default_factory=list)
    salary: Salary | None = None
    work_formats: list[WorkFormat] = Field(default_factory=list)
    locations: list[str] = Field(default_factory=list)
    must_have: list[str] = Field(default_factory=list)  # Обов'язкові умови
    deal_breakers: list[str] = Field(default_factory=list)  # Стоп слова (напр. Gambling)


class MatchResult(BaseModel):
    """How well the candidate matches the vacancy"""
    score: int = Field(ge=0, le=100)
    reason: list[str] = Field(default_factory=list)

