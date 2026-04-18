---
name: provider-usage-checker
description: Use when the user explicitly asks to check Codex or Cursor usage, credits, quota, or billing. Reuses local auth, CLI state, and browser session cookies before falling back to manual cookie headers.
version: 0.1.0
category: utility
---

# Provider Usage Checker

Use this skill only for explicit usage-accounting requests.

## Supported providers

- `codex`
- `cursor`

## Source order

### Codex

1. OAuth/backend usage from `~/.codex/auth.json`
2. Authenticated dashboard fetch using local browser cookies or a manual cookie header for richer details
3. Local Codex CLI RPC via `codex app-server`
4. Local Codex CLI `/status` PTY fallback

### Cursor

1. Cached cookie header
2. Imported browser cookies
3. Manual cookie header
4. Cursor web APIs

## Usage

```bash
python3 check_usage.py --provider codex
python3 check_usage.py --provider codex --json
python3 check_usage.py --provider codex --source dashboard --json --debug
python3 check_usage.py --provider cursor
python3 check_usage.py --provider cursor --cookie-header-file /path/to/cookie.txt
```

## Notes

- Default browser import currently targets Firefox session cookies, because they can be read locally without extra dependencies.
- Manual cookie headers are supported for both providers.
- For Codex, `--source dashboard` is the path that can add reset timestamps, code review, usage breakdown, credits history, and purchase URL when the dashboard is authenticated.
- The checker never prints raw cookie or bearer token values.
