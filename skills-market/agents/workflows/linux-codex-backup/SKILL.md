---
name: linux-codex-backup
description: Locate and back up local Codex chat history on Linux, including yiru-linux, or diagnose Linux backup paths, GitHub CLI access, and explicitly requested systemd user jobs. Use with codex-backup; use macos-codex-backup for Mac-specific setup.
metadata:
  version: "1.0.0"
---

# Linux Codex backup

Use the [`codex-backup` skill](../codex-backup/SKILL.md) and its bundled exporter. Install both skills as sibling directories. Read [the Linux setup](references/linux-setup.md) for the verified yiru-linux baseline, commands, and service constraints; recheck paths on another host.

Honor `CODEX_HOME` and `CODEX_SQLITE_HOME`. The exporter also accepts `--codex-home` and `--sqlite-home`; pass the latter when `config.toml` sets `sqlite_home`, because the exporter does not read that configuration. Read live SQLite databases through the exporter; do not copy database files without their WAL state.

Preview locally, check the intended account and transcript scope, then sync only to the user's authorized private archive. New Linux transcripts have the `Linux` tag and sync commits carry `[Linux]`. Keep an existing archive's timezone and fuller transcripts when sharing it with another machine.

Publish backup commits directly to the private archive's default branch and verify the pushed commit. For authorized changes to these skills in `AI-Skills-Collections`, also commit and push directly to its default branch. That public collection holds skill code and documentation; keep transcripts, profiles, credentials, and archive checkouts outside it.

Use `snapshot` and `sync` for manual backups. The shared runner's `install` action creates a macOS LaunchAgent and cannot install a Linux schedule. Only configure a systemd user service/timer when scheduling is requested; use absolute paths, include the user's GitHub CLI directory in `PATH`, and verify authentication in the service environment.
