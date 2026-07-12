from pydantic import BaseModel, Field

from app.models.domain.common import WorkFormat, LanguageSkill, WorkPeriod


class Salary(BaseModel):
    min: float | None = None
    max: float | None = None
    currency: str | None = None
    period: WorkPeriod | None = None


class Vacancy(BaseModel):
    external_id: str | None = None
    apply_link: str | None = None
    source_url: str | None = None

    company: str | None = None
    role: str | None = None
    location: str | None = None
    seniority: str | None = None    # junior/middle/senior
    work_format: WorkFormat | None = None

    salary: Salary | None = None
    tech_stack: list[str] = Field(default_factory=list)
    languages: list[LanguageSkill] = Field(default_factory=list)

    posting_language: str | None = Field(
        None,
        description="ISO 639-1 language in which the ad is WRITTEN "
                    "(to be answered in the same), e.g. 'uk', 'en'"
    )
    additional_info: str | None = Field(
        None,
        description="Any other useful information"
    )
    raw_text: str | None = None


class VacancyAIData(Vacancy):
    seniority: str | None = None
    work_format: WorkFormat | None = None

    salary: Salary | None = None
    tech_stack: list[str] = Field(default_factory=list)
    languages: list[LanguageSkill] = Field(default_factory=list)

    posting_language: str | None = None
    additional_info: str | None = None
