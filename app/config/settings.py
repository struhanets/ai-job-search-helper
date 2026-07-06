from pathlib import Path

from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    # Path to the root of a project
    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    # AI Settings
    # OPENAI_API_KEY: str
    GEMINI_API_KEY: str
    # LLM_MODEL: str = "gpt-4o"
    LLM_MODEL: str = "gemini-2.5-flash"
    TEMPERATURE: float = 0.0

    # Scraper Settings
    SCRAPER_DELAY_SECONDS: int = 2
    USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )

    # Storage
    DATA_DIR: Path = BASE_DIR / "data"
    PROMPTS_DIR: Path = BASE_DIR / "prompts"

    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()
