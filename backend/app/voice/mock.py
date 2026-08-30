from app.voice.base import STTProvider, TTSProvider, SpeechAudio, Transcription


class MockSTTProvider(STTProvider):
    """Development-only STT provider. Never sends audio to an external service."""

    async def transcribe(self, audio: bytes, filename: str, content_type: str | None = None) -> Transcription:
        return Transcription(
            text="[mock transcription] Voice input received by GraveyAI.",
            language="en",
            provider="mock-stt",
        )


class MockTTSProvider(TTSProvider):
    """Development-only TTS provider returning a deterministic empty audio payload."""

    async def synthesize(self, text: str, language: str = "en") -> SpeechAudio:
        return SpeechAudio(audio=b"", media_type="audio/mpeg", provider="mock-tts")
