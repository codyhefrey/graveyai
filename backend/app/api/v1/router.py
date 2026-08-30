from fastapi import APIRouter, Depends

from app.ai.base import AIProvider
from app.ai.mock import MockAIProvider
from app.api.v1.schemas import ChatRequest, ChatResponse
from app.core.config import Settings, get_settings

router = APIRouter()


def get_ai_provider(settings: Settings = Depends(get_settings)) -> AIProvider:
    if settings.ai_provider == "mock":
        return MockAIProvider()
    raise RuntimeError(f"Unsupported AI provider: {settings.ai_provider}")


@router.post("/chat", response_model=ChatResponse, tags=["chat"])
async def chat(
    request: ChatRequest,
    provider: AIProvider = Depends(get_ai_provider),
    settings: Settings = Depends(get_settings),
) -> ChatResponse:
    response = await provider.generate(request.message)
    return ChatResponse(response=response, provider=settings.ai_provider, model=settings.ai_model)
