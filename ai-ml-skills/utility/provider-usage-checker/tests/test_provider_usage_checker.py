from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.providers.codex import (
    Credits,
    Identity,
    UsageSnapshot,
    UsageWindow,
    compute_snapshot_richness,
    detect_dashboard_login_required,
    extract_html_text,
    parse_credit_history,
    parse_credits_remaining,
    parse_dashboard_auth_status,
    parse_dashboard_code_review,
    parse_dashboard_email,
    parse_dashboard_plan,
    parse_dashboard_purchase_url,
    parse_rate_limits_from_text,
)
from scripts.providers.cursor import CursorFetcher


FIXTURES = Path(__file__).parent / "fixtures"


class CodexParsingTests(unittest.TestCase):
    def test_parse_rate_limits_from_status_text(self) -> None:
        text = (FIXTURES / "codex_status.txt").read_text()
        windows = parse_rate_limits_from_text(text)
        self.assertEqual(windows["primary"].remaining_percent, 78.0)
        self.assertEqual(windows["secondary"].remaining_percent, 61.0)
        self.assertEqual(windows["tertiary"].remaining_percent, 70.0)

    def test_parse_dashboard_identity_and_plan(self) -> None:
        html = (FIXTURES / "codex_dashboard.html").read_text()
        self.assertEqual(parse_dashboard_email(html), "coder@example.com")
        self.assertEqual(parse_dashboard_plan(html), "pro")
        self.assertEqual(parse_dashboard_auth_status(html), "logged_in")

    def test_parse_dashboard_credits_and_history(self) -> None:
        html = (FIXTURES / "codex_dashboard.html").read_text()
        text = extract_html_text(html)
        self.assertEqual(parse_credits_remaining(text), 18.5)
        history = parse_credit_history(html)
        self.assertEqual(history[0]["service"], "CLI")
        self.assertEqual(parse_dashboard_code_review(text), 70.0)

    def test_detect_dashboard_login_required(self) -> None:
        html = (FIXTURES / "codex_dashboard_login.html").read_text()
        text = extract_html_text(html)
        self.assertTrue(detect_dashboard_login_required("https://chatgpt.com/auth/login", html, text))

    def test_parse_purchase_url(self) -> None:
        html = (FIXTURES / "codex_dashboard.html").read_text() + '<a href="/billing/credits">Buy credits</a>'
        self.assertEqual(parse_dashboard_purchase_url(html), "https://chatgpt.com/billing/credits")

    def test_dashboard_richness_outranks_oauth(self) -> None:
        oauth = UsageSnapshot(
            provider="codex",
            source="oauth",
            fetched_at="2026-01-01T00:00:00+00:00",
            identity=Identity(email="coder@example.com", login_method="plus"),
            windows={
                "primary": UsageWindow(name="5h", used_percent=33.0, remaining_percent=67.0),
                "secondary": UsageWindow(name="weekly", used_percent=47.0, remaining_percent=53.0),
                "tertiary": None,
            },
            credits=Credits(remaining=0.0),
        )
        dashboard = UsageSnapshot(
            provider="codex",
            source="dashboard",
            fetched_at="2026-01-01T00:00:00+00:00",
            identity=Identity(email="coder@example.com", login_method="firefox:test"),
            windows={
                "primary": UsageWindow(name="5h", used_percent=33.0, remaining_percent=67.0, resets_at="2026-01-01T10:00:00+00:00", reset_description="10:00"),
                "secondary": UsageWindow(name="weekly", used_percent=47.0, remaining_percent=53.0, resets_at="2026-01-07T10:00:00+00:00", reset_description="10:00 on 7 Jan"),
                "tertiary": UsageWindow(name="code_review", used_percent=30.0, remaining_percent=70.0),
            },
            credits=Credits(remaining=0.0, purchase_url="https://chatgpt.com/billing/credits"),
            extras={"code_review_remaining_percent": 70.0, "credit_history": [{"service": "CLI"}]},
        )
        self.assertGreater(compute_snapshot_richness(dashboard), compute_snapshot_richness(oauth))


class CursorNormalizationTests(unittest.TestCase):
    def test_cursor_window_normalization(self) -> None:
        fetcher = CursorFetcher()
        payload = json.loads((FIXTURES / "cursor_usage_summary.json").read_text())
        plan = payload["individualUsage"]["plan"]
        window = fetcher._window("included_plan", plan["used"], plan["limit"], payload["billingCycleEnd"])
        self.assertEqual(window.used_percent, 60.0)
        self.assertEqual(window.remaining_percent, 40.0)


if __name__ == "__main__":
    unittest.main()
