---
name: macos-codex-backup
description: Locate and back up macOS Codex chat history, or diagnose an existing macOS backup job. Use for Mac-specific history locations, GitHub authentication, or LaunchAgent issues.
metadata:
  version: "1.0.0"
---

# macOS Codex backup

Use the [`codex-backup` skill](../codex-backup/SKILL.md) and its bundled exporter. Install both skills together so the exporter remains available. For a manual backup, follow its [setup template](../codex-backup/references/setup-template.md) from the Mac that holds the history.

Use `CODEX_HOME` when configured and `~/.codex` otherwise. Check that the Codex account matches the intended archive and that `gh auth status` reports access to the private destination. New Mac transcripts have the `MacOS` tag. Mac sync commits carry `[MacOS]` in the subject.

Publish backup commits with a direct push to the authorized private repository’s default branch, without a pull request. Follow the same direct-push workflow for authorized updates to this skill in `AI-Skills-Collections`.

For an explicitly requested macOS schedule, the shared runner's `install` command creates a per-user LaunchAgent and prints its service label and log path. Use a persistent `gh auth login`, since the agent runs outside the interactive shell. Verify the service with `launchctl print <service>` and the pushed commit separately.
