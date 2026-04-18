from __future__ import annotations

import base64
import datetime as dt
import html
import json
import os
import pty
import re
import select
import subprocess
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from .browser_cookies import BrowserCookieError, import_cookie_header
from .cookie_cache import CookieCache
from .models import Credits, Identity, UsageSnapshot, UsageWindow


def utcnow_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


class HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.parts.append(text)

    def text(self) -> str:
        return "\n".join(self.parts)


def strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;?]*[A-Za-z]", "", text)


def snapshot_has_usable_data(snapshot: UsageSnapshot | None) -> bool:
    return bool(
        snapshot
        and (
            any(snapshot.windows.values())
            or snapshot.credits.remaining is not None
            or any(snapshot.extras.values())
        )
    )


def _decode_jwt_payload(token: str | None) -> dict[str, Any]:
    if not token or "." not in token:
        return {}
    try:
        payload = token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload.encode()).decode())
    except Exception:
        return {}


def _find_first(obj: Any, key: str) -> Any:
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for value in obj.values():
            found = _find_first(value, key)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = _find_first(value, key)
            if found is not None:
                return found
    return None


def _find_windows(obj: Any) -> list[dict[str, Any]]:
    windows: list[dict[str, Any]] = []
    if isinstance(obj, dict):
        if {"usedPercent"} <= set(obj.keys()) or {"used_percent"} <= set(obj.keys()):
            windows.append(obj)
        for value in obj.values():
            windows.extend(_find_windows(value))
    elif isinstance(obj, list):
        for value in obj:
            windows.extend(_find_windows(value))
    return windows


def parse_reset_description(text: str | None) -> tuple[str | None, str | None]:
    if not text:
        return None, None
    raw = text.strip().strip("()")
    now = dt.datetime.now()
    for fmt in ("%H:%M on %d %b", "%H:%M on %b %d", "%H:%M"):
        try:
            parsed = dt.datetime.strptime(raw, fmt)
            if "%d" not in fmt and "%b" not in fmt:
                candidate = now.replace(hour=parsed.hour, minute=parsed.minute, second=0, microsecond=0)
                if candidate < now:
                    candidate += dt.timedelta(days=1)
                return raw, candidate.astimezone(dt.timezone.utc).isoformat()
            candidate = parsed.replace(year=now.year)
            if candidate < now:
                candidate = candidate.replace(year=now.year + 1)
            return raw, candidate.astimezone(dt.timezone.utc).isoformat()
        except ValueError:
            continue
    return raw, None


def parse_rate_limits_from_text(text: str) -> dict[str, UsageWindow | None]:
    windows: dict[str, UsageWindow | None] = {"primary": None, "secondary": None, "tertiary": None}
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    specs = [
        ("primary", "5h", re.compile(r"5h limit", re.I)),
        ("secondary", "weekly", re.compile(r"weekly limit", re.I)),
        ("tertiary", "code_review", re.compile(r"code review|core review", re.I)),
    ]
    for slot, name, matcher in specs:
        for line in lines:
            if not matcher.search(line):
                continue
            pct_match = re.search(r"(\d{1,3})%\s*(?:remaining|left|used)?", line, re.I)
            used_percent = None
            remaining = None
            if pct_match:
                number = float(pct_match.group(1))
                if re.search(r"(remaining|left)", line, re.I):
                    remaining = number
                    used_percent = max(0.0, 100.0 - number)
                else:
                    used_percent = number
                    remaining = max(0.0, 100.0 - number)
            reset_match = re.search(r"(?:resets?|reset)\s*(?:at|on)?\s*([^)]+)$", line, re.I)
            reset_description, resets_at = parse_reset_description(reset_match.group(1) if reset_match else None)
            windows[slot] = UsageWindow(
                name=name,
                used_percent=used_percent,
                remaining_percent=remaining,
                resets_at=resets_at,
                reset_description=reset_description,
            )
            break
    return windows


def parse_credits_remaining(text: str) -> float | None:
    for pattern in (
        r"credits\s*remaining[^0-9]*([0-9][0-9.,]*)",
        r"credit\s*balance[^0-9]*([0-9][0-9.,]*)",
        r"credits:\s*([0-9][0-9.,]*)",
    ):
        match = re.search(pattern, text, re.I)
        if match:
            return float(match.group(1).replace(",", ""))
    return None


