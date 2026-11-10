---
name: skill-creator
domain: core
description: Create or update a self-contained agent skill, design requested skill evaluations, or improve trigger precision. Use for a reusable SKILL.md workflow; for audit-only trimming use skill-cutter.
metadata:
  version: "1.0.1"
---

# Skill Creator

Turn a reusable task into instructions that change an agent's decisions. Start
from the user's examples and corrections already present in the conversation.

## Define the contract

Establish the intended task, positive trigger, nearby exclusions, output and
required environment. Ask only for information that changes the result and cannot
be inferred. A narrow edit does not need a new interview or an evaluation project.

Use the user-specified repository/location and its conventions. Keep one canonical
copy there; installation into agent-specific folders is a separate requested task.
Do not save to unrelated personal paths or synchronize consumers automatically.

## Write the skill

Start `SKILL.md` on line 1 with YAML frontmatter containing `name` and a specific
`description`. Preserve supported metadata and any repository version contract.
Use lowercase kebab-case for new skill directories; preserve existing identities
when updating unless a rename is part of the task.

The description is the discovery contract: name concrete intent and artifacts,
not every adjacent product noun. Keep trigger rules in metadata and align any
`agents/openai.yaml` text with them. Do not make triggers pushy to inflate usage.

Keep the body focused on non-obvious constraints, fragile sequences, tool/file
contracts and failure modes. Explain why a constraint matters when that changes
execution. Generic tutorials, duplicated system policy and fixed review rituals
add context without improving decisions. Distinguish required steps from advice.

Use resources only for a concrete purpose:

- `scripts/`: deterministic or repeatedly needed operations; test changed code.
- `references/`: conditional detail linked with when to load it.
- `assets/`: files copied into the output, rather than instructions to preload.

Do not create placeholder folders or duplicate a long manual under references
simply to shorten the entrypoint. Inspect callers before removing existing files.

## Evaluate when it helps the requested change

For objective behavior, choose a few representative requests and near-misses.
Check observable outputs and important invariants, not matching prose. Small
wording fixes may need only a diff and metadata/path validation. Expensive model
runs, independent agents and interactive feedback are optional workflows, not
prerequisites to every skill edit; use them only within available authorization.

For a requested benchmark or evaluation workflow, retain these bundled contracts:

- Read [references/schemas.md](references/schemas.md) before writing eval,
  grading or benchmark JSON. `evals/evals.json` identifies the skill and prompts.
- Place generated results in a sibling workspace, separated by iteration, case
  and configuration. Preserve the old skill for a baseline when comparing edits.
- Use the same inputs and comparable settings across configurations; record
  measured timing/tokens rather than inventing values.
- Read `agents/grader.md`, `agents/analyzer.md` or `agents/comparator.md` only for
  the corresponding analysis. Report failures and uncertainty, not just averages.
- `scripts/aggregate_benchmark.py` summarizes compatible results. Use
  `eval-viewer/generate_review.py --help` for the review UI or static export when
  the user requests reviewing benchmark artifacts. Do not require browser review
  for an ordinary edit or infer satisfaction from missing feedback.
- Description-optimization helpers invoke external model/CLI runs. Inspect their
  help and costs first; test realistic positive and nearby negative requests, and
  separate tuning from held-out evaluation.

## Deliver and stop

Validate frontmatter, trigger/UI alignment, relative links and changed helpers.
Use `scripts/quick_validate.py` as a structural check where compatible with the
host; also run the repository validator. Neither proves behavioral quality.
Package with `scripts/package_skill.py` only when an installable bundle is wanted.

Report what changed, why, relevant validation and unresolved limitations. Stop
when the requested skill or evaluation is complete; further benchmark rounds,
viewer feedback and installation are follow-up work unless requested.
