from abc import ABC, abstractmethod


class EmbeddingProvider(ABC):
    """Provider-agnostic interface for generating vector embeddings."""

    @abstractmethod
    async def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError
