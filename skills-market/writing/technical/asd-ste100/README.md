# STE-inspired technical writing

Use this skill to clarify English when a reader needs to follow an instruction, understand a tool’s behavior, or evaluate a technical explanation. It draws on [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/) for procedural writing.

## How the skill edits a passage

For procedures and tool contracts, make each action and its conditions explicit. For example, “If the export times out, retain the partial file for inspection” keeps the failure condition with the instruction it governs.

For an explanation, lead with the point the reader wants to understand and keep the technical detail that supports it. A result and its comparator often belong in the same sentence. Write a final answer that a colleague can read without seeing earlier progress updates. The [worked examples](examples/before-after.md) show how the style changes with the task.

A rewrite returns the revised text by default. Ask for a comparison to see the original wording and the reason for a change.

## Structural checks

The optional linter checks patterns such as sentence length, passive constructions, and incomplete list items. Its word-count targets apply to strict STE-style passages. Review explanatory prose for accuracy, flow, and the relationships between claims. A structural check cannot verify that an edit preserved the source’s meaning.

The deterministic linter checks semicolons, a short list of soft phrasal verbs (spin up, reach out, dive into, kick off, circle back, touch base), nominalizations, marketing adjectives, passive voice, present-perfect forms (including irregular participles such as "has run"), long sentences, synonym rotation, and dangling conjunctions in supported list items. It does not check noun-cluster length (that needs part-of-speech tagging) and it does not know phrasal verbs outside its list, so "take off the panel" passes. It never flags hedges or modality.

The dangling-conjunction rule checks list markers at the start of a line with zero to three leading spaces and ASCII spaces after the marker. It supports unordered markers `-`, `*`, and `+`, and ordered numeric markers that end in `.` or `)`, such as `1.` or `1)`. It checks indented continuation lines up to the final meaningful line. It does not parse list syntax inside blockquotes, lazy continuation, or full nested-list semantics. A standalone line with four or more leading spaces is not treated as a list marker. Within an active list item, indentation at the computed content column is treated as continuation text. Fence detection follows the linter's existing simple rule: a stripped line beginning with three backticks or three tildes toggles the fence state.

The intentionally invalid examples/linter-edge-cases.md file demonstrates incomplete Markdown list items. Run python scripts/ste-lint.py examples/linter-edge-cases.md to confirm that the linter reports the two expected findings. The file is a test fixture and should not be used as compliant STE prose.

Run the built-in checks from the skill directory with `python3 scripts/ste-lint.py --selftest`. For formal STE requirements, consult the official standard and your domain glossary. The [rule summary](references/writing-rules.md) gives the sources used here.

## Installation

This collection includes the revised skill in the `writing-workstation` and `macos-personal` profiles. The commands below install the upstream release.

### Quick Install (npx skills)

The fastest way to install this skill is the [skills CLI](https://skills.sh/) — no clone, no path setup. Run it from your project root:

```bash
npx skills add danyuchn/asd-ste100-skill
```

This pulls the skill from the GitHub repo and installs it for the current project. The CLI sends anonymous install telemetry (skill name and timestamp, no personal or device information) to help rank skills on the skills.sh leaderboard. Set `DISABLE_TELEMETRY=1` to opt out.

Update later with `npx skills update`.

### Clone

```bash
git clone https://github.com/danyuchn/asd-ste100-skill ~/.claude/skills/asd-ste100
```

This clones the repo into `~/.claude/skills/`, making the skill available in every Claude Code project. Best for contributors and anyone who wants a live checkout that updates with `git pull`.

## Usage

- “Clarify this tool description so the caller can tell when to retry.”
- “Rewrite these validation notes for a collaborator who has not seen our progress updates.”
- “Apply strict STE-style guidance to this procedure and show the changes.”

## Sources

- [ASD-STE100 official site](https://www.asd-ste100.org/)
- [ASD-STE100 — About STE](https://www.asd-ste100.org/about_STE.html)
- [ASD Europe — Simplified Technical English](https://www.asd-europe.org/standards-specifications/simplified-technical-english/)
- [Simplified Technical English — Wikipedia](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- [TechScribe — ASD-STE100 Simplified Technical English](https://www.techscribe.co.uk/techw/asd-simplified-technical-english.htm)

## License

MIT — see [LICENSE](LICENSE).
