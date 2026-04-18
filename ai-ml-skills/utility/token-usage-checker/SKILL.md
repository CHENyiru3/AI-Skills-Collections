---
name: token-usage-checker
description: Check token/credit usage for MiniMax, Cursor Pro, and Codex CLI accounts. Delegates to provider-usage-checker for Codex and Cursor.
version: 1.4.0
category: utility
---

# Token Usage Checker

## MiniMax

Always unlock Bitwarden first, then retrieve credentials before logging in.

```bash
# 1. Unlock Bitwarden
export BW_SESSION=$(bw unlock --passwordenv BITWARDEN_PASSWORD --raw)

# 2. Get credentials
bw get username "Minimax"
bw get password "Minimax"

# 3. Navigate to MiniMax
browser_navigate "https://platform.minimaxi.com/user-center/payment/token-plan"
# Login via browser if redirected to /login
# Read: plan name, 可用额度, 截止日期, sk-cp- API key
```

## Cursor Pro

```bash
python3 /Users/eric_yiru/Desktop/Github/ai_skills/ai-ml-skills/utility/provider-usage-checker/scripts/check_usage.py --provider cursor
python3 /Users/eric_yiru/Desktop/Github/ai_skills/ai-ml-skills/utility/provider-usage-checker/scripts/check_usage.py --provider cursor --json
```

Uses Firefox cookies + Playwright WebKit to bypass Cloudflare. Source order: cached cookie → Firefox → manual cookie → Cursor APIs.

## Codex

```bash
python3 /Users/eric_yiru/Desktop/Github/ai_skills/ai-ml-skills/utility/provider-usage-checker/scripts/check_usage.py --provider codex
python3 /Users/eric_yiru/Desktop/Github/ai_skills/ai-ml-skills/utility/provider-usage-checker/scripts/check_usage.py --provider codex --source dashboard --json --debug
```

Source order: `~/.codex/auth.json` → authenticated dashboard → `codex app-server` RPC → `/status` PTY fallback.

## Quick Ref

| Service | Command | Headless |
|---------|---------|----------|
| MiniMax | browser_navigate + Bitwarden | ✅ |
| Cursor | provider-usage-checker | ✅ |
| Codex | provider-usage-checker | ✅ |
