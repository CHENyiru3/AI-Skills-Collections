---
name: codex-backup
description: Preview, backfill, or sync local Codex chat transcripts from macOS, Linux, Windows, or WSL into a private GitHub Markdown archive. Use when asked to back up Codex chat history or reuse a backup on another machine.
metadata:
  version: "1.0.0"
---

# Codex backup

Read [the setup template](references/setup-template.md) for the history locations, profile, and commands for the source machine. Use the bundled exporter to preview local sessions and verify their scope before syncing to the authorized private repository.

- Keep one Markdown file per thread under `sessions/YYYY/MM/`. Match by thread ID so a rename or a new message keeps the same path.
- Publish backup commits with a direct push to the authorized private repository’s default branch, without a pull request.
- Verify the pushed commit. Its subject identifies the source platform, its body summarizes message counts, and its diff contains the changes.
- Preserve the fuller archive when a machine has an incomplete copy of a thread. Report local history that the current reader cannot access.

For authorized updates to these backup skills in `AI-Skills-Collections`, commit and push directly to the collection’s default branch.

The exporter covers local conversation text and progress updates. Use a separate account export for cloud-only conversations and other artifacts.
