"""Minimal ERC-4361/SIWE challenge and signature verification primitives."""

from dataclasses import dataclass
from datetime import datetime, timezone
import secrets

from eth_account import Account
from eth_account.messages import encode_defunct


@dataclass(frozen=True)
class SIWEChallenge:
    nonce: str
    domain: str
    uri: str
    chain_id: int
    address: str
    issued_at: datetime
    expiration_time: datetime

    def message(self) -> str:
        return (
            f"{self.domain} wants you to sign in with your Ethereum account:\n"
            f"{self.address}\n\n"
            "Sign in to GraveyAI. This request will not initiate a blockchain transaction.\n\n"
            f"URI: {self.uri}\n"
            "Version: 1\n"
            f"Chain ID: {self.chain_id}\n"
            f"Nonce: {self.nonce}\n"
            f"Issued At: {self.issued_at.isoformat().replace('+00:00', 'Z')}\n"
            f"Expiration Time: {self.expiration_time.isoformat().replace('+00:00', 'Z')}"
        )


def create_challenge(*, domain: str, uri: str, chain_id: int, address: str, ttl_seconds: int = 300) -> SIWEChallenge:
    now = datetime.now(timezone.utc)
    return SIWEChallenge(
        nonce=secrets.token_urlsafe(24),
        domain=domain,
        uri=uri,
        chain_id=chain_id,
        address=address,
        issued_at=now,
        expiration_time=now.replace(microsecond=0) + __import__('datetime').timedelta(seconds=ttl_seconds),
    )


def recover_address(message: str, signature: str) -> str:
    recovered = Account.recover_message(encode_defunct(text=message), signature=signature)
    return recovered
