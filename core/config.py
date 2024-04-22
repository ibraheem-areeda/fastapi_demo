from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Fast Api Demo"
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    REDIS_HOST: str
    REDIS_PORT: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')