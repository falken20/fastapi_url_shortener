# by Richi Rod AKA @richionline / falken20

# Library that uses type annotation to validate data and manage settings.
from pydantic import BaseSettings
# Library to cache the data
from functools import lru_cache


class Settings(BaseSettings):
    # pydantic will automatically assume those default values if it doesn’t
    # find the corresponding environment variables.
    env_name: str = "Local"
    base_url: str = "http://localhost:8080"
    db_url: str = "sqlite:///./shortener.db"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
