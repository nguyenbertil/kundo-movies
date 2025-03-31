import httpx
from fastapi import HTTPException
from app.core.config import settings


class OMDBService:
    def __init__(self):
        self.api_key = settings.OMDB_API_KEY
        self.base_url = settings.OMDB_API_URL

    async def search_movies(self, query: str, page: int = 1) -> dict:
        params = {"apikey": self.api_key, "s": query, "page": page}

        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params=params)

            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error fetching data from OMDB API",
                )

            data = response.json()

            return data

    async def get_movie_details(self, imdb_id: str) -> dict:
        params = {"apikey": self.api_key, "i": imdb_id}

        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params=params)

            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error fetching data from OMDB API",
                )

            data = response.json()

            if data.get("Response") == "False":
                raise HTTPException(
                    status_code=404, detail=data.get("Error", "Movie not found")
                )

            return data


omdb_service = OMDBService()
