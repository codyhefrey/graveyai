from fastapi import Depends, Header, HTTPException, status

from app.auth.mock_provider import MockIdentityProvider
from app.auth.provider import Identity, IdentityProvider
from app.core.config import Settings, get_settings


def extract_bearer_token(authorization: str | None = Header(default=None)) -> str:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token.strip():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token.strip()


def get_identity_provider(settings: Settings = Depends(get_settings)) -> IdentityProvider:
    if settings.identity_provider == "mock" and settings.environment == "development":
        return MockIdentityProvider(settings.development_identity_token)
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="No production identity provider is configured",
    )


async def require_identity(
    token: str = Depends(extract_bearer_token),
    provider: IdentityProvider = Depends(get_identity_provider),
) -> Identity:
    return await provider.verify(token)


# Backwards-compatible dependency for routes that only need the verified token.
async def require_bearer_token(token: str = Depends(extract_bearer_token)) -> str:
    return token
