from app.config.settings import settings


class PromptLoader:
    @staticmethod
    def load(file_name: str) -> str:
        path = settings.PROMPTS_DIR / file_name
        return path.read_text(encoding="utf-8")