from app.ai.client import AIClient
from app.models.domain.candidate import CandidateProfile
from app.parsers.pdf_parser import PDFParser


class ResumeParserService:
    def __init__(self):
        self.ai_client = AIClient()
        self.pdf_parser = PDFParser()
        # Загальний промпт, який класифікує поведінку самої моделі
        self._system_prompt = (
            "You are an expert HR Assistant and Technical Recruiter. "
            "Your task is to extract structured information from a resume text. "
            "Be precise, especially with tech stack and years of experience. "
            "If some information is missing, leave it as null."
        )

    async def parse_resume(self, file_content: bytes) -> CandidateProfile:
        raw_content = self.pdf_parser.extract_text(file_content)
        # промпт який дає вказівку витягнути відповідну інфо з нашого файлу
        prompt = f"Extract candidate profile from this resume text:\n\n{raw_content}"

        profile = await self.ai_client.get_structured_data(
            prompt=prompt,
            response_model=CandidateProfile,
            system_prompt=self._system_prompt
        )
        return profile