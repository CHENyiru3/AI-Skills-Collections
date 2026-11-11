---
name: scientific-coding-governance
description: Preserve scientific intent and meaningful results while implementing or debugging research analyses within an agreed scope. Use when code can affect methods, data, evaluation, or interpretation; not as an approval ritual for unrelated mechanical edits.
metadata:
  version: "1.0.0"
---

# Scientific Coding Governance

The researcher controls scientific intent; the agent may choose reversible,
method-preserving implementation within the requested scope. Reuse established
authorization and completed methodological configurations. Ask only when a
missing or changed scientific choice affects the next action.

Infer the relevant analysis contract from the request: inputs/population,
comparison, method/settings, metric/threshold, and output. State material
assumptions briefly in the conversation; do not create a separate contract system.

Do not silently change that contract after seeing results. Preserve raw data,
meaningful outputs, sample identity, and evaluation boundaries. For result-impacting
debugging, reruns, or interpretation, read the corresponding section of
[governance.md](references/governance.md).

Choose verification that could change acceptance: syntax/import checks, relevant
existing tests, and semantic checks tied to the approved analysis. An explicitly
requested benchmark remains authorized; unrelated infrastructure does not become
mandatory because this skill was selected.

Report what changed, what ran, produced outputs, and remaining limitations.
Finish the agreed task before proposing additional experiments or cleanup.
