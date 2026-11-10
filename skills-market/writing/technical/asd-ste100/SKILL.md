---
name: asd-ste100
description: Clarify English instructions, tool descriptions, errors or agent messages when ambiguity has a concrete cost, or when STE/plain-language rewriting is explicitly requested. Not a default style for all dense prose, creative writing or marketing.
metadata:
  version: "0.4.1"
---

# STE-Inspired Clarity

Read for meaning before rewriting. Preserve facts, actor, conditions, exceptions,
units, scope and confidence. “May have failed” must not become “failed”; a clearer
sentence must not invent a cause, measurement or certainty.

For a procedure/error/tool contract, use strict structural guidance: one instruction
per sentence, an explicit actor/object where ambiguity matters, consistent names,
short noun clusters and unambiguous conditions. Aim for at most 20 words in an
instruction and 25 in a description, one topic and at most six sentences per paragraph.
Split semicolon chains and sequences into clear sentences or lists.

For explanatory prose, use those techniques as clarity aids rather than forcing
an alien voice. Prefer direct verbs and familiar vocabulary; avoid rotating names
for the same entity. Keep necessary domain terms and define them when needed.
Simple tenses/active voice help when they preserve temporal meaning and agency;
retain a compound tense or passive construction when simplifying loses information.

The official approved dictionary is not bundled. Lexical choices are heuristic;
this skill cannot certify ASD-STE100 compliance. For exact controlled-language
requirements, use the official standard and an appropriate domain glossary. Read
[references/writing-rules.md](references/writing-rules.md) for rule categories and
sources, or [examples/before-after.md](examples/before-after.md) for a relevant case.

`scripts/ste-lint.py` is an optional structural aid, not proof of meaning or standards
compliance. Inspect its help for file/stdin, JSON, baseline and rule controls.
Its hard/advisory categories describe local tooling, not new acceptance policy.
Do not remove hedges merely to silence a length/style warning.

Return rewritten text alone by default. On request, show original/revised wording
and the relevant rule. Briefly explain an unchanged phrase only when simplifying it
would lose necessary precision. If already clear, preserve it. Stop when ambiguity
is resolved, not when the text is shortest or every heuristic has been satisfied.
