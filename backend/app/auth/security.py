import hashlib
import hmac
import secrets


def generate_session_token() -> str:
    """Generate an opaque, high-entropy session token."""
    return secrets.token_urlsafe(32)


def token_fingerprint(token: str) -> str:
    """Store only a SHA-256 fingerprint when a token must be persisted."""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def constant_time_equal(left: str, right: str) -> bool:
    return hmac.compare_digest(left, right)
