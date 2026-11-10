---
name: github-pr-workflow
domain: platforms
description: Prepare or manage a GitHub PR, its requested CI repairs, or an authorized merge. Use for the specified PR lifecycle steps; editing alone does not imply commit/push/merge and a review does not imply posting.
author: Hermes Agent
license: MIT
metadata:
  version: "1.1.1"
  hermes:
    tags:
    - GitHub
    - Pull-Requests
    - CI/CD
    - Git
    - Automation
    - Merge
    related_skills:
    - github-auth
    - github-code-review
---

# Pull Request Workflow

Identify the host/repository, intended base/head, local work and authorized lifecycle
steps. Reuse connected tools/gh and protected credentials. Discover the default/base
branch rather than assuming main, and keep unrelated work outside the task's diff.

Create a branch/worktree when useful; do not pull/switch through a dirty checkout
by default. Stage exact intended files after reviewing the diff, using the project's
commit style. Avoid `git add .`/`-A` recipes that capture unrelated changes.

For a requested PR, prepare concrete changes and relevant validation, then create
it against the correct base/head. Use structured body arguments or a temporary
`--body-file` for multiline text, with accurate checks and intentional issue-closing
keywords. Keep draft status when the work is not ready; do not invent passed tests.

For CI, bind statuses, check-runs and logs to the actual PR head SHA. A combined
commit status alone may omit required checks. Distinguish pending, skipped, canceled,
failed and unavailable evidence. Diagnose failures before editing, retry only
supported fixes within scope, and stop expanding when the blocker requires external
state/user information. Repeatedly pushing speculative fixes is not verification.

## Authorized merge

Re-read the PR's current head, required checks/review state and merge method. Bind
the operation to the reviewed/tested head, for example the installed gh option
`--match-head-commit` or the REST merge request's expected `sha`. If the head changes,
refresh the relevant evidence rather than merging a different revision silently.
Respect repository protections/merge queues; do not bypass them because CI is slow.

Inspect actual merge/auto-merge/queue state after the request; queued is not merged.
Delete only a task-owned branch when that cleanup is included and its result is
safe. Report the PR URL, revision, relevant CI and actual merge status.

Use [ci-troubleshooting.md](references/ci-troubleshooting.md) only for a relevant
CI failure; [conventional-commits.md](references/conventional-commits.md) and the
`templates/` bodies are optional when the repository uses them. Stop at the requested
lifecycle outcome. Reference: [gh pr merge](https://cli.github.com/manual/gh_pr_merge).
