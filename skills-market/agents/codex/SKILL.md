---
name: codex
domain: agents
description: Delegate an explicitly requested task to the Codex CLI and inspect its result. Use when the user wants another Codex run or CLI automation; not for ordinary coding already handled by the current agent.
author: Hermes Agent
license: MIT
metadata:
  version: "1.0.1"
  hermes:
    tags:
    - Coding-Agent
    - Codex
    - OpenAI
    - Code-Review
    - Refactoring
    related_skills:
    - claude-code
---

# Codex CLI Delegation

Identify the delegated outcome, workspace, allowed mutations and result artifact.
Use the available process/terminal API; do not assume a particular host's tool names.
Check `codex --help` and `codex exec --help` for the installed version before
constructing flags. Reuse configured authentication without printing credentials.

For a bounded non-interactive run:

```bash
codex exec --sandbox read-only "Review the relevant changes and report findings"
```

Run in the selected working directory. Select a sandbox compatible with the task;
use workspace writes only for an authorized editing task. `exec` is non-interactive
and does not universally need a PTY. Use a PTY for an interactive session when the
actual terminal interface requires one.

Codex normally checks for a trusted Git repository. Where appropriate for a known
scratch folder, the installed CLI may provide `--skip-git-repo-check`; confirm it
in help rather than creating a repository merely to satisfy a stale assumption.
Do not default to disabling sandboxing or bypassing approval controls.

For long runs, keep the process/session handle, inspect progress and final exit
status, and verify the requested output. Do not blindly answer trust or permission
prompts. Surface a real authorization gap with the exact action it concerns.

If independent work is requested, use separate worktrees/checkouts so runs cannot
edit the same files. Record the base and target revisions. For reviews, prefer an
isolated checkout and keep the review read-only unless fixes were requested.

Inspect the resulting diff and relevant checks before accepting an editing run.
Report failures and partial results accurately. Commits, pushes, PR creation and
posting reviews require that scope in the user's request; delegation alone does
not authorize them. Stop after the delegated outcome is verified and clean up only
scratch resources created for that run.
