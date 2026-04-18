from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class Identity:
    email: str | None = None
    organization: str | None = None
    login_method: str | None = None


@dataclass
class UsageWindow:
    name: str
    used_percent: float | None = None
    remaining_percent: float | None = None
    resets_at: str | None = None
    reset_description: str | None = None


@dataclass
class Credits:
    remaining: float | None = None
    purchase_url: str | None = None


@dataclass
class UsageSnapshot:
    provider: str
    source: str
    fetched_at: str
    identity: Identity = field(default_factory=Identity)
    windows: dict[str, UsageWindow | None] = field(default_factory=dict)
    credits: Credits = field(default_factory=Credits)
    extras: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

