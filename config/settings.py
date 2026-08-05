# from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
#open_AI
    OPENAI_API_KEY: str 
# supabase
    SUPABASE_URL: str
    SUPABASE_KEY: str 

#SEARCH
    TAVILY_API_KEY: str 
    FIRECRAWL_API_KEY: str

settings: Settings = Settings()

__all__ = ["Settings", "settings"]
