from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Transcription:
    text: str
    language: str
    provider: str


@dataclass(frozen=True)
class SpeechAudio:
    audio: bytes
    media_type: str
    provider: str


class STTProvider(ABC):
    @abstractmethod
    async def transcribe(self, audio: bytes, filename: str, content_type: str | None = None) -> Transcription:
        raise NotImplementedError


class TTSProvider(ABC):
    @abstractmethod
    async def synthesize(self, text: str, language: str = "en") -> SpeechAudio:
        raise NotImplementedError
