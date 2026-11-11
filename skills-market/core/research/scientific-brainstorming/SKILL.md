---
name: scientific-brainstorming
description: Generate, challenge, or compare candidate scientific research directions with explicit assumptions and evidence limits. Use for requested ideation or prioritization; not hypothesis validation, clinical advice, or permission to run experiments.
license: MIT
metadata:
  version: "1.4.1"
  source-version: "1.4-local.2"
  upstream-version: "1.4"
  skill-author: "K-Dense Inc."
  upstream-repository: "https://github.com/K-Dense-AI/scientific-agent-skills"
  upstream-commit: "92ace75ac21efe19a620434e0ca4e356081fe807"
---

# Scientific Brainstorming

Produce candidate directions, their assumptions, and discriminating next checks.
Brainstorming supplies proposals, not validation or approval to execute them.
Keep ideas, assumptions, predictions, located evidence, and actual decisions
distinct. Preserve human ideas, negative evidence, and unresolved disagreement.

## Scope and generate

Infer the focal question, constraints, and decision from the request and relevant
project records. Ask only for missing information that changes the task. An
ordinary chat brainstorm can be completed in the response without a workshop,
JSON register, scoring system, or new project-management documents.

- **Direct AI-assisted session:** generate candidates and then critique them.
  Disclose actual information exposure and missing expertise. Multiple model
  roles or samples are perspectives, not independent experts or replications.
- **Real human session:** private initial generation, leader-last sharing, and
  independent ratings can reduce particular participation/anchoring problems.
  Do not invent participants, dissent, reviews, or approvals. This skill does
  not itself authorize contacting people or spawning agents.

Vary mechanisms and assumptions, not just wording. Include a plausible null,
measurement explanation, or simpler alternative when relevant. Record what each
retained idea predicts and what would make it wrong or uninformative. Analogies
need explicit mappings and mismatches; they are proposals rather than evidence.

## Challenge and compare

State relevant criteria and tradeoffs. Qualitative comparison is usually enough.
For requested numeric scoring, expose scale anchors, directions, weights, raw
ratings, uncertainty, and sensitivity. Scores support a decision; they do not
establish truth, erase disagreement, or automatically select a winner.

Challenge shortlisted ideas with competing explanations, confounding,
measurement failure, feasibility, and concrete harms. Identify an actual
independent reviewer when one participated; otherwise label the self-critique.

Verify citations and novelty claims against primary sources. An initial idea
round before literature review may help avoid anchoring, but honor evidence-first
requests and required factual checks. Record search limits and reopen ideas when
evidence changes the framing. A bounded search cannot establish that an idea
has never been studied.

## Deliver the decision support

Report candidates, evidence for/against, central uncertainties, a recommendation,
and the smallest useful next discriminating check. Do not invent a researcher
decision. Carry existing authorization forward, but a proposal alone does not
authorize a new experiment, method change, expensive run, or external disclosure.
Route clinical or regulated execution to the relevant expertise and reviews
only when the proposed action actually requires them.

For project recording use the existing convention; see
[local workflow](references/local_workflow.md). Ideas formed after seeing outcomes
are exploratory; a saved brainstorm is not preregistration or validation.

## Optional modes and tools

Load only the resource needed:

| Need | Resource |
| --- | --- |
| Alternative generation methods | [Methods](references/brainstorming_methods.md) |
| Human, direct, or asynchronous facilitation | [Workflows](references/facilitation_workflows.md) |
| Scoring schemas, uncertainty, sensitivity | [Evaluation](references/idea_evaluation.md) |
| AI provenance, disclosure, restricted information | [Responsible AI](references/responsible_ai.md) |
| Evidence and dated policy summaries | [Sources and limits](references/sources.md) |

The optional Python 3.11+ standard-library helpers are `scripts/session_scaffold.py`,
`scripts/validate_register.py`, and `scripts/evaluate_matrix.py`; inspect `--help`
and the evaluation reference before use. They make no network/model calls.
Keep outputs in the chosen record location and preserve existing meaningful
records. The scaffold contains pending stages, not completed work. The validator
checks selected structure/provenance fields, not truth or all governance records;
the matrix leaves decisions to the researcher. The retained MIT notice and
upstream provenance cover this adapted skill; citation does not authorize edits
to unrelated research artifacts.
