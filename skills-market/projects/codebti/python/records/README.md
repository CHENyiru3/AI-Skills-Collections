# Session Records

This folder stores CodeBTI interview records. A record preserves the user's project description, fixed answers, adaptive answers, agent observations, and final style inference.

Use one markdown file per interview session.

Filename format:

```text
YYYY-MM-DD-project-slug.md
```

Example:

```text
2026-04-22-python-cli-tool.md
```

## Recording Rules

- Record the user's selected answer and any short explanation they gave.
- Record answer changes when the user goes back and reselects.
- Keep hidden scoring separate from user-facing answers.
- Do not record secrets, credentials, private tokens, or unrelated personal details.
- Prefer concise notes over full conversation transcripts.
- Preserve enough evidence that another agent can understand why the final `CodeStyle.md` was generated.

## What To Record

Each session should include:

- project summary,
- interview date,
- language target,
- fixed question answers,
- adaptive question answers,
- answer changes,
- style-axis summary,
- pattern signals,
- unresolved assumptions,
- generated output files.

Use [session-record.template.md](session-record.template.md) as the starting point.
