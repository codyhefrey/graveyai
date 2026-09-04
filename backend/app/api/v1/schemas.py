from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000)


class ChatResponse(BaseModel):
    response: str
    provider: str
    model: str


class VoiceTranscriptionResponse(BaseModel):
    text: str
    language: str
    provider: str


class VoiceResponse(BaseModel):
    text: str
    language: str
    stt_provider: str
    ai_provider: str
    ai_model: str
    tts_provider: str


class RAGDocumentRequest(BaseModel):
    document_id: str = Field(min_length=1, max_length=200)
    text: str = Field(min_length=1, max_length=100000)


class RAGDocumentResponse(BaseModel):
    document_id: str
    chunks: int
    content_hash: str
    hash_algorithm: str
    chain: str
    quantum_ready: bool


class RAGSearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=8000)
    top_k: int = Field(default=5, ge=1, le=20)


class RAGResult(BaseModel):
    document_id: str
    chunk_id: str
    text: str
    score: float
    content_hash: str


class RAGSearchResponse(BaseModel):
    results: list[RAGResult]


class MemoryCreateRequest(BaseModel):
    content: str = Field(min_length=1, max_length=100000)
    scope: str = Field(min_length=1, max_length=32)
    source: str | None = Field(default=None, max_length=500)
    metadata: dict[str, str] = Field(default_factory=dict)


class MemoryResponse(BaseModel):
    memory_id: UUID
    content: str
    scope: str
    source: str | None
    created_at: datetime
    expires_at: datetime | None
    metadata: dict[str, str]


class MemoryListResponse(BaseModel):
    items: list[MemoryResponse]


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
