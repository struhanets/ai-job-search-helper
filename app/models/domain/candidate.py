from pydantic import BaseModel, Field

from app.models.domain.common import LanguageSkill, ExperienceEntry, Education


class CandidateProfile(BaseModel):
    full_name: str | None = None
    title: str | None = None    # Python Backend Developer
    location: str | None = None
    years_of_experience: float | None = None
    seniority: str | None = None    # junior/middle/senior

    tech_stack: list[str] = Field(default_factory=list)
    languages: list[LanguageSkill] = Field(default_factory=list)
    experience: list[ExperienceEntry] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    summary: str | None = None

    additional_info: str | None = Field(
        None,
        description="Any other useful information "
                    "that does not fit into the structure"
    )

