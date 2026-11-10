---
name: skill-cutter
description: Critically audit or explicitly trim an existing agent skill to its behavioral core, including narrowing over-broad trigger metadata. Use when the user asks to cut, simplify, shorten, de-slop, or reduce the context cost or trigger aggressiveness of a SKILL.md or skill folder. Do not trigger merely because a skill is long or is being edited for another purpose.
metadata:
  version: "1.0.1"
---

# Skill Cutter

Reduce context cost and accidental activation while preserving the decisions that
make the skill useful. Length is evidence, not a target.

## Establish scope

- Audit requests authorize inspection and findings. Do not edit the target.
- An explicit request to implement findings, cut, trim or simplify authorizes
  local edits to the named skill scope, not publication or consumer installation.
- Read the complete `SKILL.md`, available UI metadata and directly relevant
  resources. Preserve unrelated work and identify the user's requested outcome.

## Classify before editing

Keep non-obvious domain constraints, fragile required sequences, exact file/tool
contracts and action-specific authorization or data-integrity controls.

| Material | Treatment |
| --- | --- |
| Useful optional expert advice | Condense and mark non-blocking. |
| Generic knowledge or repeated policy | Delete. |
| Duplicate example or instruction | Keep the clearest useful instance. |
| Incident/project-specific rule in a generic skill | Move to its actual scope or delete. |
| Stale or unsupported claim | Verify with primary documentation, qualify or delete. |
| Useful detail for one variant | Link a selectively loaded reference. |

Do not move bulk merely to reduce the entrypoint's line count. Inspect callers
before deleting scripts, assets or references; apparent non-use is insufficient.

## Keep acceptance proportional

Blocking criteria come from the user outcome, higher-level invariants and risks
created by the action. Distinguish:

- **Invariant:** explicit and narrow, such as preserving sample identity.
- **Action-required:** applies only to the named task, such as a file contract.
- **Risk-triggered gate:** names the risk and proportional proof.
- **Recommendation/opportunity:** advice or follow-up, not a prerequisite.

Flag unrelated coordination, optional infrastructure presented as mandatory,
repeated approval despite established authorization, self-approval by a broken
subsystem, and proof gathering that cannot change acceptance. More than one or
two skill-added gates for a bounded task needs a concrete correctness, privacy,
security, data-integrity or irreversible-action reason.

## Narrow discovery and execution

Describe concrete user intents and artifacts in frontmatter. Remove broad
product-name triggers and catchalls; add nearby-task exclusions where useful.
Keep explicit requests discoverable. Align UI descriptions and the default
prompt; an audit-oriented prompt must not silently request edits.

Prefer deletion to dense compression. Remove copied manuals, speculative catalogs,
novice tutorials, repeated completion language, historical justification and
subjective preferences promoted to universal rules. Preserve readable constraints
and conditional routing that change execution. Separate provider requirements
from local conventions and non-blocking recommendations.

## Validate and stop

For an edit, check changed links and UI metadata, run the applicable skill
validator, inspect the diff and smoke-test changed helpers. Scale verification
to changed behavior; do not require unrelated tests or repeated polishing.

Report the retained behavioral core, material keep/condense/move/delete decisions
with reasons, trigger changes, relevant checks and deliberately unresolved facts.
For substantive cuts, include before/after lines, words and files. For acceptance
reviews, identify the stop condition and justify remaining blocking gates.

Stop when the requested audit or authorized revision is delivered and relevant
checks pass. Do not keep trimming merely because further cuts are possible.
