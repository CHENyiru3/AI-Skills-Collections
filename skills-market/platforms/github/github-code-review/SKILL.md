---
name: github-code-review
domain: platforms
description: Review a local diff or GitHub PR for concrete correctness and risk findings. Use for an explicit code review; report locally unless posting comments or a formal review was requested.
author: Hermes Agent
license: MIT
metadata:
  version: "1.1.1"
  hermes:
    tags:
    - GitHub
    - Code-Review
    - Pull-Requests
    - Git
    - Quality
    related_skills:
    - github-auth
    - github-pr-workflow
---

# Code Review

Identify the review target: staged/working changes or an exact PR base/head revision.
Inspect the diff and surrounding code/data contracts before judging it. Local diffs
need no GitHub authentication. For a PR, use available connected tools/gh and
configured access rather than unrelated absolute auth helpers or credential scraping.

Discover the actual base branch and compare the intended revisions; do not assume
`main`. Preserve the user's dirty checkout. If execution or a full checkout helps,
use an isolated worktree/clone and assess unfamiliar code/hooks before running it.
Do not switch or force-delete the user's branches as a cleanup default.

Prioritize reproducible defects and material risks introduced by the change. Explain
the trigger, consequence and precise location; distinguish a confirmed issue from
a question, pre-existing problem or optional style preference. Check only relevant
correctness, security, compatibility, tests and performance implications rather than
turning a generic checklist into mandatory redesign.

A scope-appropriate test can establish a concern, but test execution is not required
for a read-only static finding, and absence of findings is allowed. Report checks
that did/did not run. Use [review-output-template.md](references/review-output-template.md)
when helpful, without inventing critical findings or requiring every rating section.

## If posting was requested

Bind inline comments to the reviewed head commit, actual diff path and correct
LEFT/RIGHT side/line. Recheck a changed head before submitting; do not reuse stale
line numbers. Choose COMMENT/REQUEST_CHANGES/APPROVE based on supported findings
and the requested review scope. Submit one coherent review rather than duplicate
formal/summary messages. Check the returned URL/status and stop after the review;
merging, fixing code and publishing are separate actions unless included.
