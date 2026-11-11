# Back up Codex on macOS, Linux, or Windows

Run the backup in the environment that contains the Codex history. Use Python 3.9 or later, Git, GitHub CLI, and an initialized private GitHub repository with push access.

| Where Codex runs | Default history directory | Shell |
|---|---|---|
| macOS | `~/.codex` | Terminal |
| Linux | `~/.codex` | Your Linux shell |
| Native Windows | `%USERPROFILE%\.codex` | PowerShell |
| Codex CLI inside WSL | `~/.codex` in that distribution | The WSL shell |

The runner honors `CODEX_HOME` and `CODEX_SQLITE_HOME`. Pass `--codex-home` or `--sqlite-home` when an app setting puts history elsewhere. If Windows and WSL use separate histories, run once in each environment. Each run adds its own local sessions to the same repository. Do not point both runners at a shared live database.

## Reusable setup prompt

~~~text
Back up the local Codex conversations from this machine.
Platform and environment: <macOS, Linux, native Windows, or WSL>
Private GitHub repository: OWNER/REPO
Transcript timezone: UTC
Codex home: detect the current environment or use <path>
Preview the local transcripts, then perform a one-time sync to GitHub.
~~~

## Run a manual backup

Open the skill root, the folder containing `SKILL.md` and `scripts/`. Save a `profile.json` there and substitute your private destination. Keep the timezone consistent across machines using the same repository.

~~~json
{
  "repository": "OWNER/REPO",
  "timezone": "UTC"
}
~~~

Check `gh auth status`. If needed, sign in with `gh auth login --hostname github.com --git-protocol https`.

**macOS, Linux, or WSL**

~~~bash
python3 scripts/codex_chat_archive.py snapshot --profile profile.json --output "$(mktemp -d)"
python3 scripts/codex_chat_archive.py sync --profile profile.json
~~~

**Native Windows PowerShell**

~~~powershell
py -3 -m pip install --user tzdata
$preview = Join-Path $env:TEMP ("codex-preview-" + [guid]::NewGuid().ToString())
py -3 scripts/codex_chat_archive.py snapshot --profile profile.json --output $preview
py -3 scripts/codex_chat_archive.py sync --profile profile.json
~~~

Use `python` in place of `py -3` if your Windows installation provides only `python`. On Linux, install your distribution's `tzdata` package if Python cannot resolve the configured zone. Keep previews in private folders and remove them when finished.

`snapshot` creates local Markdown files. `sync` verifies that the remote is private, updates one file per thread under `sessions/YYYY/MM/`, and pushes changes. The source platform appears in the commit subject. A sync run inside WSL uses `[Linux]`. The commit body summarizes new prompts and replies, while the Git diff shows the text. Run the same `sync` command for later updates. Verify the commit and inspect a transcript before relying on the archive.

The runner reads supported local Codex SQLite history and older session logs. It exports user-facing text and progress updates. Attachments, raw tool output, background threads, and cloud-only chats are outside this export. If an older copy of a thread lacks messages already archived by another machine, the runner preserves the fuller transcript and reports the thread. If a Codex update changes the storage schema, verify the local preview before pushing.

Official references

- [Codex configuration and state locations](https://learn.chatgpt.com/docs/config-file/environment-variables)
- [Native Windows Codex](https://learn.chatgpt.com/docs/windows/windows-sandbox) and [Codex in WSL](https://learn.chatgpt.com/docs/windows/wsl)
- [Python time-zone data](https://docs.python.org/3/library/zoneinfo.html#data-sources)
