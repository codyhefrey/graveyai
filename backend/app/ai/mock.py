from .base import AIProvider


class MockAIProvider(AIProvider):
    """Deterministic provider used for local development and tests."""

    async def generate(self, prompt: str) -> str:
        cleaned = prompt.strip()
        return f"GraveyAI development response: {cleaned}" if cleaned else "GraveyAI development response."
