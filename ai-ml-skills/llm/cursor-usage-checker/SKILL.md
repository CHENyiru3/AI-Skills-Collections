---
name: cursor-usage-checker
description: Checks Cursor Pro billing usage by scraping the billing page via Firefox cookies + Playwright WebKit (bypasses Cloudflare). Extracts API tokens, Auto+Composer usage, and spending data. Trigger when user asks to check cursor usage, billing, or token consumption.
category: ai-ml-skills/llm
---

# Cursor Usage Checker

Scrapes cursor.com/dashboard/billing using Firefox session cookies + Playwright WebKit to bypass Cloudflare bot protection.

## Requirements

- **Python 3.11+** via uv: `/Users/eric_yiru/.local/share/uv/python/cpython-3.11.14-macos-aarch64-none/bin/python3.11`
- **Playwright with WebKit**: `uv python -m playwright install webkit`
- **Firefox** with an active Cursor session (must be logged in)
- Cookies sourced from `ftyiboxw.default-release` Firefox profile

## Key Technical Findings

| Browser | Cloudflare Result |
|---------|-----------------|
| Chromium (headless) | ❌ Blocked |
| Chrome/Chrome-for-Testing | ❌ Blocked |
| Arc (Chromium-based) | ❌ Blocked |
| **WebKit (Playwright)** | ✅ **Works** |

- Firefox cookies DB can be read while Firefox is running (WAL mode)
- `api.cursor.com` exists but all usage endpoints require Enterprise API key — not accessible to Pro users
- nodriver couldn't connect to any browser (CDP sandbox issue in this env)

## Usage

```bash
~/.local/share/uv/python/cpython-3.11.14-macos-aarch64-none/bin/python3.11 \
  check_usage.py
```

Or import as module:

```python
import asyncio, subprocess
uv = '/Users/eric_yiru/.local/share/uv/python/cpython-3.11.14-macos-aarch64-none/bin/python3.11'
result = subprocess.run([uv, 'check_usage.py'], capture_output=True, text=True)
print(result.stdout)
```

## What it extracts

- Current billing cycle dates
- API token usage (total + per-model breakdown)
- Auto + Composer token usage
- On-demand usage and costs
- Invoice history
- Plan renewal date

## Privacy Note

The script copies Firefox's cookies.sqlite to `/tmp/` before reading — it never exfiltrates data. Review the script before running.
