import httpx
import pytest
import pytest_asyncio
import respx
from app.services.omdb_service import OMDBService
from fastapi import HTTPException

TEST_BASE_URL = "https://test-omdb-api.com"
TEST_API_KEY = "test_api_key"


@pytest_asyncio.fixture
async def omdb_service():
    service = OMDBService()
    service.api_key = TEST_API_KEY
    service.base_url = TEST_BASE_URL
    return service


@pytest.mark.asyncio
@respx.mock
async def test_search_movies_success(omdb_service):
    mock_response = {
        "Search": [
            {
                "Title": "My Movie",
                "Year": "2025",
                "imdbID": "ASDFLKJ",
                "Type": "movie",
                "Poster": "something",
            }
        ],
        "totalResults": "1",
        "Response": "True",
    }
    route = respx.get(
        TEST_BASE_URL,
        params={"apikey": TEST_API_KEY, "s": "test", "page": 1},
    ).mock(return_value=httpx.Response(200, json=mock_response))

    result = await omdb_service.search_movies("test")

    assert route.called
    assert result == mock_response


@pytest.mark.asyncio
@respx.mock
async def test_search_movies_api_error(omdb_service):
    respx.get(
        TEST_BASE_URL,
        params={"apikey": TEST_API_KEY, "s": "test", "page": 1},
    ).mock(return_value=httpx.Response(500))

    with pytest.raises(HTTPException) as exception_info:
        await omdb_service.search_movies("test")

    assert exception_info.value.status_code == 500
    assert exception_info.value.detail == "Error fetching data from OMDB API"


@pytest.mark.asyncio
@respx.mock
async def test_get_movie_details_success(omdb_service):

    mock_response = {
        "Title": "WWA: The Inception",
        "Year": "2001",
        "Rated": "N/A",
        "Released": "26 Oct 2001",
        "Runtime": "N/A",
        "Genre": "Action, Sport",
        "Director": "N/A",
        "Writer": "Jeremy Borash",
        "Actors": "Bret Hart, Jeff Jarrett, Brian James, David Heath",
        "Plot": "N/A",
        "Language": "English",
        "Country": "Australia",
        "Awards": "N/A",
        "Poster": "https://m.media-amazon.com/images/M/MV5BNTEyNGJjMTMtZjZhZC00ODFkLWIyYzktN2JjMTcwMmY5MDJlXkEyXkFqcGdeQXVyNDkwMzY5NjQ@._V1_SX300.jpg",
        "Ratings": [{"Source": "Internet Movie Database", "Value": "5.9/10"}],
        "Metascore": "N/A",
        "imdbRating": "5.9",
        "imdbVotes": "24",
        "imdbID": "tt0311992",
        "Type": "movie",
        "DVD": "N/A",
        "BoxOffice": "N/A",
        "Production": "N/A",
        "Website": "N/A",
        "Response": "True",
    }
    route = respx.get(
        "https://test-omdb-api.com", params={"apikey": "test_api_key", "i": "tt1234567"}
    ).mock(return_value=httpx.Response(200, json=mock_response))

    result = await omdb_service.get_movie_details("tt1234567")

    assert route.called
    assert result == mock_response


@pytest.mark.asyncio
@respx.mock
async def test_get_movie_details_not_found(omdb_service):
    mock_response = {"Response": "False", "Error": "Movie not found"}

    respx.get(TEST_BASE_URL, params={"apikey": TEST_API_KEY, "i": "invalid_id"}).mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    with pytest.raises(HTTPException) as exception_info:
        await omdb_service.get_movie_details("invalid_id")

    assert exception_info.value.status_code == 404
    assert exception_info.value.detail == "Movie not found"


@pytest.mark.asyncio
@respx.mock
async def test_get_movie_details_api_error(omdb_service):
    respx.get(TEST_BASE_URL, params={"apikey": TEST_API_KEY, "i": "something"}).mock(
        return_value=httpx.Response(500)
    )

    with pytest.raises(HTTPException) as exc_info:
        await omdb_service.get_movie_details("something")

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Error fetching data from OMDB API"
