from __future__ import annotations

import json

from .models import UsageSnapshot


def snapshot_to_json(snapshot: UsageSnapshot) -> str:
    return json.dumps(snapshot.to_dict(), indent=2, sort_keys=True)


def _render_window(name: str, payload: dict | None) -> list[str]:
    if not payload:
        return [f"{name}: unavailable"]
    remaining = payload.get("remaining_percent")
    used = payload.get("used_percent")
    reset = payload.get("reset_description") or payload.get("resets_at") or "unknown reset"
    return [f"{name}: used={used} remaining={remaining} reset={reset}"]


def snapshot_to_text(snapshot: UsageSnapshot) -> str:
    data = snapshot.to_dict()
    lines = [
        f"provider: {data['provider']}",
        f"source: {data['source']}",
        f"fetched_at: {data['fetched_at']}",
    ]
    identity = data.get("identity") or {}
    if identity.get("email"):
        lines.append(f"email: {identity['email']}")
    if identity.get("login_method"):
        lines.append(f"login_method: {identity['login_method']}")
    for key in ("primary", "secondary", "tertiary"):
        lines.extend(_render_window(key, (data.get("windows") or {}).get(key)))
    credits = data.get("credits") or {}
    if credits.get("remaining") is not None:
        lines.append(f"credits_remaining: {credits['remaining']}")
    extras = data.get("extras") or {}
    for key, value in extras.items():
        if value in (None, [], {}, ""):
            continue
        lines.append(f"{key}: {value}")
    warnings = data.get("warnings") or []
    if warnings:
        lines.append("warnings:")
        for warning in warnings:
            lines.append(f"  - {warning}")
    return "\n".join(lines)
