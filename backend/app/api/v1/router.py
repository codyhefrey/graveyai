from fastapi import APIRouter, Depends, HTTPException, UploadFile, status

from app.ai.base import AIProvider
from app.ai.mock import MockAIProvider
from app.ai.openai_provider import OpenAIProvider
from app.api.v1.auth import router as auth_router
from app.api.v1.schemas import ChatRequest, ChatResponse, VoiceResponse, VoiceTranscriptionResponse
from app.auth.dependencies import require_bearer_token
from app.core.config import Settings, get_settings
from app.voice.base import STTProvider, TTSProvider
from app.voice.mock import MockSTTProvider, MockTTSProvider

router = APIRouter()
router.include_router(auth_router)


def get_ai_provider(settings: Settings = Depends(get_settings)) -> AIProvider:
    if settings.ai_provider == "mock":
        return MockAIProvider()

    if settings.ai_provider == "openai":
        if not settings.openai_api_key:
            raise HTTPException(
                status_code=503,
                detail="OpenAI provider is enabled but OPENAI_API_KEY is not configured.",
            )
        return OpenAIProvider(api_key=settings.openai_api_key, model=settings.ai_model)

    raise HTTPException(status_code=500, detail=f"Unsupported AI provider: {settings.ai_provider}")


def get_stt_provider(settings: Settings = Depends(get_settings)) -> STTProvider:
    if settings.voice_stt_provider == "mock":
        return MockSTTProvider()
    raise HTTPException(status_code=500, detail=f"Unsupported STT provider: {settings.voice_stt_provider}")


def get_tts_provider(settings: Settings = Depends(get_settings)) -> TTSProvider:
    if settings.voice_tts_provider == "mock":
        return MockTTSProvider()
    raise HTTPException(status_code=500, detail=f"Unsupported TTS provider: {settings.voice_tts_provider}")


@router.post("/chat", response_model=ChatResponse, tags=["chat"])
async def chat(
    request: ChatRequest,
    provider: AIProvider = Depends(get_ai_provider),
    settings: Settings = Depends(get_settings),
) -> ChatResponse:
    response = await provider.generate(request.message)
    return ChatResponse(response=response, provider=settings.ai_provider, model=settings.ai_model)


@router.post("/voice/transcribe", response_model=VoiceTranscriptionResponse, tags=["voice"])
async def transcribe_voice(
    audio: UploadFile,
    _: str = Depends(require_bearer_token),
    provider: STTProvider = Depends(get_stt_provider),
    settings: Settings = Depends(get_settings),
) -> VoiceTranscriptionResponse:
    data = await audio.read(settings.voice_max_audio_bytes + 1)
    if len(data) > settings.voice_max_audio_bytes:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Audio file is too large")
    result = await provider.transcribe(data, audio.filename or "voice-input", audio.content_type)
    return VoiceTranscriptionResponse(text=result.text, language=result.language, provider=result.provider)


@router.post("/voice/respond", response_model=VoiceResponse, tags=["voice"])
async def voice_respond(
    audio: UploadFile,
    language: str = "en",
    _: str = Depends(require_bearer_token),
    stt: STTProvider = Depends(get_stt_provider),
    tts: TTSProvider = Depends(get_tts_provider),
    ai: AIProvider = Depends(get_ai_provider),
    settings: Settings = Depends(get_settings),
) -> VoiceResponse:
    data = await audio.read(settings.voice_max_audio_bytes + 1)
    if len(data) > settings.voice_max_audio_bytes:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Audio file is too large")
    transcription = await stt.transcribe(data, audio.filename or "voice-input", audio.content_type)
    ai_response = await ai.generate(transcription.text)
    await tts.synthesize(ai_response, language=language)
    return VoiceResponse(
        text=ai_response,
        language=language,
        stt_provider=transcription.provider,
        ai_provider=settings.ai_provider,
        ai_model=settings.ai_model,
        tts_provider=settings.voice_tts_provider,
    )
