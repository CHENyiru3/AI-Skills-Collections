---
name: token-usage-checker
description: Check token/credit usage for MiniMax, Cursor Pro, and Codex CLI accounts
version: 1.3.0
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
python ~/.hermes/skills/cursor-usage-checker/check_usage.py
```

## Codex

```bash
codex
# /status
# Interactive only — no headless command available
```

## Quick Ref

| Service | Command | Headless |
|---------|---------|----------|
| MiniMax | browser_navigate URL above | ✅ |
| Cursor | python script | ✅ |
| Codex | codex → /status | ❌ |
