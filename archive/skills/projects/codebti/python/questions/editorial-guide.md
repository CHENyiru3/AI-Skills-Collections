# Question Editorial Guide

Use this guide when turning draft CodeBTI questions into final interview questions.

The goal is a serious but approachable questionnaire. Users should not feel tested on design-pattern vocabulary or Python seniority. They should choose the style they would naturally want to maintain.

## Voice

Write in plain engineering language.

Prefer:

- "data shape" over "schema" when the meaning is not technical validation,
- "change later" over "extensibility",
- "shared state" over "global mutable state",
- "clear boundary" over "encapsulation boundary",
- "small helper" over "utility abstraction",
- "project code" over "implementation surface".

Avoid:

- academic labels in user-facing choices,
- jokes or personality labels,
- words that make one answer sound obviously more mature,
- long paragraphs before the user sees the choices.

## Balance Rules

Every choice must be valid for some real project.

Do not write choices where:

- one option is obviously unsafe,
- one option is obviously overengineered,
- one option is only for beginners,
- one option is only for experts,
- one option depends on a hidden requirement.

When a choice has a risk, mention the risk only in hidden scoring or `CodeStyle.md` implications unless the risk is part of the user-facing tradeoff.

## Code Example Rules

Use code when it makes a preference easier to feel. Do not use code when the scenario alone is clearer.

Good code examples:

- show the same small task in several styles,
- fit on one screen,
- use realistic names,
- avoid external libraries unless dependency choice is the point,
- do not contain distracting edge cases.

For multi-choice code comparisons, keep the implementation quality even. If option A has typing, option B should not look sloppy just because it represents a lighter style.

## Choice Label Rules

Use neutral labels.

Prefer labels like:

- Object-centered,
- Function-first,
- Data-first,
- Flat procedural,
- Boundary-first,
- Pipeline-style,
- Validation-first.

Avoid labels like:

- Strict,
- Pure,
- Advanced,
- Simple,
- Quick and dirty,
- Enterprise,
- Best practice.

## Skill-Test Prevention

The questionnaire should not reward the user for guessing the "best" answer.

To reduce this problem:

- ask what they would maintain, not what is theoretically correct,
- keep every choice plausible,
- use the same task across choices,
- avoid named patterns in user-facing text,
- keep hidden scoring hidden,
- avoid examples where the longest code always looks most professional.

## Medium Rewrite Workflow

For each draft question:

1. Identify the one main dimension it tests.
2. Remove secondary dimensions unless they are necessary.
3. Rewrite the setup in one or two sentences.
4. Normalize choice labels.
5. Rewrite choices so each one has a real tradeoff.
6. Shorten code examples and balance their quality.
7. Add hidden style-axis scoring.
8. Add secondary pattern signals.
9. Add `CodeStyle.md` implications.

## Final Quality Check

Before a question is accepted, verify:

- a non-pattern expert can answer it,
- the choices are not ranked by obvious professionalism,
- the code snippets are short enough to scan,
- the question tests one main dimension,
- the hidden scoring can affect generated coding guidance,
- the wording is serious, simple, and not condescending.
