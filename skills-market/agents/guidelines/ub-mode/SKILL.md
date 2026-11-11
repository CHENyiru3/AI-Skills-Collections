---
name: ub-mode
description: Apply the reduced engineering principles when the user explicitly invokes ub-mode or requests them. Use for that chosen coding workflow; not as a mandatory process for every code edit.
metadata:
  version: "1.0.0"
---

# Reduced Engineering Principles

## First make it work

- Make the smallest coherent change that solves the problem. Keep each decision
  in one place and subtract complexity before adding abstractions.
- Start with the data shape and domain constraints. Validate at boundaries;
  represent invalid states explicitly rather than hiding them behind guards.
- When a behavioral test is practical, reproduce the failure before the fix.
  Do not write an implementation-mirroring test merely to satisfy a ritual.
- Reconsider a shared premise after repeated fixes fail for the same reason.
  Explain the faulty assumption and change the design when necessary.
- Separate state that need not be shared. When shared mutation is required,
  make ownership explicit; design retryable operations to be idempotent.

## Then make it right

Fix the cause, work in verifiable increments, and check observable behavior.
Pin the behavior before a structural refactor and verify it afterward. Use
classes for coherent state and functions for stateless transformations when
that improves the actual design.

Complexity, duplication, and mutation tools can help when available and relevant.
Use the project's chosen tools and thresholds; do not install a tool, impose a
universal score, or run expensive mutation analysis for every reversible edit.

## Follow practice

Keep concise reasons and relevant checks in the project's existing record.
Avoid a transcript of every action or a new mandatory logging system. Use
focused context and independent workspaces when the task benefits from them.
Reclaim worktrees only within requested cleanup scope after checking ownership
and active use; uncommitted work requires resolution.

Follow the user's Git workflow. Make small reviewable commits when committing
is requested; this skill alone does not authorize pushing to a remote or main.

These principles are adapted from the installed reduced mode, which credits
[@poteto's rules](https://github.com/poteto) and the optional
[Crapper](https://github.com/unclebob/crapper),
[Dryer](https://github.com/unclebob/dryer), and
[Mutator](https://github.com/unclebob/mutator) tools. Their availability is not a
prerequisite for using the principles.
