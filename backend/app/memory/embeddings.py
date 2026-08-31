"""Embedding provider abstraction for semantic memory."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Embedding:
    values: tuple[float, ...]
    model: str
    version: str


class EmbeddingProvider(Protocol):
    def embed(self, text: str) -> Embedding: ...


class DeterministicEmbeddingProvider:
    """Development-only provider for contract tests; not semantic AI."""

    def __init__(self, dimensions: int = 1536) -> None:
        if dimensions <= 0:
            raise ValueError("dimensions must be positive")
        self.dimensions = dimensions

    def embed(self, text: str) -> Embedding:
        if not text.strip():
            raise ValueError("text is required")
        # Stable zero vector keeps development deterministic without pretending
        # to provide meaningful semantic similarity.
        return Embedding(
            values=tuple(0.0 for _ in range(self.dimensions)),
            model="deterministic-development",
            version="1",
        )
