from fastapi import APIRouter

from app.api.routes.resume import router as resume_router
from app.api.routes.analysis import router as analysis_router

api_router = APIRouter()

api_router.include_router(
    resume_router
)

api_router.include_router(
    analysis_router
)