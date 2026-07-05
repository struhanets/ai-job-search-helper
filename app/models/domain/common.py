from enum import Enum

from pydantic import BaseModel, Field


class WorkFormat(str, Enum):
    onsite = "onsite"
    remote = "remote"
    hybrid = "hybrid"

class LanguageSkill(BaseModel):
    language_code: str | None = Field(None, description="ISO 639-1 code, e.g., 'en', 'uk'")
    level: str | None = Field(None, description="CEFR level if specified, e.g., 'B2', 'C1', 'Native'")

class ExperienceEntry(BaseModel):
    """Last note in experience block"""
    company: str | None = None
    role: str | None = None
    years: float | None = Field(None, description="Years of experience")
    highlights: list[str] = Field(default_factory=list, description="main achievements")

class Education(BaseModel):
    degree: str | None = None
    field: str | None = None
    institution: str | None = None


class WorkPeriod(Enum):
    week = "week"
    month = "month"
    year = "year"
