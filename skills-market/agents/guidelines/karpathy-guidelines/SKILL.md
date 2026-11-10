---
name: karpathy-guidelines
domain: agents
description: Apply Karpathy-style simplicity and surgical changes when explicitly requested, or review code for overengineering and hidden assumptions. Not a mandatory workflow for every routine code edit.
license: MIT
metadata:
  version: "1.0.1"
---

# Karpathy Guidelines

Use the smallest change that solves the stated problem. Preserve existing style,
interfaces and unrelated work; remove only code made unused by the requested change.
Avoid speculative abstractions, configurability and features without a concrete use.

State assumptions that materially affect correctness or scope. Resolve routine,
reversible choices from context; ask only when a consequential ambiguity cannot
be settled. Continue independent work while a needed answer is pending.

Define observable success and choose verification that can change confidence in
that outcome. A regression test is useful for a reproducible bug; trivial wording
or formatting changes need proportionate inspection rather than a mandatory new
test. Stop once the requested behavior and relevant checks pass.

For reviews, identify concrete complexity, scope creep or unsupported assumptions
and explain their effect. Do not demand a rewrite merely to hit a line-count target.

Attribution: derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876).
