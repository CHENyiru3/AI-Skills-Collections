---
name: building-python-communities
domain: programming
description: Create or revise Python project contribution, governance, issue/PR templates or maintainer workflows. Use for explicit contributor-experience work; not ordinary code fixes or automatic GitHub messaging.
metadata:
  version: "1.0.1"
---

# Python Project Community

Inspect existing contribution files, license, maintainer roles and repository
conventions. Deliver the requested documents or configuration without replacing
established governance, commit styles or response expectations by default.

For contribution instructions, verify setup and check commands against the actual
project. Do not promise a nonexistent dev extra, Make target or pre-commit hook.
Use issue templates that request enough information to reproduce the problem
without collecting credentials or unnecessary personal data. Tailor PR prompts to
changes that actually require tests, docs or migration notes.

Read [TEMPLATES.md](TEMPLATES.md) for a needed template and
[GOVERNANCE.md](GOVERNANCE.md) for an ownership/decision model. Present optional
choices as choices; adding a code of conduct requires real contact/enforcement
arrangements, not an invented email address or maintainer commitment.

GitHub automation is conditional on a request for it. Confirm current action inputs
and token permissions from the action's primary documentation. Avoid executing
untrusted PR code with privileged `pull_request_target` credentials. Drafted welcome
text does not authorize sending messages, changing labels or publishing policy.

Check local links and real development commands. Stop after the scoped contributor
artifacts are complete; fixed response SLAs, recurring triage and a full governance
stack are follow-up decisions, not prerequisites.
