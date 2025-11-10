from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):
    DB_URL: str

    @field_validator('DB_URL')
    def must_be_postgres(cls, v: str) -> str:
        if not v.startswith("postgresql+psycopg://"):
            raise ValueError("DB_URL must be a PostgreSQL URL (start with 'postgresql://')")
        return v

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

settings = Settings()