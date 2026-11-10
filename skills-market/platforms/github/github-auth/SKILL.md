---
name: github-auth
domain: platforms
description: Set up or troubleshoot GitHub authentication when the requested operation lacks suitable access. Reuse working connectors/credentials; ordinary GitHub reads and local diffs do not require reauthentication or global Git changes.
author: Hermes Agent
license: MIT
metadata:
  version: "1.1.1"
  hermes:
    tags:
    - GitHub
    - Authentication
    - Git
    - gh-cli
    - SSH
    - Setup
    related_skills:
    - github-pr-workflow
    - github-code-review
    - github-issues
    - github-repo-management
---

# GitHub Authentication

Identify the required operation, GitHub host/repository and existing access path.
A connected GitHub tool may already work even if the local gh/git client is not
configured. Separate identity, authentication, repository permission and network
failure; a DNS error is not evidence that a token needs replacement.

Prefer an existing credential manager, host connector or authenticated gh session.
Use `gh auth status` or a scoped read when needed without displaying token material.
The optional `scripts/gh-env.sh` uses gh auth status and local repository/env hints;
it does not scrape credential files, print secrets, set global Git configuration
or resolve a username. gh may contact the host to verify authentication. Inspect a shell script before sourcing it.

For a requested new login, use the provider's supported browser/device flow or a
least-required token/account scope. Do not default to a broad classic repo/workflow
credential when a narrower method covers the task. Keep secrets out of chat, URLs,
process arguments, logs and committed files; use a protected input/store mechanism.
Do not enable plaintext credential-store as the convenient default.

For SSH, reuse a suitable existing key/agent. Never overwrite a key path, expose a
private key or generate an unencrypted key by default. Follow the chosen provider's
public-key registration and host verification procedure. Limit configuration to the
requested host/repository rather than rewriting all HTTPS URLs globally.

Git author identity is separate from access. Set repository-local identity only
when a requested commit needs it and the value is known; do not invent an email or
change global identity. `git ls-remote` proves read access only, not push permission.
Validate the specific access needed without creating a test commit/publication.

Stop when the requested operation has suitable access, or report the exact missing
credential/permission. Reference: [gh auth login](https://cli.github.com/manual/gh_auth_login).
