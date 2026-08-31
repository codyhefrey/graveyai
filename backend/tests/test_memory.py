from datetime import datetime, timedelta, timezone

from app.memory.models import MemoryItem, MemoryScope
from app.memory.policy import MemoryPolicy
from app.memory.store import InMemoryMemoryStore


def test_policy_assigns_scope_ttl():
    policy = MemoryPolicy()
    decision = policy.evaluate(owner_id="user-1", content="research context", scope=MemoryScope.RESEARCH)

    assert decision.allowed is True
    assert decision.expires_at is not None
    assert decision.expires_at > datetime.now(timezone.utc)


def test_policy_rejects_empty_content():
    decision = MemoryPolicy().evaluate(owner_id="user-1", content=" ", scope=MemoryScope.USER)
    assert decision.allowed is False


def test_store_isolates_memory_by_owner():
    store = InMemoryMemoryStore()
    item = MemoryItem(owner_id="user-1", content="private", scope=MemoryScope.USER)
    store.save(item)

    assert store.get(item.memory_id, "user-1") == item
    assert store.get(item.memory_id, "user-2") is None


def test_expired_memory_is_not_readable():
    store = InMemoryMemoryStore()
    item = MemoryItem(
        owner_id="user-1",
        content="expired",
        scope=MemoryScope.SESSION,
        expires_at=datetime.now(timezone.utc) - timedelta(seconds=1),
    )
    store.save(item)

    assert store.get(item.memory_id, "user-1") is None


def test_delete_requires_owner():
    store = InMemoryMemoryStore()
    item = MemoryItem(owner_id="user-1", content="private", scope=MemoryScope.USER)
    store.save(item)

    assert store.delete(item.memory_id, "user-2") is False
    assert store.get(item.memory_id, "user-1") == item
    assert store.delete(item.memory_id, "user-1") is True
