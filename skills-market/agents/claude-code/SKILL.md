---
name: claude-code
domain: agents
description: Delegate an explicitly requested task to Claude Code CLI, monitor it and review the result. Use for another Claude run or CLI automation; not for ordinary coding within the current agent.
author: Hermes Agent + Teknium
license: MIT
metadata:
  version: "2.2.1"
  hermes:
    tags:
    - Coding-Agent
    - Claude
    - Anthropic
    - Code-Review
    - Refactoring
    - PTY
    - Automation
    related_skills:
    - codex
---

# Claude Code Delegation

Establish the task, selected workspace, allowed changes and expected output.
Discover the installed `claude --help` contract and reuse existing authentication.
Do not install, update or rewrite global settings just to run an already configured
client. Use the host's available process tools rather than assuming Hermes or tmux.

## Choose the interaction

For a bounded task, print mode returns a result and exits:

```bash
claude -p "Review the relevant code and report findings" --tools "Read,Grep,Glob" --permission-mode dontAsk
```

Confirm flags with installed help. `--tools` selects built-in tools;
`--allowedTools` pre-approves matching tool calls and is not a capability whitelist.
Check separately configured MCP tools, hooks and permissions when restricting a
run. `dontAsk` denies operations that would require approval; it does not make the
whole environment read-only. For authorized edits choose the required capabilities,
without defaulting to permission bypass.

Print mode does not require a PTY. For a genuine multi-turn TUI session, use an
available PTY/session controller; tmux is one option, not a universal prerequisite.
Do not automatically accept workspace trust or bypass warnings. Verify the folder
and the scope that the user has actually authorized.

## Bound execution and inspect results

Project hooks and MCP configuration can run even in a print-mode invocation.
For unfamiliar repositories, inspect relevant configuration or use a supported
isolated/bare setup. Bare mode changes loaded context and authentication; check
its documented behavior instead of assuming it preserves the user's OAuth setup.

Run in an explicit working directory. Set turn/budget limits when appropriate;
a limit reached is a partial run, not proof of task completion. Keep the process
handle and actual session ID for monitoring or resumption. Interpret structured
output using the installed version's schema, including error and limit statuses.

For independent tasks use separate worktrees only when delegation is authorized.
Record the base/head for a review and avoid disturbing the user's checkout.
Inspect generated diffs and relevant tests before accepting a coding result.
Report what completed, failed or remains uncertain. A delegated review does not
authorize posting to GitHub; coding does not automatically authorize commit, push
or deployment. Stop at the requested result and clean up only sessions/workspaces
created for this task.

Reference: [programmatic use](https://code.claude.com/docs/en/headless).
