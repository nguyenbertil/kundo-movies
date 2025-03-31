import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    OMDB_API_KEY: str = os.getenv("OMDB_API_KEY", "placeholder_api_key")
    OMDB_API_URL: str = os.getenv("OMDB_API_URL", "http://www.omdbapi.com/")

settings = Settings()

