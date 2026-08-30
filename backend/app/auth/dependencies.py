from fastapi import Header, HTTPException, status


def require_bearer_token(authorization: str | None = Header(default=None)) -> str:
    """Require a bearer token; token verification is delegated to the identity provider."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    token = authorization.removeprefix("Bearer ").strip()
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    return token
