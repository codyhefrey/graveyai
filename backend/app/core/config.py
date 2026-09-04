from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "GraveyAI API"
    app_version: str = "0.7.0"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://graveyai:change-me@localhost:5432/graveyai"

    ai_provider: str = "mock"
    ai_model: str = "gpt-5.6-luna"
    openai_api_key: str | None = None

    voice_stt_provider: str = "mock"
    voice_tts_provider: str = "mock"
    voice_max_audio_bytes: int = 10_000_000

    identity_provider: str = "mock"
    development_identity_token: str | None = "development-token"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
