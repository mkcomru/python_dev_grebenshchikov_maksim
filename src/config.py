from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    AUTHORS_DB_URL: str
    TECH_INFO_DB_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()