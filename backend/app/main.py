from fastapi import FastAPI, APIRouter
from app.api.endpoints import movies
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

api_router = APIRouter()
api_router.include_router(movies.router, prefix="/movies", tags=["movies"])

app.include_router(api_router, prefix=settings.API_V1_STR)
