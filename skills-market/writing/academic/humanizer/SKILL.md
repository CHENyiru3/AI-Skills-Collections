---
name: humanizer
domain: writing
description: |
  Use when text sounds AI-generated, robotic, generic, corporate, over-smoothed,
  or unlike the user's voice. Also use when the user asks to humanize text,
  remove AI tells, make prose sound more natural, add voice, or reduce stiffness.
  This is a cleanup and voice-calibration skill, not a general writing-default
  skill. For academic writing, pair with academic-writing-editor first, then use
  this skill as a final anti-AI cleanup pass.
license: MIT
metadata:
  author: ice-ninja
  version: "3.0"
---

# Humanizer

Make prose sound written by a person without changing what it means.

Use this skill for cleanup, not for every writing task. The goal is to remove
high-signal AI patterns, restore natural rhythm, and preserve the right voice
for the genre.

## When to use this skill

Use `humanizer` when the user:

- asks to humanize, naturalize, de-AI, or de-corporatize text
- says the writing sounds robotic, stiff, bland, generic, or unlike them
- wants a cleanup pass after drafting
- pastes prose full of obvious AI tells, inflated tone, or repetitive structure

You may also use it without explicit request when the text is clearly:

- overstuffed with AI vocabulary or corporate phrasing
- rhythmically flat
- padded with fake significance, vague authority, or formulaic transitions

## When not to use this skill

Do not treat this as the default for all prose generation.

Do not use it to:

- inject personality into formal or citation-bound writing by default
- make accurate technical or legal text less precise
- replace `academic-writing-editor` for manuscript structure or argument flow
- introduce slang, humor, or first-person voice unless the genre supports it

## Workflow

### 1. Identify the mode

Choose one:

- **Academic mode**: manuscript, abstract, methods, results, discussion,
  literature review, reviewer response, technical note, grant prose
- **General prose mode**: email, blog post, memo, essay, marketing copy,
  social post, proposal, documentation, cover letter

If this is academic writing, use `academic-writing-editor` first for structure
and claim discipline, then use `humanizer` as the final cleanup pass.

### 2. Diagnose before rewriting

Determine which failure mode dominates:

- **Vocabulary tells**: AI words, hedges, corporate jargon, fake intensity
- **Structure tells**: repetitive sentence shape, participial trailers, rigid
  paragraph logic, lists of three everywhere
- **Voice tells**: neutralized tone, generic enthusiasm, no point of view,
  inappropriate smoothness

Load references only as needed:

- `references/ai-vocabulary-list.md` for lexical cleanup
- `references/sentence-patterns.md` for sentence and paragraph structure
- `references/rhythm-techniques.md` for cadence and voice variation
- `references/content-type-guides.md` for genre-specific constraints
- `references/validation-checklist.md` for QA or difficult cases

### 3. Rewrite with restraint

Always:

- preserve meaning, factual content, and intended register
- simplify obvious AI constructions before adding voice
- prefer specificity over hype
- prefer direct attribution over vague authority
- keep edits proportional to the problem

For general prose, add voice only where it helps:

- vary sentence length and openings
- use contractions when the genre permits
- allow a clearer stance or personality
- replace generic claims with concrete detail

For academic prose:

- keep the register formal and citation-compatible
- preserve justified hedging
- do not inject humor, edge, or casual commentary
- make sentences more direct, not more chatty

### 4. Run a final anti-AI audit

After rewriting, do one short adversarial pass:

1. Ask: "What still makes this sound AI-generated?"
2. Fix only the remaining high-signal issues

Focus on:

- leftover vocabulary clusters
- repeated sentence shapes
- fake significance or generic uplift
- over-polished symmetry
- tone mismatch for the content type

## Academic mode

In academic mode:

- keep terminology, caution, and evidence alignment intact
- replace generic phrasing with more specific, evidence-linked language
- reduce puffery, throat-clearing, and empty transitions
- keep "we" only if the source and genre support it
- never humanize by making the text casual

If a sentence is weak, make it more precise and accountable, not more friendly.

## General prose mode

In general prose:

- remove robotic transitions and filler
- reduce over-explanation
- break up uniform rhythm
- allow a clearer human stance when appropriate
- avoid making everything sound quirky or informal

Voice should feel intentional, not performatively "human."

## Output

Default output:

- the revised text only

If the user asks for explanation or if the rewrite is substantial, you may add a
brief note naming the main changes.

For especially AI-marked input, it is acceptable to provide:

1. a revised version
2. 2-4 brief bullets on the strongest AI tells that were removed

Do not pad the response with process commentary the user did not ask for.
