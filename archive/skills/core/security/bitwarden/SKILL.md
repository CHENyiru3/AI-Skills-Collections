---
name: bitwarden
domain: core
description: Use Bitwarden CLI (bw) for headless secret retrieval. Install via npm, authenticate silently with --passwordenv, read vault items without interactive prompts.
version: 1.1.0
category: productivity
---

# Bitwarden CLI Skill

Headless Bitwarden CLI usage — no tmux, no interactive prompts needed.

## Install

```bash
npm install -g @bitwarden/cli
# or: brew install bitwarden-cli
```

Verify:
```bash
bw --version
```

## Headless Login / Unlock

Use `--passwordenv` to pass the master password as an environment variable.

```bash
# Login (if not already logged in)
bw login email@example.com --passwordenv BITWARDEN_PASSWORD

# Check status
bw status

# Unlock vault
export BW_SESSION=$(bw unlock --passwordenv BITWARDEN_PASSWORD --raw)
```

## Read Secrets

```bash
bw get password "Item Name"
bw get username "Item Name"
bw get item "Item Name"
bw list items --search "query"
```

## Security Notes

- Never echo secrets in output visible to users
- BW_SESSION expires on lock/logout
- Re-unlock with `bw unlock --passwordenv BITWARDEN_PASSWORD --raw` if locked
