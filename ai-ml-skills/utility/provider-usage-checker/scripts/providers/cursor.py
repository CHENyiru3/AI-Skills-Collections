from __future__ import annotations

import datetime as dt
import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from .browser_cookies import BrowserCookieError, import_cookie_header
from .cookie_cache import CookieCache
from .models import Credits, Identity, UsageSnapshot, UsageWindow


def utcnow_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def cents_to_dollars(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return round(float(value) / 100.0, 2)
    except (TypeError, ValueError):
        return None


@dataclass
class CursorFetcher:
    browser: str = "auto"
    timeout: float = 20.0
    cache_dir: str | None = None
    debug: bool = False

    COOKIE_DOMAINS = ["cursor.com", ".cursor.com", "cursor.sh", ".cursor.sh", "authenticator.cursor.sh", ".authenticator.cursor.sh"]
    COOKIE_NAMES = {
        "WorkosCursorSessionToken",
        "__Secure-next-auth.session-token",
        "next-auth.session-token",
        "wos-session",
        "__Secure-wos-session",
        "authjs.session-token",
        "__Secure-authjs.session-token",
    }

    def _debug(self, message: str) -> None:
        if self.debug:
            print(f"[cursor-debug] {message}")

    def _request_json(self, url: str, cookie_header: str) -> dict[str, Any]:
        request = urllib.request.Request(
            url,
            headers={
                "Cookie": cookie_header,
                "User-Agent": "provider-usage-checker/0.1",
                "Accept": "application/json",
            },
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            return json.loads(response.read().decode())

    def resolve_cookie_header(self, cookie_header: str | None, cookie_header_file: str | None) -> tuple[str, str]:
        if cookie_header:
            return cookie_header.strip(), "manual"
        if cookie_header_file:
            return open(cookie_header_file).read().strip(), "manual-file"
        cache = CookieCache(self.cache_dir)
        cached = cache.load("cursor", max_age_seconds=900)
        if cached:
            return cached
        imported = import_cookie_header(self.browser, self.COOKIE_DOMAINS, cookie_names=self.COOKIE_NAMES)
        cache.save("cursor", imported.cookie_header, imported.source)
        return imported.cookie_header, imported.source

    def _window(self, name: str, used_cents: Any, limit_cents: Any, resets_at: str | None) -> UsageWindow | None:
        used = cents_to_dollars(used_cents)
        limit = cents_to_dollars(limit_cents)
        if used is None and limit is None:
            return None
        used_percent = None
        remaining_percent = None
        if used is not None and limit and limit > 0:
            used_percent = round((used / limit) * 100.0, 2)
            remaining_percent = round(max(0.0, 100.0 - used_percent), 2)
        return UsageWindow(
            name=name,
            used_percent=used_percent,
            remaining_percent=remaining_percent,
            resets_at=resets_at,
            reset_description=resets_at,
        )

    def fetch(self, cookie_header: str | None = None, cookie_header_file: str | None = None) -> UsageSnapshot:
        try:
            header, source_label = self.resolve_cookie_header(cookie_header, cookie_header_file)
        except BrowserCookieError as exc:
            raise RuntimeError(str(exc)) from exc
        try:
            auth_me = self._request_json("https://cursor.com/api/auth/me", header)
            usage_summary = self._request_json("https://cursor.com/api/usage-summary", header)
        except urllib.error.HTTPError as exc:
            raise RuntimeError(f"Cursor API request failed with HTTP {exc.code}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Cursor API request failed: {exc.reason}") from exc

        user_id = auth_me.get("user", {}).get("id") or auth_me.get("id")
        legacy_usage = None
        if user_id:
            try:
                legacy_usage = self._request_json(f"https://cursor.com/api/usage?user={user_id}", header)
            except Exception as exc:
                self._debug(f"legacy usage endpoint failed: {exc}")

        individual = usage_summary.get("individualUsage") or {}
        plan = individual.get("plan") or {}
        on_demand = individual.get("onDemand") or {}
        billing_end = usage_summary.get("billingCycleEnd")

        extras = {
            "billing_cycle_start": usage_summary.get("billingCycleStart"),
            "billing_cycle_end": billing_end,
            "membership_type": usage_summary.get("membershipType"),
            "limit_type": usage_summary.get("limitType"),
            "is_unlimited": usage_summary.get("isUnlimited"),
            "plan_breakdown": plan.get("breakdown"),
            "plan_auto_percent_used": plan.get("autoPercentUsed"),
            "plan_api_percent_used": plan.get("apiPercentUsed"),
            "plan_total_percent_used": plan.get("totalPercentUsed"),
            "legacy_request_usage": legacy_usage,
        }
        provider_cost = {
            "used_usd": cents_to_dollars(on_demand.get("used")),
            "limit_usd": cents_to_dollars(on_demand.get("limit")),
            "remaining_usd": cents_to_dollars(on_demand.get("remaining")),
        }

        return UsageSnapshot(
            provider="cursor",
            source="web-api",
            fetched_at=utcnow_iso(),
            identity=Identity(
                email=(auth_me.get("user") or {}).get("email") or auth_me.get("email"),
                organization=None,
                login_method=source_label,
            ),
            windows={
                "primary": self._window("included_plan", plan.get("used"), plan.get("limit"), billing_end),
                "secondary": self._window("on_demand", on_demand.get("used"), on_demand.get("limit"), billing_end),
                "tertiary": None,
            },
            credits=Credits(),
            extras={**extras, "provider_cost": provider_cost},
            raw={"source_details": {"user_id_present": bool(user_id)}},
        )
