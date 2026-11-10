---
name: humanizer
domain: writing
description: Clean up prose that sounds robotic, generic, corporate or unlike the user’s voice, especially when the user requests humanizing or removal of AI tells. Preserve meaning/register; not a general writing default or a mandatory full academic edit.
license: MIT
metadata:
  author: ice-ninja
  version: "3.0.1"
---

# Humanizer

Improve naturalness without changing meaning, evidence or the user's voice.
Diagnose actual vocabulary, structure or tone problems before rewriting; do not
change a passage merely because it contains a common AI-associated word.

Remove inflated significance, vague attribution, formulaic transitions, empty
enthusiasm and repeated sentence shapes. Prefer concrete wording supported by the
source. Vary rhythm where it helps, without inserting anecdotes, opinions, humor,
slang or new facts to simulate a human author.

Preserve technical terms, necessary hedges, quantities, citations and scope.
Academic/technical prose should become more precise and readable, not more casual.
Use academic-writing-editor when the task also needs structural/scientific editing;
a small style cleanup does not require chaining a full manuscript workflow.

Load a reference only for the diagnosed problem: `references/ai-vocabulary-list.md`,
`references/sentence-patterns.md`, `references/rhythm-techniques.md`, or
`references/content-type-guides.md`. The validation checklist is optional for a
difficult case, not a new acceptance gate or a mechanical blacklist.

Return the revised text by default, with a brief explanation only when requested
or a material change needs attention. Check that the rewrite retains the original
claims and register, then stop. Naturalness is not a guarantee that a detector will
classify text a particular way.
