from fastapi import FastAPI

from app.api.v1.router import router as api_v1_router
from app.api.v1.schemas import HealthResponse
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for the GraveyAI platform.",
)

app.include_router(api_v1_router, prefix=settings.api_v1_prefix)


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    """Return a lightweight service health response."""
    return HealthResponse(
        status="ok",
        service="graveyai-api",
        version=settings.app_version,
    )