def parse_dashboard_email(html_text: str) -> str | None:
    for needle in ('id="client-bootstrap"', 'id="__NEXT_DATA__"'):
        match = re.search(rf'{needle}[^>]*>(.*?)</script>', html_text, re.S)
        if not match:
            continue
        try:
            payload = json.loads(html.unescape(match.group(1)))
        except json.JSONDecodeError:
            continue
        email = _find_first(payload, "email")
        if isinstance(email, str) and "@" in email:
            return email.strip()
    return None


def parse_dashboard_plan(html_text: str) -> str | None:
    for needle in ('id="client-bootstrap"', 'id="__NEXT_DATA__"'):
        match = re.search(rf'{needle}[^>]*>(.*?)</script>', html_text, re.S)
        if not match:
            continue
        try:
            payload = json.loads(html.unescape(match.group(1)))
        except json.JSONDecodeError:
            continue
        for key in ("chatgpt_plan_type", "planType", "accountPlan"):
            value = _find_first(payload, key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    return None


def parse_dashboard_auth_status(html_text: str) -> str | None:
    match = re.search(r'id="client-bootstrap"[^>]*>(.*?)</script>', html_text, re.S)
    if not match:
        return None
    try:
        payload = json.loads(html.unescape(match.group(1)))
    except json.JSONDecodeError:
        return None
    status = _find_first(payload, "authStatus")
    return status.strip() if isinstance(status, str) and status.strip() else None


def extract_html_text(html_text: str) -> str:
    parser = HTMLTextExtractor()
    parser.feed(html_text)
    return parser.text()


def parse_credit_history(html_text: str) -> list[dict[str, Any]]:
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", html_text, re.S | re.I)
    events: list[dict[str, Any]] = []
    for row in rows:
        cells = [re.sub(r"<[^>]+>", " ", cell) for cell in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S | re.I)]
        cleaned = [" ".join(cell.split()) for cell in cells if " ".join(cell.split())]
        if len(cleaned) >= 3 and re.search(r"\b20\d{2}\b", cleaned[0]):
            events.append({"date": cleaned[0], "service": cleaned[1], "credits_used": cleaned[2]})
    return events[:20]


def parse_usage_breakdown_from_html(html_text: str) -> list[dict[str, Any]]:
    matches = re.findall(r'"usageBreakdown(?:JSON)?":(\[.*?\])', html_text, re.S)
    for match in matches:
        try:
            payload = json.loads(match)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, list):
            return payload[:60]
    match = re.search(r"window\.__codexbarUsageBreakdownJSON\s*=\s*(['\"])(.*?)\1", html_text, re.S)
    if match:
        try:
            payload = json.loads(html.unescape(match.group(2)))
        except json.JSONDecodeError:
            return []
        if isinstance(payload, list):
            return payload[:60]
    return []


def parse_dashboard_purchase_url(html_text: str) -> str | None:
    patterns = (
        r'href="([^"]*(?:billing|credits|usage)[^"]*)"',
        r'"creditsPurchaseURL":"([^"]+)"',
    )
    for pattern in patterns:
        match = re.search(pattern, html_text, re.I)
        if not match:
            continue
        value = html.unescape(match.group(1))
        if value.startswith("/"):
            return f"https://chatgpt.com{value}"
        return value
    return None


def detect_dashboard_login_required(route: str | None, html_text: str, body_text: str) -> bool:
    lower = body_text.lower()
    auth_status = parse_dashboard_auth_status(html_text)
    if auth_status == "logged_out":
        return True
    if route and ("/login" in route or "/auth/" in route):
        return True
    return any(
        phrase in lower
        for phrase in (
            "log in",
            "sign in",
            "continue with google",
            "continue with apple",
            "continue with microsoft",
        )
    )


def parse_dashboard_code_review(body_text: str) -> float | None:
    patterns = (
        r"Code\s*review[^0-9%]*([0-9]{1,3})%\s*remaining",
        r"Core\s*review[^0-9%]*([0-9]{1,3})%\s*remaining",
    )
    for pattern in patterns:
        match = re.search(pattern, body_text, re.I)
        if match:
            return min(100.0, max(0.0, float(match.group(1))))
    return None


