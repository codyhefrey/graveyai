from abc import ABC, abstractmethod

from app.rag.models import RetrievalResult


class Retriever(ABC):
    """Provider-agnostic retrieval interface for vector or hybrid search."""

    @abstractmethod
    async def search(self, query: str, limit: int = 5) -> list[RetrievalResult]:
        raise NotImplementedError
