---
name: github-issues
domain: platforms
description: Create, manage, triage, and close GitHub issues. Search existing issues, add labels, assign people, and link to PRs. Works with gh CLI or falls back to git + GitHub REST API via curl.
author: Hermes Agent
license: MIT
metadata:
  version: "1.1.1"
  hermes:
    tags:
    - GitHub
    - Issues
    - Project-Management
    - Bug-Tracking
    - Triage
    related_skills:
    - github-auth
    - github-pr-workflow
---

# GitHub Issues

Establish the host, owner/repository, issue identity and requested read/write scope.
Prefer an existing connected tool or authenticated gh; use the REST API only with
configured protected credentials. A local clone/auth setup is not needed for every
issue query, and credential files must not be scraped to make a fallback work.

Search before creating a potentially duplicate issue. Read its current state and
relevant labels/assignees before edits. Use the repository's actual template;
`templates/bug-report.md` and `templates/feature-request.md` are optional aids.
Describe observed behavior, reproduction and impact without inventing environment
facts or committing other people to work.

For listing/search, handle pagination and incomplete/search-limited responses.
REST issues endpoints can return PRs: exclude records containing `pull_request`,
and use `is:issue` in search when issue-only results are intended. Never feed an
unfiltered issues API response into a bulk-close loop.

For requested bulk changes, build the exact eligible issue-number set, recheck
current state as needed, then apply only those changes. Use structured JSON or a
body file for multiline text; URL-encode identifiers/labels correctly. Check HTTP
status and actual returned state per item, record partial failures and retry only
failed operations after resolving their cause. Do not print success for a failed
request or duplicate comments on blind retries.

Posting comments, assignment, label changes and closing require that scope in the
request; triage can be a read-only report. Closing keywords in a PR can have future
merge effects, so include them intentionally. Stop at the requested issue outcome.
Reference: [GitHub issues API](https://docs.github.com/en/rest/issues/issues).
