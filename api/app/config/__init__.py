import os
from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50

    class Config:
        env_file = ".env", f".env.{os.getenv('ENVIRONMENT', 'local')}"


@lru_cache()
def get_settings():
    return Settings()
