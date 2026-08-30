from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class RetrievedDocument:
    id: str
    text: str
    score: float
    source: str


class RAGProvider(Protocol):
    async def retrieve(self, query: str, top_k: int = 5) -> list[RetrievedDocument]: ...

    async def add(self, text: str, source: str = "memory") -> RetrievedDocument: ...
