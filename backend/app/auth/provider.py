from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Identity:
    subject: str
    email: str | None = None
    name: str | None = None


class IdentityProvider(ABC):
    @abstractmethod
    async def verify(self, token: str) -> Identity:
        raise NotImplementedError
