from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from uuid import UUID

from app.ai.base import AIProvider
from app.ai.mock import MockAIProvider
from app.ai.openai_provider import OpenAIProvider
from app.api.v1.auth import router as auth_router
from app.api.v1.schemas import (
    ChatRequest, ChatResponse, MemoryCreateRequest, MemoryListResponse,
    MemoryResponse, RAGDocumentRequest, RAGDocumentResponse, RAGResult,
    RAGSearchRequest, RAGSearchResponse, VoiceResponse,
    VoiceTranscriptionResponse,
)
from app.auth.dependencies import require_identity
from app.auth.provider import Identity
from app.core.config import Settings, get_settings
from app.memory.models import MemoryItem, MemoryScope
from app.memory.policy import MemoryPolicy
from app.memory.store import InMemoryMemoryStore
from app.rag.service import RAGService
from app.voice.base import STTProvider, TTSProvider
from app.voice.mock import MockSTTProvider, MockTTSProvider

router = APIRouter()
router.include_router(auth_router)
_rag = RAGService()
_memory_store = InMemoryMemoryStore()
_memory_policy = MemoryPolicy()


def get_ai_provider(settings: Settings = Depends(get_settings)) -> AIProvider:
    if settings.ai_provider == "mock":
        if settings.environment != "development":
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Mock AI provider is development-only",
            )
        return MockAIProvider()
    if settings.ai_provider == "openai":
        if not settings.openai_api_key:
            raise HTTPException(status_code=503, detail="OpenAI provider is enabled but OPENAI_API_KEY is not configured.")
        return OpenAIProvider(api_key=settings.openai_api_key, model=settings.ai_model)
    raise HTTPException(status_code=500, detail=f"Unsupported AI provider: {settings.ai_provider}")


def get_stt_provider(settings: Settings = Depends(get_settings)) -> STTProvider:
    if settings.voice_stt_provider == "mock":
        if settings.environment != "development":
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Mock STT provider is development-only",
            )
        return MockSTTProvider()
    raise HTTPException(status_code=500, detail=f"Unsupported STT provider: {settings.voice_stt_provider}")


def get_tts_provider(settings: Settings = Depends(get_settings)) -> TTSProvider:
    if settings.voice_tts_provider == "mock":
        if settings.environment != "development":
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Mock TTS provider is development-only",
            )
        return MockTTSProvider()
    raise HTTPException(status_code=500, detail=f"Unsupported TTS provider: {settings.voice_tts_provider}")


def _memory_response(item: MemoryItem) -> MemoryResponse:
    return MemoryResponse(
        memory_id=item.memory_id,
        content=item.content,
        scope=item.scope.value,
        source=item.source,
        created_at=item.created_at,
        expires_at=item.expires_at,
        metadata=item.metadata,
    )


@router.post("/chat", response_model=ChatResponse, tags=["chat"])
async def chat(
    request: ChatRequest,
    _: Identity = Depends(require_identity),
    provider: AIProvider = Depends(get_ai_provider),
    settings: Settings = Depends(get_settings),
) -> ChatResponse:
    response = await provider.generate(request.message)
    return ChatResponse(response=response, provider=settings.ai_provider, model=settings.ai_model)


@router.post("/memory", response_model=MemoryResponse, status_code=status.HTTP_201_CREATED, tags=["memory"])
async def create_memory(
    request: MemoryCreateRequest,
    identity: Identity = Depends(require_identity),
) -> MemoryResponse:
    try:
        scope = MemoryScope(request.scope)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail="Unsupported memory scope") from exc

    decision = _memory_policy.evaluate(
        owner_id=identity.subject,
        content=request.content,
        scope=scope,
    )
    if not decision.allowed:
        raise HTTPException(status_code=422, detail=decision.reason)

    item = MemoryItem(
        owner_id=identity.subject,
        content=request.content,
        scope=scope,
        source=request.source,
        expires_at=decision.expires_at,
        metadata=request.metadata,
    )
    _memory_store.save(item)
    return _memory_response(item)


@router.get("/memory", response_model=MemoryListResponse, tags=["memory"])
async def list_memory(
    scope: str | None = None,
    identity: Identity = Depends(require_identity),
) -> MemoryListResponse:
    parsed_scope: MemoryScope | None = None
    if scope is not None:
        try:
            parsed_scope = MemoryScope(scope)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail="Unsupported memory scope") from exc
    items = _memory_store.list(identity.subject, parsed_scope)
    return MemoryListResponse(items=[_memory_response(item) for item in items])


@router.get("/memory/{memory_id}", response_model=MemoryResponse, tags=["memory"])
async def get_memory(
    memory_id: UUID,
    identity: Identity = Depends(require_identity),
) -> MemoryResponse:
    item = _memory_store.get(memory_id, identity.subject)
    if item is None:
        raise HTTPException(status_code=404, detail="Memory item not found")
    return _memory_response(item)


@router.delete("/memory/{memory_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["memory"])
async def delete_memory(
    memory_id: UUID,
    identity: Identity = Depends(require_identity),
) -> None:
    if not _memory_store.delete(memory_id, identity.subject):
        raise HTTPException(status_code=404, detail="Memory item not found")


@router.post("/rag/documents", response_model=RAGDocumentResponse, tags=["rag"])
async def add_rag_document(
    request: RAGDocumentRequest,
    identity: Identity = Depends(require_identity),
) -> RAGDocumentResponse:
    chunks, provenance = _rag.ingest(identity.subject, request.document_id, request.text)
    return RAGDocumentResponse(
        document_id=request.document_id,
        chunks=len(chunks),
        content_hash=provenance.content_hash,
        hash_algorithm=provenance.hash_algorithm,
        chain=provenance.chain,
        quantum_ready=provenance.quantum_ready,
    )


@router.post("/rag/search", response_model=RAGSearchResponse, tags=["rag"])
async def search_rag(
    request: RAGSearchRequest,
    identity: Identity = Depends(require_identity),
) -> RAGSearchResponse:
    results = _rag.search(identity.subject, request.query, request.top_k)
    return RAGSearchResponse(results=[RAGResult(
        document_id=r.chunk.document_id,
        chunk_id=r.chunk.chunk_id,
        text=r.chunk.text,
        score=r.score,
        content_hash=r.chunk.content_hash,
    ) for r in results])


@router.post("/voice/transcribe", response_model=VoiceTranscriptionResponse)
async def transcribe_voice(
    audio: UploadFile,
    _: Identity = Depends(require_identity),
    provider: STTProvider = Depends(get_stt_provider),
    settings: Settings = Depends(get_settings),
) -> VoiceTranscriptionResponse:
    data = await audio.read(settings.voice_max_audio_bytes + 1)
    if len(data) > settings.voice_max_audio_bytes:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Audio file is too large")
    result = await provider.transcribe(data, audio.filename or "voice-input", audio.content_type)
    return VoiceTranscriptionResponse(text=result.text, language=result.language, provider=result.provider)


@router.post("/voice/respond", response_model=VoiceResponse)
async def voice_respond(
    audio: UploadFile,
    language: str = "en",
    _: Identity = Depends(require_identity),
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