def compute_snapshot_richness(snapshot: UsageSnapshot | None) -> int:
    if not snapshot:
        return -1
    score = 0
    for window in snapshot.windows.values():
        if not window:
            continue
        score += 1
        if window.resets_at:
            score += 2
        if window.reset_description:
            score += 1
    if snapshot.credits.remaining is not None:
        score += 1
    if snapshot.credits.purchase_url:
        score += 2
    extras = snapshot.extras or {}
    if extras.get("code_review_remaining_percent") is not None:
        score += 2
    if extras.get("code_review_limit"):
        score += 1
    if extras.get("usage_breakdown"):
        score += 3
    if extras.get("credit_history"):
        score += 3
    if extras.get("account_plan"):
        score += 1
    return score


@dataclass
class CodexFetcher:
    browser: str = "auto"
    timeout: float = 20.0
    cache_dir: str | None = None
    debug: bool = False

    COOKIE_DOMAINS = ["chatgpt.com", ".chatgpt.com", "openai.com", ".openai.com"]
    DASHBOARD_URLS = [
        "https://chatgpt.com/codex/settings/usage",
        "https://chatgpt.com/codex/cloud/settings/analytics#usage",
    ]

    def _debug(self, message: str) -> None:
        if self.debug:
            print(f"[codex-debug] {message}")

    def _auth_path(self) -> Path:
        home = os.environ.get("CODEX_HOME") or str(Path.home() / ".codex")
        return Path(home) / "auth.json"

    def load_auth(self) -> tuple[dict[str, Any], Identity]:
        path = self._auth_path()
        data = json.loads(path.read_text())
        payload = _decode_jwt_payload(data.get("tokens", {}).get("id_token"))
        auth_claims = payload.get("https://api.openai.com/auth", {}) if isinstance(payload, dict) else {}
        email = payload.get("email") or _find_first(payload, "email")
        plan = auth_claims.get("chatgpt_plan_type") or payload.get("chatgpt_plan_type")
        identity = Identity(email=email, login_method=plan)
        return data, identity

    def _build_request(self, url: str, *, bearer: str | None = None, cookie_header: str | None = None) -> urllib.request.Request:
        headers = {
            "User-Agent": "provider-usage-checker/0.1",
            "Accept": "application/json, text/html;q=0.9,*/*;q=0.8",
        }
        if bearer:
            headers["Authorization"] = f"Bearer {bearer}"
        if cookie_header:
            headers["Cookie"] = cookie_header
        return urllib.request.Request(url, headers=headers)

    def fetch_oauth_usage(self) -> UsageSnapshot | None:
        data, identity = self.load_auth()
        access_token = data.get("tokens", {}).get("access_token")
        if not access_token:
            return None
        request = self._build_request("https://chatgpt.com/backend-api/wham/usage", bearer=access_token)
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode())
        except Exception as exc:
            self._debug(f"oauth usage fetch failed: {exc}")
            return None

        windows = _find_windows(payload)
        normalized: dict[str, UsageWindow | None] = {"primary": None, "secondary": None, "tertiary": None}
        for idx, item in enumerate(windows[:3]):
            used = item.get("usedPercent")
            if used is None:
                used = item.get("used_percent")
            if used is None:
                continue
            resets = item.get("resetsAt") or item.get("resetAt") or item.get("resets_at")
            resets_at = None
            if isinstance(resets, (int, float)):
                resets_at = dt.datetime.fromtimestamp(float(resets), tz=dt.timezone.utc).isoformat()
            normalized[("primary", "secondary", "tertiary")[idx]] = UsageWindow(
                name=("5h", "weekly", "extra")[idx],
                used_percent=float(used),
                remaining_percent=max(0.0, 100.0 - float(used)),
                resets_at=resets_at,
                reset_description=None,
            )
        credits = _find_first(payload, "credits") or {}
        remaining = None
        if isinstance(credits, dict):
            remaining = credits.get("balance") or credits.get("remaining")
        elif isinstance(credits, (int, float, str)):
            remaining = credits
        try:
            remaining_value = float(str(remaining).replace(",", "")) if remaining is not None else None
        except ValueError:
            remaining_value = None
        if not any(normalized.values()) and remaining_value is None:
            return None
        return UsageSnapshot(
            provider="codex",
            source="oauth",
            fetched_at=utcnow_iso(),
            identity=identity,
            windows=normalized,
            credits=Credits(remaining=remaining_value),
            raw={"source_details": {"keys": sorted(payload.keys()) if isinstance(payload, dict) else type(payload).__name__}},
        )

    def _manual_or_imported_cookie_header(self, cookie_header: str | None, cookie_header_file: str | None) -> tuple[str | None, str | None]:
        if cookie_header:
            self._debug("using manual cookie header")
            return cookie_header.strip(), "manual"
        if cookie_header_file:
            self._debug(f"using manual cookie header file: {cookie_header_file}")
            return Path(cookie_header_file).read_text().strip(), "manual-file"
        cache = CookieCache(self.cache_dir)
        cached = cache.load("codex", max_age_seconds=900)
        if cached:
            self._debug(f"using cached cookie header from {cached[1]}")
            return cached
        try:
            imported = import_cookie_header(self.browser, self.COOKIE_DOMAINS)
        except BrowserCookieError as exc:
            self._debug(str(exc))
            return None, None
        self._debug(f"imported cookie header from {imported.source}")
        cache.save("codex", imported.cookie_header, imported.source)
        return imported.cookie_header, imported.source

    def fetch_dashboard_usage(self, cookie_header: str | None = None, cookie_header_file: str | None = None, expected_email: str | None = None) -> UsageSnapshot | None:
        header, source_label = self._manual_or_imported_cookie_header(cookie_header, cookie_header_file)
        if not header:
            return None
        html_body = None
        route = None
        for url in self.DASHBOARD_URLS:
            request = self._build_request(url, cookie_header=header)
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    html_body = response.read().decode(errors="ignore")
                    route = response.geturl()
                    break
            except urllib.error.HTTPError as exc:
                self._debug(f"dashboard fetch failed for {url}: {exc.code}")
            except Exception as exc:
                self._debug(f"dashboard fetch failed for {url}: {exc}")
        if not html_body:
            return None
        text = extract_html_text(html_body)
        if detect_dashboard_login_required(route, html_body, text):
            return UsageSnapshot(
                provider="codex",
                source="dashboard",
                fetched_at=utcnow_iso(),
                identity=Identity(login_method=source_label),
                windows={"primary": None, "secondary": None, "tertiary": None},
                credits=Credits(),
                warnings=["dashboard login required"],
                raw={"route": route, "source_details": {"browser_source": source_label, "dashboard_mode": "login-required"}},
            )
        email = parse_dashboard_email(html_body)
        if expected_email and email and email.lower() != expected_email.lower():
            return UsageSnapshot(
                provider="codex",
                source="dashboard",
                fetched_at=utcnow_iso(),
                identity=Identity(email=email, login_method=source_label),
                windows={"primary": None, "secondary": None, "tertiary": None},
                credits=Credits(),
                warnings=[f"dashboard email mismatch: expected {expected_email}, got {email}"],
                raw={"route": route, "source_details": {"browser_source": source_label, "dashboard_mode": "email-mismatch"}},
            )
        windows = parse_rate_limits_from_text(text)
        credits_remaining = parse_credits_remaining(text)
        plan = parse_dashboard_plan(html_body)
        usage_breakdown = parse_usage_breakdown_from_html(html_body)
        history = parse_credit_history(html_body)
        code_review = parse_dashboard_code_review(text)
        purchase_url = parse_dashboard_purchase_url(html_body)
        code_review_window = windows.get("tertiary")
        if code_review is None and code_review_window:
            code_review = code_review_window.remaining_percent
        return UsageSnapshot(
            provider="codex",
            source="dashboard",
            fetched_at=utcnow_iso(),
            identity=Identity(email=email or expected_email, login_method=source_label or plan),
            windows=windows,
            credits=Credits(
                remaining=credits_remaining,
                purchase_url=purchase_url,
            ),
            extras={
                "code_review_remaining_percent": code_review,
                "code_review_limit": code_review_window.reset_description if code_review_window else None,
                "usage_breakdown": usage_breakdown,
                "credit_history": history,
                "account_plan": plan,
            },
            raw={
                "route": route,
                "body_sample": text[:400],
                "source_details": {
                    "browser_source": source_label,
                    "dashboard_mode": "rich" if usage_breakdown or history or purchase_url or code_review is not None else "basic",
                    "auth_status": parse_dashboard_auth_status(html_body),
                },
            },
        )

    def fetch_rpc_usage(self) -> UsageSnapshot | None:
        try:
            proc = subprocess.Popen(
                ["codex", "-s", "read-only", "-a", "untrusted", "app-server"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=False,
            )
        except OSError as exc:
            self._debug(f"rpc launch failed: {exc}")
            return None
        try:
            messages = [
                {"id": 1, "method": "initialize", "params": {"clientInfo": {"name": "provider-usage-checker", "version": "0.1.0"}}},
                {"method": "initialized", "params": {}},
                {"id": 2, "method": "account/read", "params": {}},
                {"id": 3, "method": "account/rateLimits/read", "params": {}},
            ]
            assert proc.stdin is not None
            for message in messages:
                proc.stdin.write((json.dumps(message) + "\n").encode())
            proc.stdin.flush()
            responses: dict[int, dict[str, Any]] = {}
            deadline = time.time() + self.timeout
            assert proc.stdout is not None
            assert proc.stderr is not None
            buffer = b""
            while time.time() < deadline and len(responses) < 3:
                ready, _, _ = select.select([proc.stdout, proc.stderr], [], [], 0.5)
                if not ready:
                    if proc.poll() is not None:
                        break
                    continue
                for stream in ready:
                    chunk = os.read(stream.fileno(), 4096)
                    if not chunk:
                        continue
                    if stream is proc.stderr:
                        self._debug(f"rpc stderr: {chunk.decode(errors='ignore').strip()[:300]}")
                        continue
                    buffer += chunk
                    while b"\n" in buffer:
                        line, buffer = buffer.split(b"\n", 1)
                        if not line.strip():
                            continue
                        try:
                            payload = json.loads(line.decode())
                        except json.JSONDecodeError:
                            continue
                        if "id" in payload:
                            responses[int(payload["id"])] = payload
            account = ((responses.get(2) or {}).get("result") or {}).get("account")
            limits = ((responses.get(3) or {}).get("result") or {}).get("rateLimits") or {}
            windows = {
                "primary": self._window_from_rpc(limits.get("primary"), "5h"),
                "secondary": self._window_from_rpc(limits.get("secondary"), "weekly"),
                "tertiary": None,
            }
            credits = limits.get("credits") or {}
            remaining = None
            if isinstance(credits, dict) and credits.get("balance") is not None:
                try:
                    remaining = float(str(credits["balance"]).replace(",", ""))
                except ValueError:
                    remaining = None
            email = None
            plan = None
            if isinstance(account, dict) and account.get("type", "").lower() == "chatgpt":
                email = account.get("email")
                plan = account.get("planType")
            if not any(windows.values()) and remaining is None:
                return None
            return UsageSnapshot(
                provider="codex",
                source="cli-rpc",
                fetched_at=utcnow_iso(),
                identity=Identity(email=email, login_method=plan),
                windows=windows,
                credits=Credits(remaining=remaining),
                raw={"source_details": {"account_type": account.get("type") if isinstance(account, dict) else None}},
            )
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                proc.kill()

    def _window_from_rpc(self, payload: dict[str, Any] | None, name: str) -> UsageWindow | None:
        if not payload:
            return None
        used = payload.get("usedPercent")
        if used is None:
            return None
        resets_at = payload.get("resetsAt")
        timestamp = None
        if isinstance(resets_at, (int, float)):
            timestamp = dt.datetime.fromtimestamp(float(resets_at), tz=dt.timezone.utc).isoformat()
        return UsageWindow(
            name=name,
            used_percent=float(used),
            remaining_percent=max(0.0, 100.0 - float(used)),
            resets_at=timestamp,
            reset_description=None,
        )

    def fetch_pty_usage(self) -> UsageSnapshot | None:
        master_fd, slave_fd = pty.openpty()
        try:
            proc = subprocess.Popen(
                ["codex", "-s", "read-only", "-a", "untrusted"],
                stdin=slave_fd,
                stdout=slave_fd,
                stderr=slave_fd,
                text=False,
                close_fds=True,
            )
            os.write(master_fd, b"/status\n")
            deadline = time.time() + min(self.timeout, 8.0)
            chunks: list[bytes] = []
            while time.time() < deadline:
                ready, _, _ = select.select([master_fd], [], [], 0.5)
                if not ready:
                    continue
                data = os.read(master_fd, 4096)
                if not data:
                    break
                chunks.append(data)
                if b"Weekly limit" in data or b"Credits:" in data:
                    time.sleep(0.5)
                    break
            text = strip_ansi(b"".join(chunks).decode(errors="ignore"))
            windows = parse_rate_limits_from_text(text)
            credits_remaining = parse_credits_remaining(text)
            if not any(windows.values()) and credits_remaining is None:
                return None
            warnings = []
            if "update available" in text.lower():
                warnings.append("Codex CLI reports an update prompt; /status parsing may be incomplete.")
            return UsageSnapshot(
                provider="codex",
                source="cli-pty",
                fetched_at=utcnow_iso(),
                identity=Identity(),
                windows=windows,
                credits=Credits(remaining=credits_remaining),
                warnings=warnings,
                raw={"body_sample": text[:400]},
            )
        except OSError as exc:
            self._debug(f"pty launch failed: {exc}")
            return None
        finally:
            try:
                os.close(master_fd)
            except OSError:
                pass
            try:
                os.close(slave_fd)
            except OSError:
                pass
            try:
                proc.terminate()
                proc.wait(timeout=2)
            except Exception:
                pass

    def fetch(self, source: str, cookie_header: str | None = None, cookie_header_file: str | None = None, expected_email: str | None = None) -> UsageSnapshot:
        ordered = {
            "auto": ["oauth", "dashboard", "cli-rpc", "cli-pty"],
            "oauth": ["oauth"],
            "dashboard": ["dashboard"],
            "cli-rpc": ["cli-rpc"],
            "cli-pty": ["cli-pty"],
        }[source]
        warnings: list[str] = []
        auth_identity = None
        try:
            _, auth_identity = self.load_auth()
        except Exception:
            auth_identity = None
        if source == "auto":
            oauth_snapshot = self.fetch_oauth_usage()
            dashboard_snapshot = self.fetch_dashboard_usage(
                cookie_header=cookie_header,
                cookie_header_file=cookie_header_file,
                expected_email=expected_email or (auth_identity.email if auth_identity else None),
            )
            oauth_ok = snapshot_has_usable_data(oauth_snapshot)
            dashboard_ok = snapshot_has_usable_data(dashboard_snapshot) and not any(
                warning in {"dashboard login required"} or warning.startswith("dashboard email mismatch")
                for warning in (dashboard_snapshot.warnings if dashboard_snapshot else [])
            )
            if oauth_ok and dashboard_ok:
                if compute_snapshot_richness(dashboard_snapshot) > compute_snapshot_richness(oauth_snapshot):
                    dashboard_snapshot.warnings = warnings + dashboard_snapshot.warnings
                    return dashboard_snapshot
                oauth_snapshot.warnings = warnings + oauth_snapshot.warnings + ["dashboard returned no incremental value over oauth"]
                return oauth_snapshot
            if oauth_ok:
                if dashboard_snapshot and dashboard_snapshot.warnings:
                    oauth_snapshot.warnings = warnings + oauth_snapshot.warnings + dashboard_snapshot.warnings
                return oauth_snapshot
            if dashboard_ok and dashboard_snapshot:
                dashboard_snapshot.warnings = warnings + dashboard_snapshot.warnings
                return dashboard_snapshot
            warnings.extend(dashboard_snapshot.warnings if dashboard_snapshot else [])
            ordered = ["cli-rpc", "cli-pty"]
        for candidate in ordered:
            snapshot = None
            if candidate == "oauth":
                snapshot = self.fetch_oauth_usage()
            elif candidate == "dashboard":
                snapshot = self.fetch_dashboard_usage(
                    cookie_header=cookie_header,
                    cookie_header_file=cookie_header_file,
                    expected_email=expected_email or (auth_identity.email if auth_identity else None),
                )
            elif candidate == "cli-rpc":
                snapshot = self.fetch_rpc_usage()
            elif candidate == "cli-pty":
                snapshot = self.fetch_pty_usage()
            if source == "dashboard" and snapshot and snapshot.warnings and (
                "dashboard login required" in snapshot.warnings
                or any(w.startswith("dashboard email mismatch") for w in snapshot.warnings)
            ):
                raise RuntimeError("; ".join(snapshot.warnings))
            if snapshot_has_usable_data(snapshot):
                snapshot.warnings = warnings + snapshot.warnings
                return snapshot
            warnings.append(f"{candidate} did not return usable usage data")
        raise RuntimeError("Unable to retrieve Codex usage from OAuth, dashboard, RPC, or PTY sources.")
