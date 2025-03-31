from typing import List

from pydantic import BaseModel


class BaseMovie(BaseModel):
    imdbID: str
    Title: str
    Year: str
    Type: str
    Poster: str


class MovieSearch(BaseModel):
    Search: List[BaseMovie]
    totalResults: str
    Response: str


class MovieDetail(BaseMovie):
    Rated: str
    Released: str
    Runtime: str
    Genre: str
    Director: str
    Writer: str
    Actors: str
    Plot: str
    Language: str
    Country: str
    Awards: str
    Ratings: List[dict]
    Metascore: str
    imdbRating: str
    imdbVotes: str
    DVD: str
    BoxOffice: str
    Production: str
    Website: str
    Response: str
