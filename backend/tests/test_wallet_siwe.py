from datetime import timedelta

from eth_account import Account
from eth_account.messages import encode_defunct

from app.wallet.siwe import create_challenge, recover_address


def test_siwe_challenge_is_nonce_bound_and_recoverable() -> None:
    account = Account.create()
    challenge = create_challenge(
        domain="graveyai.example",
        uri="https://graveyai.example/wallet",
        chain_id=1,
        address=account.address,
    )

    signature = Account.sign_message(
        encode_defunct(text=challenge.message()),
        account.key,
    ).signature.hex()

    assert recover_address(challenge.message(), signature).lower() == account.address.lower()
    assert len(challenge.nonce) >= 32
    assert challenge.expiration_time > challenge.issued_at
    assert challenge.expiration_time - challenge.issued_at == timedelta(seconds=300)
