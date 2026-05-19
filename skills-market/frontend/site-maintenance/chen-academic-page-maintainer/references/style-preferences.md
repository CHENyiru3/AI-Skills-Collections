# Style Preferences

## Voice

- Default tone: formal academic
- Allowed warmth: light personality is acceptable in transitions and on the life page
- Keep research-facing pages concise, credible, and specific

## Section-specific expectations

- Homepage:
  - polished but restrained
  - do not paraphrase protected identity statements
- Publications:
  - factual and complete
  - no hidden authorship
- CV:
  - concise and factual
  - avoid stylistic rewriting of protected academic facts
- Projects:
  - clear and technically grounded
  - preserve meaning when polishing
- Tech Blog:
  - clear, practical, and engineering-focused
  - keep the index scannable with dates, tags, descriptions, and direct read links
  - do not mix general sample posts into the Tech Blog index
  - expose the Tech Blog RSS feed with a compact subscribe link on the landing page
  - bilingual posts should default to English and expose a compact English/Chinese switcher without duplicating cards on the index
  - disable the al-folio related-post block for Tech Blog articles unless the user explicitly asks for recommendations
  - keep Tech Blog screenshots responsive to the article/window size, preserve aspect ratio, and small enough to inspect in one viewport
  - Website Management TechBlog drafts may be polished lightly for clarity, but preserve technical claims and code unless the user asks for editing
- Life page:
  - warmer and more personal than research-facing pages
  - pair concise prose with real photos when available; keep sections text-only when no photos are provided
- Research Radar:
  - concise, scannable, and research-facing
  - use the Hot Topic hint to foreground the day's strongest theme when available
  - separate computational methods, biomedicine, other fields, and Friday BioTech News Delivery clearly
  - keep Friday BioTech items visibly labeled as industry/news context
  - preserve source links, DOI information, and recommendation rationale

## Formatting behavior

- Preserve section ordering unless the user requests change.
- Reuse shared includes and existing patterns before introducing new ones.
- Avoid adding new duplicated styles or hardcoded factual values when a shared source of truth exists.
- Keep Tech Blog immediately next to Research Radar in navigation unless the user requests a different order.
- Preserve Life page responsive gallery grids when real photos are present, but do not add fake frames for sections without photos.
- When applying Website Management notes, preserve exact protected wording and make only the minimum website changes implied by the editable mirror or draft note.
- When applying a new `Website_management/TechBlog/*.md` post candidate, keep the prose practical and readable while preserving technical claims, code, filenames, and commands.
- For Research Radar, preserve generated article wording unless the user asks for a correction or regeneration.

## Finish-line checks

- Confirm that edits match the intended tone for the section.
- Confirm that factual language was preserved where exact wording is required.
- Confirm that any new ambiguity was escalated to the user instead of guessed.
