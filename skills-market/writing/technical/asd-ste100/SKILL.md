---
name: asd-ste100
description: Clarify ambiguous English in procedures, tool descriptions, errors, and agent messages. Use also when asked to clarify a technical explanation for a particular audience or to rewrite text in plain English or Simplified Technical English (STE).
metadata:
  version: "0.5.0"
---

# STE-inspired technical writing

Choose the style for the passage you are editing. A reader following a procedure needs an unambiguous next action. A reader evaluating a technical explanation needs to understand how the evidence supports the conclusion. A single document can serve both purposes.

## Technical explanations

Lead with the result, decision, or behavior the reader came to understand. Supply enough context to interpret that first claim, then explain the evidence or mechanism it depends on. Introduce a concept before referring to it by a pronoun or abbreviation.

Use the terminology the user and sources use. Keep domain terms that distinguish concepts the reader needs, and explain unfamiliar terms at first use. Prefer active voice when the actor matters. Preserve tense, units, conditions, exceptions, scope, and degree of confidence. If the source says an operation *may have failed*, the rewrite must preserve that uncertainty.

Let the relationship between ideas determine sentence length. Keep a condition with the behavior it governs, a measurement with its comparator, or a finding with the qualification that limits it. Split a sentence when the reader has to track a second topic or an independent action. Explanatory prose has no fixed word limit.

Write each reader-facing passage afresh for its audience. The final answer should stand on its own if the reader sees none of the progress updates. Carry over the facts and the rationale the reader needs. Leave working shorthand, tool narration, and phrasing from internal notes out of the finished text.

## Procedures, errors, and tool contracts

Give one independently executable instruction per sentence. Put a prerequisite before its action, name the actor or object where responsibility could be ambiguous, and use numbered steps when order matters. In an error message, distinguish what the system observed from a possible cause. In a tool contract, state the condition that selects each outcome.

For strict STE-style passages, aim for at most 20 words per instruction and 25 per descriptive sentence. Keep each paragraph to one topic and up to six sentences. Use the [rule summary](references/writing-rules.md) for controlled-language questions. The optional [structural linter](scripts/ste-lint.py) flags patterns for review. Only the official standard and applicable glossary can establish the vocabulary required for formal STE work.

## Deliver the revision

For a rewrite, return the revised passage alone unless the user asks for an explanation or comparison. Keep wording that already serves the reader. Check that an edit preserves the source's claims and introduces no new facts or obligations. The [worked examples](examples/before-after.md) illustrate both executable instructions and technical explanations.
