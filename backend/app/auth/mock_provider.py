from fastapi import HTTPException, status

from app.auth.provider import Identity, IdentityProvider


class MockIdentityProvider(IdentityProvider):
    """Development-only provider with an explicit configured token."""

    def __init__(self, expected_token: str | None) -> None:
        self.expected_token = expected_token

    async def verify(self, token: str) -> Identity:
        if not self.expected_token or token != self.expected_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return Identity(subject="dev:user", email=None, name="Development User")
