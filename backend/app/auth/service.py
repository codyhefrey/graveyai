from abc import ABC, abstractmethod

from app.auth.models import User


class AuthService(ABC):
    """Provider-agnostic authentication contract.

    Production implementations should use a managed identity provider or
    a properly secured database-backed identity service rather than storing
    plaintext passwords in the application.
    """

    @abstractmethod
    async def authenticate(self, email: str, credential: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, user_id: str) -> User | None:
        raise NotImplementedError
