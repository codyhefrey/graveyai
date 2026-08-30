from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000)


class ChatResponse(BaseModel):
    response: str
    provider: str
    model: str


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
