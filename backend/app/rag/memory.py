import re
from dataclasses import dataclass
from uuid import uuid4

from app.rag.base import RetrievedDocument


@dataclass
class _Document:
    id: str
    text: str
    source: str
    terms: set[str]


class InMemoryRAGProvider:
    """Dependency-free development RAG store; replaceable with a vector DB later."""

    def __init__(self) -> None:
        self._documents: list[_Document] = []

    async def add(self, text: str, source: str = "memory") -> RetrievedDocument:
        document = _Document(str(uuid4()), text, source, _terms(text))
        self._documents.append(document)
        return RetrievedDocument(document.id, document.text, 1.0, document.source)

    async def retrieve(self, query: str, top_k: int = 5) -> list[RetrievedDocument]:
        query_terms = _terms(query)
        if not query_terms:
            return []
        scored = []
        for document in self._documents:
            overlap = len(query_terms & document.terms)
            if overlap:
                score = overlap / len(query_terms)
                scored.append(RetrievedDocument(document.id, document.text, score, document.source))
        scored.sort(key=lambda item: item.score, reverse=True)
        return scored[:top_k]


def _terms(text: str) -> set[str]:
    return {term for term in re.findall(r"[a-zA-Z0-9_]{2,}", text.lower())}
