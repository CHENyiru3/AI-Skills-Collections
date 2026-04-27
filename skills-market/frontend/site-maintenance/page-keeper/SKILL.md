---
name: page-keeper
domain: frontend
description: Create a repo-specific maintenance skill for a personal website. Use this skill whenever the user wants to turn a website repo into a reusable maintenance workflow, codify site-specific editing rules, teach an agent which website sections can change and which must stay fixed, or generate a maintenance skill for an academic site, portfolio, blog, lab page, or personal homepage. Use it even if the user does not explicitly say "skill" but clearly wants persistent AI-safe maintenance rules for a website repo.
---

# Page Keeper

`page-keeper` is a meta-skill. Its job is not to directly maintain the website. Its job is to inspect a website repo, extract structure and rules, ask only the missing high-value questions, and then generate a repo-specific maintenance skill for that site.

Optimize for personal websites generally. Be especially alert to academic and tech personal-site patterns such as publications, CVs, profile sections, project pages, news, downloadable assets, and repo-specific formatting contracts.

## What To Produce

Always work toward these outputs, in order:

1. `Repo assessment`
2. `Discovered rules`
3. `Questions for the user`
4. `Confirmed rules`
5. `Rulebook`
6. `Repo-specific maintenance skill outline`
7. `Final downstream SKILL.md draft`
8. `Suggested eval prompts`

Do not jump directly to the downstream skill.

## Default Workflow

### 1. Inspect the repo first

Start with repo exploration, not questions.

Identify:
- framework and stack
- route pages and entrypoints
- layouts, templates, includes, or shared components
- data files and config files
- content directories for homepage, projects, publications, CV, blog/news, and personal pages
- repeated renderers and duplication patterns
- file naming and versioning conventions
- special logic for publications, references, CVs, downloadable files, and profile metadata

Use [references/repo-discovery-checklist.md](references/repo-discovery-checklist.md) as the inspection checklist.

### 2. Build a repo map

Summarize the repo in a compact map with:
- framework
- main routes/pages
- content sources
- shared renderers
- configuration sources
- data-driven sections
- section duplication risks
- special derived-value rules such as dates, versions, or filenames

### 3. Split inferred rules from user-only rules

Always classify findings into two buckets.

#### Inferred from repo

Infer these directly when possible:
- framework and layout chain
- section inventory
- where content lives
- shared partials or includes
- rendering order and grouping
- bibliography or CV logic
- asset naming conventions
- duplication and centralization patterns
- existing tone and formatting patterns

#### Must be confirmed with the user

Ask before freezing these:
- which sections may be edited proactively
- which sections must use exact user wording
- what content is sensitive or must never be inferred
- what visual/style freedom is allowed
- which formatting preferences are intentional rather than accidental
- how references and publications should be grouped when multiple valid styles exist
- what future agents may restructure versus only lightly edit

Use [references/question-catalog.md](references/question-catalog.md) to guide the question pass.

### 4. Ask only high-impact questions

After inspection, ask only questions that materially change the downstream maintenance skill.

Focus on:
- site purpose and audience
- editable versus locked sections
- exact-wording-only sections
- style and tone preferences
- publication/reference formatting preferences
- date and version display rules
- duplication versus centralization preferences
- approval-required change categories

Do not ask questions the repo already answers.

### 5. Build a normalized rulebook

Before drafting the downstream skill, create a rulebook using the schema in [references/rulebook-schema.md](references/rulebook-schema.md).

The rulebook must cover:
- framework and architecture
- content inventory
- editable sections
- restricted sections
- exact-wording sections
- formatting contracts
- reference and publication rules
- versioning and date rules
- style and voice rules
- duplication and centralization rules
- approval-required changes
- verification checklist

### 6. Generate the downstream maintenance skill

Use [references/generated-skill-template.md](references/generated-skill-template.md) as the template for the repo-specific maintenance skill.

The downstream skill must teach future agents to:
- inspect before editing
- prefer shared renderers over duplicated edits
- preserve repo-specific formatting contracts
- ask before editing restricted sections
- respect exact-wording-only zones
- keep homepage and dedicated pages consistent
- derive dates, versions, and asset paths from config or naming rules instead of hardcoding them

## Output Contract

Use this section order in your response when running `page-keeper`:

### Repo assessment
State the framework, core directories, shared renderers, data sources, and special conventions.

### Discovered rules
List the rules that can already be inferred from the repo.

### Questions for the user
List only unresolved, high-impact questions.

### Confirmed rules
After user response, restate the rules that are now fixed.

### Rulebook
Write the normalized rulebook.

### Repo-specific maintenance skill outline
Summarize the sections and behavior of the downstream skill.

### Final downstream SKILL.md draft
Provide the full draft or write it to disk when the user asked for implementation.

### Suggested eval prompts
Provide 2-3 realistic test prompts for the downstream skill.

## Common Website Patterns To Recognize

### General personal-site patterns
- homepage/about page
- project list and project detail pages
- blog or news collection
- downloadable CV or resume
- profile metadata block
- shared header/footer/nav
- duplicated content across homepage and dedicated pages

### Academic and tech-site patterns
- publication pages driven by BibTeX, YAML, JSON, or custom data
- accepted versus published versus preprint distinctions
- conference posters and presentations
- CV versioning or file naming rules
- institution and affiliation sensitivity
- project pages tied to publications
- exact display rules for badges, authorship markers, and manuscript status

Do not assume these exist, but actively check for them.

## Safety and Scope Boundaries

- Do not rewrite protected sections without explicit user approval.
- Do not infer sensitive facts such as affiliations, job status, future plans, or publication status if the repo does not support them.
- Do not treat formatting inconsistencies as mistakes until you have checked whether they are intentional.
- Do not overgeneralize from one page; always look for shared renderers and templates first.
- Prefer centralization rules over one-off edits when the repo structure supports it.

## Example Prompts

**Example 1**
User: "Turn my academic website repo into a maintenance skill so future agents know which sections they can polish and which parts require my exact wording."

**Example 2**
User: "Inspect this portfolio website and create an AI-safe maintenance skill for it. I want the site style preserved and duplicated content kept in sync."

**Example 3**
User: "I want a reusable skill that understands my personal homepage repo and asks me about the rules it cannot infer."

## Suggested Eval Prompts

See [evals/evals.json](evals/evals.json) for starter prompts covering academic, portfolio, and duplication-heavy personal sites.
