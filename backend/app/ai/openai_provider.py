from openai import AsyncOpenAI

from app.ai.base import AIProvider


class OpenAIProvider(AIProvider):
    """OpenAI-backed provider using the Responses API."""

    def __init__(self, api_key: str, model: str) -> None:
        self.model = model
        self.client = AsyncOpenAI(api_key=api_key)

    async def generate(self, prompt: str) -> str:
        response = await self.client.responses.create(
            model=self.model,
            input=prompt,
        )
        return response.output_text
