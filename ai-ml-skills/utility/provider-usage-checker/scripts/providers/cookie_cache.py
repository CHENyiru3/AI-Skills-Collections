from __future__ import annotations

import json
import os
import time
from pathlib import Path


class CookieCache:
    def __init__(self, cache_dir: str | None = None) -> None:
        base = cache_dir or os.path.join(Path.home(), "Library", "Caches", "provider-usage-checker")
        self.cache_dir = Path(base)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _path(self, provider: str) -> Path:
        return self.cache_dir / f"{provider}-cookie.json"

    def load(self, provider: str, max_age_seconds: int) -> tuple[str, str] | None:
        path = self._path(provider)
        if not path.exists():
            return None
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            return None
        stored_at = payload.get("stored_at", 0)
        if time.time() - stored_at > max_age_seconds:
            return None
        cookie_header = payload.get("cookie_header")
        source = payload.get("source", "cache")
        if not cookie_header:
            return None
        return cookie_header, source

    def save(self, provider: str, cookie_header: str, source: str) -> None:
        payload = {
            "cookie_header": cookie_header,
            "source": source,
            "stored_at": time.time(),
        }
        self._path(provider).write_text(json.dumps(payload, indent=2))
