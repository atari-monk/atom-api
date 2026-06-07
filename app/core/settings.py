from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "record-api"
    env: str = "dev"

    model_config = {"env_file": ".env"}


settings = Settings()