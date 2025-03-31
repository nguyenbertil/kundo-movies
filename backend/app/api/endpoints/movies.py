from app.models.movie import MovieDetail, MovieSearch
from app.services.omdb_service import omdb_service
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/", response_model=MovieSearch)
async def search_movies(
    query: str = Query(..., description="Movie title to search for"),
    page: int = Query(1, description="Page number for pagination"),
):
    movies = await omdb_service.search_movies(query, page)
    return MovieSearch(**movies)


@router.get("/{imdb_id}/", response_model=MovieDetail)
async def get_movie_details(imdb_id: str):
    movie_details = await omdb_service.get_movie_details(imdb_id=imdb_id)
    return MovieDetail(**movie_details)
