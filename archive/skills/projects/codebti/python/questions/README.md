# CodeBTI Question Framework

This folder defines the CodeBTI interview system. The interview helps an agent convert a user's project goals and coding preferences into a project-specific `CodeStyle.md`, `SKILL.md`, or `SPEC.md`.

The first version is Python-first. Future languages should add parallel fixed question sheets instead of changing the shared interview flow.

## Interview Flow

1. Ask the user for a short project description.
2. Ask the 10 fixed Python questions from [fixed-python.md](fixed-python.md).
3. Ask exactly 5 adaptive follow-up questions using [adaptive-question-guide.md](adaptive-question-guide.md).
4. Record answers in a session record file using [../records/session-record.template.md](../records/session-record.template.md).
5. Infer style dimensions and pattern tendencies.
6. Generate a project-specific `CodeStyle.md`.

## Question Style

Questions should use concrete examples instead of pattern terminology. A user should be able to answer by looking at a small scenario or code section and choosing the style they would rather maintain.

Good questions:

- present realistic Python tradeoffs,
- cover one primary dimension at a time,
- use short code snippets when code makes the choice clearer,
- avoid trick choices,
- keep design-pattern scoring hidden from the user.

Use [question-format.md](question-format.md) for the required card structure.
Use [editorial-guide.md](editorial-guide.md) when rewriting draft questions into final form.
Use [../records/README.md](../records/README.md) for recording guidance.

## Scoring Principle

Answers map to CodeBTI style dimensions first and design-pattern signals second. For example, a choice may primarily signal "interface-first abstraction" and only secondarily suggest Strategy, Bridge, or Abstract Factory.

The interview result should guide coding consistency. It should not judge the user's ability or personality.

## Organization Pass

When the user provides draft questions, organize them with a medium rewrite:

1. Keep the user's dimension and core idea.
2. Rewrite the scenario and choices for balance.
3. Simplify wording without making the topic unserious.
4. Add or trim code examples so each option feels equally realistic.
5. Add hidden scoring and `CodeStyle.md` implications.
