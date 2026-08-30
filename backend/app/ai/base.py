from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Provider-agnostic interface for text generation."""

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Generate a response from a prompt."""
        raise NotImplementedError
