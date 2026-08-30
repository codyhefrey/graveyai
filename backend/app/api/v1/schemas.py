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
    text: str = Field(min_length=1, max_length=20000)
    source: str = Field(default="api", min_length=1, max_length=500)


class RAGDocumentResponse(BaseModel):
    id: str
    text: str
    source: str


class RAGSearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=8000)
    top_k: int = Field(default=5, ge=1, le=20)


class RAGResult(BaseModel):
    id: str
    text: str
    score: float
    source: str


class RAGSearchResponse(BaseModel):
    results: list[RAGResult]


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
