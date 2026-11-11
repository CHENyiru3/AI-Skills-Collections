# Linux setup

## yiru-linux baseline

Observed on 2026-11-11. These are setup facts, not portable defaults; recheck before a backup.

| Item | Verified location or behavior |
| --- | --- |
| Host and shell | `yiru-linux`, Linux Mint, Bash |
| Collection checkout | `/home/yiru/projects/AI-Skills-Collections` |
| Installed skill roots | `/home/yiru/.codex/skills/codex-backup` and `/home/yiru/.codex/skills/linux-codex-backup` |
| Codex home | `/home/yiru/.codex`; `CODEX_HOME` is unset |
| SQLite directory | `/home/yiru/.codex`; `CODEX_SQLITE_HOME` and `config.toml`'s `sqlite_home` are unset |
| Current history | `state_5.sqlite`, `thread_history_1.sqlite`, and `sessions/**/rollout-*.jsonl` |
| Python and Git | `/usr/bin/python3` (3.12), `/usr/bin/git` |
| GitHub CLI | `/home/yiru/.local/bin/gh`; account `CHENyiru3`, HTTPS, keyring authentication |
| Storage | Home, including the default archive checkout location, is on ext4 |
| Service manager | `systemctl --user` is available and running; this does not imply a backup timer exists |

The exporter supports the observed database schema. It reads SQLite in read-only mode, including live WAL content, and falls back to supported rollout logs. Schema details are an observed implementation, not an OpenAI storage compatibility guarantee.

## Preview and manual sync

The following Bash commands work from the collection checkout. For an installed copy, set `backup_skill="$HOME/.codex/skills/codex-backup"` instead. Keep both skill directories together so the relative references resolve.

```bash
backup_skill=/home/yiru/projects/AI-Skills-Collections/skills-market/agents/workflows/codex-backup
export PATH="$HOME/.local/bin:/usr/bin:/bin:$PATH"
codex_history="${CODEX_HOME:-$HOME/.codex}"
sqlite_history="${CODEX_SQLITE_HOME:-$codex_history}"
# If config.toml sets sqlite_home, use that directory for sqlite_history.
umask 077
preview_dir="$(mktemp -d "${TMPDIR:-/tmp}/codex-preview.XXXXXXXX")"
/usr/bin/python3 "$backup_skill/scripts/codex_chat_archive.py" snapshot \
  --codex-home "$codex_history" --sqlite-home "$sqlite_history" \
  --output "$preview_dir"
```

Inspect a transcript in the private preview directory and compare it with the local Codex thread. Check the prompts, replies, progress updates, and `Linux` tag. The preview uses UTC by default. For an existing archive, pass its profile with `--profile` to keep the same timezone. Remove the temporary preview after inspection.

Before the first upload, obtain or reuse the user's private archive destination. `AI-Skills-Collections` is public and is not a chat archive. Save a profile outside the collection, for example `~/.config/codex-backup/profile.json`, using the chosen repository and its established timezone:

```json
{
  "repository": "OWNER/PRIVATE-ARCHIVE",
  "timezone": "UTC"
}
```

Replace the example repository before syncing. On yiru-linux the desktop timezone is `Asia/Shanghai`; the profile controls transcript timestamps independently. Run `gh auth status` and verify the destination with `gh repo view OWNER/PRIVATE-ARCHIVE --json visibility,defaultBranchRef`. The runner requires an initialized private repository and refuses a public one.

```bash
/usr/bin/python3 "$backup_skill/scripts/codex_chat_archive.py" sync \
  --codex-home "$codex_history" --sqlite-home "$sqlite_history" \
  --profile "$HOME/.config/codex-backup/profile.json"
```

The local checkout is `${XDG_STATE_HOME:-$HOME/.local/state}/CodexChatArchive/<repository-hash>/checkout`; the script prints Git output. Verify that its latest `[Linux]` commit is on the remote default branch and inspect a transcript there. This exports local conversation text, not attachments, raw tool output, background threads, or cloud-only chats. Do not commit `auth.json`, `.env`, raw databases, or local profiles into the skill collection.

## When a Linux schedule is requested

The runner's `install` action is macOS-only. Use a systemd **user** oneshot service calling the same `sync` command, with absolute Python, script, history, and profile paths. Set a `PATH` containing `/home/yiru/.local/bin` on this host so `shutil.which("gh")` succeeds. Test `gh auth status` in the service context: a running user manager does not guarantee an unlocked desktop keyring.

Pair it with a user timer at the requested local time; `Persistent=true` permits a missed run at the next user-manager start. Verify with `systemctl --user list-timers`, `journalctl --user -u <service>`, and the remote commit. A user timer cannot run while the host is powered off. Enabling lingering or changing system services requires that additional scope; a manual backup does not require either.

Official state-location references: [Codex environment variables](https://learn.chatgpt.com/docs/config-file/environment-variables) and [`sqlite_home` configuration](https://learn.chatgpt.com/docs/config-file/config-reference).
