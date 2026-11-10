---
name: github-repo-management
domain: platforms
description: Clone, create, fork or configure a specific GitHub repository, release, workflow or secret when requested. Use for repository administration; read-only inspection does not authorize visibility changes, publication or unrelated global configuration.
author: Hermes Agent
license: MIT
metadata:
  version: "1.1.1"
  hermes:
    tags:
    - GitHub
    - Repositories
    - Git
    - Releases
    - Secrets
    - Configuration
    related_skills:
    - github-auth
    - github-pr-workflow
    - github-issues
---

# GitHub Repository Management

Establish the host/owner/repository and exact requested operation. Prefer working
connected tools or authenticated gh; use git/REST with protected credentials when
needed. Do not scrape credential files or assume local authentication is missing
because another client is not configured.

For clone/fork work, use the requested non-overwriting destination, preserve existing
remotes and discover the real default branch. A shallow clone may omit history
needed by review/migration work. Verify the created fork/repo identity and readiness
rather than relying on a fixed sleep.

For repository creation, make visibility intentional. Honor a specified choice;
if none exists, a private repository is a safe reversible starting point rather than a
public upload. Creation does not imply pushing the whole working directory. Stage
and publish only intended content, preserving unrelated files/history.

Read current settings/protection rules before modifying them. Send only requested
fields and retain unrelated rules; do not replace branch protection from a generic
example. Workflow dispatch can deploy or modify external systems, so bind its ref,
inputs and environment to the requested action. Listing runs does not authorize reruns.

For secrets, use a protected input mechanism and inspect target scope/name without
printing values or putting them in command arguments. REST secret writes require
the provider's current public-key/encryption contract; verify a change by metadata
or intended use, not attempting to read the secret back.

For releases, bind tag/target revision and exact fresh assets. Draft preparation,
publication and changing an existing immutable release are distinct operations.
For gists, distinguish public exposure from an unlisted link; unlisted is not a
private access-control guarantee. Confirm actual returned status/URLs per operation.

Read [github-api-cheatsheet.md](references/github-api-cheatsheet.md) only for a
relevant API, verifying current schema/permissions before use. Handle pagination,
HTTP errors and partial failure without blind duplicate mutations. Stop at the
requested repository outcome; no generic settings, release or workflow rollout.
