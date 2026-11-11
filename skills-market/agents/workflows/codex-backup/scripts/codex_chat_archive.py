#!/usr/bin/env python3
"""Export local, user-facing Codex messages to a private Markdown archive."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import plistlib
import re
import shutil
import shlex
import sqlite3
import subprocess
import sys
from collections import Counter, defaultdict
from contextlib import closing, contextmanager
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


HOME = Path.home()
DEFAULT_PROFILE = {"repository": "", "timezone": "UTC", "run_at": "23:55"}
PLATFORM_TAG = {"darwin": "MacOS", "linux": "Linux", "win32": "Windows"}.get(sys.platform, sys.platform)
THREAD_MARKER = re.compile(r"^<!-- codex-thread: ([a-zA-Z0-9_-]+) -->$", re.M)
MESSAGE_MARKER = re.compile(r"^<!-- codex-message: (prompt|reply|update) ([a-zA-Z0-9_-]+) -->$", re.M)
ROLE_LABELS = {"prompt": "You", "reply": "Codex", "update": "Codex update"}


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()[:12]


@dataclass(frozen=True)
class Profile:
    repository: str
    timezone: str
    run_at: str

    @property
    def origin(self):
        return f"https://github.com/{self.repository}.git"

    @property
    def zone(self):
        return ZoneInfo(self.timezone)

    @property
    def state(self):
        if sys.platform == "darwin":
            base = HOME / "Library/Application Support"
        elif os.name == "nt":
            base = Path(os.environ.get("LOCALAPPDATA", HOME / "AppData/Local"))
        else:
            base = Path(os.environ.get("XDG_STATE_HOME", HOME / ".local/state"))
        return base / "CodexChatArchive" / digest(self.repository.lower())

    @property
    def label(self):
        return f"com.codex.chatrepo-backup.{digest(self.repository.lower())}"


def load_profile(path):
    values = {**DEFAULT_PROFILE, **(json.loads(path.read_text(encoding="utf-8-sig")) if path else {})}
    profile = Profile(**values)
    if profile.repository and not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", profile.repository):
        raise ValueError("Set repository to a GitHub owner/repo name in the profile.")
    if not re.fullmatch(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]", profile.run_at):
        raise ValueError("Set run_at to a 24-hour HH:MM time in the profile.")
    try:
        ZoneInfo(profile.timezone)
    except ZoneInfoNotFoundError as error:
        raise ValueError(f"Time zone {profile.timezone!r} is unavailable. Check the name and install tzdata with this Python if needed.") from error
    return profile


@dataclass(frozen=True)
class Message:
    id: str
    role: str
    text: str
    timestamp: int | None


def read_db(path):
    db = None
    try:
        db = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=10)
        db.execute("PRAGMA schema_version").fetchone()
    except sqlite3.OperationalError:
        if db is not None:
            db.close()
        wal = path.with_name(path.name + "-wal")
        if wal.exists() and wal.stat().st_size:
            raise
        db = sqlite3.connect(path.as_uri() + "?mode=ro&immutable=1", uri=True)
    db.row_factory = sqlite3.Row
    return db


def current_identity(home):
    path = home / "auth.json"
    if not path.is_file():
        return None, None
    try:
        tokens = json.loads(path.read_text(encoding="utf-8")).get("tokens") or {}
        account = tokens.get("account_id")
        user = None
        for key in ("id_token", "access_token"):
            parts = (tokens.get(key) or "").split(".")
            if len(parts) != 3:
                continue
            segment = parts[1] + "=" * (-len(parts[1]) % 4)
            claims = json.loads(base64.urlsafe_b64decode(segment)).get("https://api.openai.com/auth", {})
            account = account or claims.get("chatgpt_account_id")
            user = user or claims.get("chatgpt_user_id") or claims.get("user_id")
        return account, user
    except (OSError, ValueError, TypeError):
        return None, None


def text_parts(parts):
    return "\n\n".join(part["text"] for part in parts if isinstance(part, dict)
                      and part.get("type") in {"text", "input_text", "output_text"}
                      and isinstance(part.get("text"), str))


def make_message(item, item_id, timestamp, item_type):
    if item_type.lower() == "usermessage":
        role = "prompt"
        text = text_parts(item.get("content", []))
    else:
        role = "update" if item.get("phase") == "commentary" else "reply"
        text = item.get("text") or text_parts(item.get("content", []))
    if not text.strip():
        return None
    text = re.sub(r"(?m)^<!-- codex-(thread|message):", r"&lt;!-- codex-\1:", text)
    stable_id = item_id if re.fullmatch(r"[a-zA-Z0-9_-]+", item_id) else digest(item_id)
    return Message(stable_id, role, text, timestamp)


def timestamp_ms(value):
    if not isinstance(value, str):
        return None
    try:
        return int(datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp() * 1000)
    except ValueError:
        return None


def read_rollout(path):
    messages = {}
    legacy = []
    with path.open("rb") as file:
        for number, line in enumerate(file, 1):
            if b'"event_msg"' not in line[:160]:
                continue
            try:
                record = json.loads(line)
                payload = record["payload"]
            except (ValueError, KeyError, TypeError):
                continue
            item = payload.get("item") or {}
            kind = payload.get("type")
            if kind == "item_completed" and item.get("type") in {"UserMessage", "AgentMessage"} and item.get("id"):
                msg = make_message(item, item["id"], payload.get("started_at_ms"), item["type"])
                if msg:
                    messages[msg.id] = msg
            elif kind in {"user_message", "agent_message"} and isinstance(payload.get("message"), str):
                is_user = kind == "user_message"
                item = {"content": [{"type": "text", "text": payload["message"]}], "phase": payload.get("phase")}
                msg = make_message(item, f"legacy-{number}", timestamp_ms(record.get("timestamp")),
                                   "UserMessage" if is_user else "AgentMessage")
                if msg:
                    legacy.append(msg)
    return list(messages.values()) if any(msg.role == "prompt" for msg in messages.values()) else legacy


def legacy_threads(home):
    titles = {}
    index = home / "session_index.jsonl"
    if index.is_file():
        with index.open(encoding="utf-8") as stream:
            for line in stream:
                try:
                    row = json.loads(line)
                    titles[row["id"]] = row.get("thread_name")
                except (ValueError, KeyError, TypeError):
                    continue
    for folder in ("sessions", "archived_sessions"):
        for path in sorted((home / folder).rglob("rollout-*.jsonl")):
            try:
                with path.open("rb") as stream:
                    record = json.loads(stream.readline())
                metadata = record["payload"]
                thread_id = metadata["id"]
            except (ValueError, KeyError, TypeError):
                continue
            source = metadata.get("source")
            if record.get("type") != "session_meta" or metadata.get("agent_role"):
                continue
            if metadata.get("thread_source") in {"subagent", "guardian_review"} or (isinstance(source, dict) and "subagent" in source):
                continue
            started = timestamp_ms(metadata.get("timestamp") or record.get("timestamp"))
            yield {"id": thread_id, "name": titles.get(thread_id), "title": None,
                   "created_at": started // 1000 if started is not None else int(path.stat().st_mtime),
                   "rollout_path": str(path), "creator_account_id": metadata.get("creator_account_id"),
                   "creator_user_id": metadata.get("creator_user_id")}


def history(home, identity, sqlite_home):
    account, user = identity
    state = sqlite_home / "state_5.sqlite"
    history_db = sqlite_home / "thread_history_1.sqlite"
    records = []
    known_ids = set()
    if state.is_file():
        with closing(read_db(state)) as db:
            columns = {row["name"] for row in db.execute("PRAGMA table_info(threads)")}
            required = {"id", "name", "title", "created_at", "rollout_path", "creator_account_id", "creator_user_id", "thread_source"}
            if required <= columns:
                known_ids = {row["id"] for row in db.execute("SELECT id FROM threads")}
                records = list(db.execute("""
                    SELECT id, name, title, created_at, rollout_path, creator_account_id, creator_user_id
                    FROM threads WHERE coalesce(thread_source, '') NOT IN ('subagent', 'guardian_review')
                """))
    rollouts = {row["id"]: row for row in legacy_threads(home)}
    records.extend(row for ident, row in rollouts.items() if ident not in known_ids)
    if not records and not state.is_file():
        raise RuntimeError("No supported local Codex history found. Check CODEX_HOME and --sqlite-home.")
    owned = {(row["creator_account_id"], row["creator_user_id"]) for row in records
             if row["creator_account_id"] or row["creator_user_id"]}
    if not (account or user) and len(owned) > 1:
        raise RuntimeError("Multiple Codex users are present. Sign in to the user to archive first.")
    selected = {}
    for row in records:
        row_account, row_user = row["creator_account_id"], row["creator_user_id"]
        if (account and row_account and row_account != account) or (user and row_user and row_user != user):
            continue
        selected[row["id"]] = row

    messages = defaultdict(list)
    if history_db.is_file():
        with closing(read_db(history_db)) as db:
            rows = db.execute("""
                SELECT i.thread_id, i.item_id, i.created_at_ms, i.item_type, i.item_json
                FROM thread_items i JOIN thread_turns t
                  ON t.thread_id = i.thread_id AND t.turn_id = i.turn_id
                WHERE i.item_type IN ('userMessage', 'agentMessage')
                ORDER BY i.thread_id, t.rollout_ordinal, i.rollout_ordinal, i.created_at_ms, i.item_id
            """)
            for row in rows:
                if row["thread_id"] in selected:
                    message = make_message(json.loads(row["item_json"]), row["item_id"],
                                           row["created_at_ms"], row["item_type"])
                    if message:
                        messages[row["thread_id"]].append(message)

    missing_rollouts = 0
    for thread_id, row in selected.items():
        thread_messages = messages[thread_id]
        if not any(msg.role == "prompt" for msg in thread_messages):
            path = Path(row["rollout_path"]).resolve() if row["rollout_path"] else None
            if (not path or not path.is_file()) and thread_id in rollouts:
                path = Path(rollouts[thread_id]["rollout_path"]).resolve()
            if path and path.is_relative_to(home) and path.is_file():
                thread_messages = read_rollout(path)
            else:
                missing_rollouts += 1
        if any(msg.role == "prompt" for msg in thread_messages):
            yield row, thread_messages
    if missing_rollouts:
        print(f"Skipped {missing_rollouts} local thread(s) with no stored prompts or accessible rollout.", file=sys.stderr)


def display_title(row):
    return " ".join((row["name"] or row["title"] or "Untitled session").split())


def render(row, messages, zone, platform):
    title = display_title(row)
    created = datetime.fromtimestamp(row["created_at"], zone)
    parts = [f"# {title}\n\n<!-- codex-thread: {row['id']} -->\n\n"
             f"- Created: {created.isoformat(timespec='minutes')}\n- Tags: {platform}\n"]
    for message in messages:
        time = ""
        if message.timestamp:
            stamp = datetime.fromtimestamp(message.timestamp / 1000, zone)
            time = f" · {stamp:%Y-%m-%d %H:%M}"
        parts.append(f"<!-- codex-message: {message.role} {message.id} -->\n"
                     f"## {ROLE_LABELS[message.role]}{time}\n\n{message.text.rstrip()}\n")
    return "\n".join(parts)


def message_records(markdown):
    matches = list(MESSAGE_MARKER.finditer(markdown))
    records = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
        records[(match[1], match[2])] = markdown[match.start():end].rstrip()
    return records


def changes(old, new):
    before, after = message_records(old), message_records(new)
    added = Counter(role for role, _ in after.keys() - before.keys())
    parts = [f"+{count} {role}{'s' if count != 1 else ''}"
             for role in ROLE_LABELS if (count := added[role])]
    revised = sum(before[key] != after[key] for key in before.keys() & after.keys())
    if revised:
        parts.append(f"{revised} revised message{'s' if revised != 1 else ''}")
    if old and old.splitlines()[0] != new.splitlines()[0]:
        parts.append("title updated")
    return ", ".join(parts) or "metadata updated"


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(content)
    temp.replace(path)


def snapshot(home, destination, identity, zone, sqlite_home):
    sessions = destination / "sessions"
    existing = {}
    for path in sessions.rglob("*.md"):
        content = path.read_text(encoding="utf-8")
        marker = THREAD_MARKER.search(content)
        if marker:
            existing[marker[1]] = (path, content)
    updates = []
    for row, messages in list(history(home, identity, sqlite_home)):
        title = display_title(row)
        path, old = existing.get(row["id"], (None, ""))
        if path is None:
            month = datetime.fromtimestamp(row["created_at"], zone).strftime("%Y/%m")
            slug = re.sub(r"[^\w]+", "-", title.lower()).strip("-_")[:55] or "session"
            path = sessions / month / f"{slug}--{digest(row['id'])}.md"
        old_tag = re.search(r"(?m)^- Tags: (.+)$", old.split("<!-- codex-message:", 1)[0])
        new = render(row, messages, zone, old_tag[1] if old_tag else PLATFORM_TAG)
        if old and message_records(old).keys() - message_records(new).keys():
            print(f"Preserved existing transcript with messages absent from this Mac ({digest(row['id'])}).")
            continue
        if new != old:
            updates.append((path, new))
    for path, content in updates:
        atomic_write(path, content)
    return len(updates)


def command(args, cwd=None, capture=False):
    return subprocess.run(args, cwd=cwd, check=True, encoding="utf-8", capture_output=capture).stdout


def stage_changes(git, repo):
    if not (repo / "sessions").exists():
        return []
    command(git + ["add", "--", "sessions"], cwd=repo)
    output = command(git + ["diff", "--cached", "--name-only", "--diff-filter=AM", "-z", "--", "sessions"],
                     cwd=repo, capture=True)
    summaries = []
    for path in filter(None, output.split("\0")):
        old = subprocess.run(git + ["show", f"HEAD:{path}"], cwd=repo, encoding="utf-8", capture_output=True).stdout
        new = (repo / path).read_text(encoding="utf-8")
        title = new.splitlines()[0][2:]
        summaries.append(f"{title} · {'new session, ' if not old else ''}{changes(old, new)}")
    return sorted(summaries)


def sync(home, profile, sqlite_home):
    gh, git_path = shutil.which("gh"), shutil.which("git")
    if not gh or not git_path:
        raise RuntimeError("Git and GitHub CLI must both be on PATH.")
    target = json.loads(command([gh, "repo", "view", profile.repository, "--json",
                                 "visibility,defaultBranchRef"], capture=True))
    if target.get("visibility") != "PRIVATE":
        raise RuntimeError("Choose a private GitHub repository.")
    branch = (target.get("defaultBranchRef") or {}).get("name")
    if not branch:
        raise RuntimeError("Initialize the GitHub repository with a default branch.")
    viewer = json.loads(command([gh, "api", "user", "--jq", "{id, login}"], capture=True))
    login = viewer["login"]
    email = f"{viewer['id']}+{login}@users.noreply.github.com"
    helper = shlex.quote(Path(gh).as_posix())
    git = [git_path, "-c", "core.autocrlf=false", "-c", "credential.helper=", "-c", f"credential.helper=!{helper} auth git-credential",
           "-c", f"user.name={login}", "-c", f"user.email={email}"]
    repo = profile.state / "checkout"
    if not (repo / ".git").is_dir():
        command(git + ["clone", "--branch", branch, profile.origin, str(repo)])
    origin = command(git + ["remote", "get-url", "origin"], cwd=repo, capture=True).strip()
    if origin != profile.origin:
        raise RuntimeError("The archive checkout points to a different repository.")
    command(git + ["pull", "--rebase", "--autostash", "origin", branch], cwd=repo)
    identity_path = profile.state / "identity.json"
    if identity_path.exists():
        identity = json.loads(identity_path.read_text(encoding="utf-8"))
    else:
        identity = current_identity(home)
        if any(identity):
            atomic_write(identity_path, json.dumps(identity))
    snapshot(home, repo, identity, profile.zone, sqlite_home)
    summaries = stage_changes(git, repo)
    if summaries:
        date = datetime.now(profile.zone).date().isoformat()
        body = "\n".join(f"- {line}" for line in summaries)
        command(git + ["commit", "-m", f"[{PLATFORM_TAG}] Codex sessions · {date}", "-m", body], cwd=repo)
    command(git + ["push", "origin", f"HEAD:refs/heads/{branch}"], cwd=repo)
    print(f"{len(summaries)} session files updated.")


def install(home, profile, sqlite_home):
    if sys.platform != "darwin":
        raise RuntimeError("The scheduler installation requires macOS.")
    script = profile.state / Path(__file__).name
    if Path(__file__).resolve() != script.resolve():
        shutil.copyfile(__file__, script)
    config = profile.state / "profile.json"
    atomic_write(config, json.dumps(asdict(profile)))
    sync(home, profile, sqlite_home)
    agents = HOME / "Library/LaunchAgents"
    agents.mkdir(parents=True, exist_ok=True)
    plist = agents / f"{profile.label}.plist"
    hour, minute = (int(part) for part in profile.run_at.split(":"))
    log = profile.state / "archive.log"
    plist.write_bytes(plistlib.dumps({
        "Label": profile.label,
        "ProgramArguments": [sys.executable, str(script), "sync", "--codex-home", str(home),
                             "--profile", str(config), "--sqlite-home", str(sqlite_home)],
        "StartCalendarInterval": {"Hour": hour, "Minute": minute},
        "RunAtLoad": True,
        "EnvironmentVariables": {"PATH": "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin",
                                 "GIT_TERMINAL_PROMPT": "0", "GH_PROMPT_DISABLED": "1"},
        "StandardOutPath": str(log),
        "StandardErrorPath": str(log),
    }))
    domain = f"gui/{os.getuid()}"
    launchctl = "/bin/launchctl"
    service = f"{domain}/{profile.label}"
    existing = subprocess.run([launchctl, "print", service], capture_output=True)
    if existing.returncode == 0:
        command([launchctl, "bootout", service])
    command([launchctl, "bootstrap", domain, str(plist)])
    print(f"Daily archive installed for {profile.run_at} Mac local time.\nService: {service}\nLog: {log}")


@contextmanager
def sync_lock(path):
    with path.open("a+b") as lock:
        if os.name == "nt":
            import msvcrt

            lock.seek(0, os.SEEK_END)
            if not lock.tell():
                lock.write(b"\0")
                lock.flush()
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("snapshot", "sync", "install"))
    parser.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME", HOME / ".codex")))
    parser.add_argument("--sqlite-home", type=Path, help="Override the Codex history database directory")
    parser.add_argument("--output", type=Path, help="Local destination for snapshot mode")
    parser.add_argument("--profile", type=Path, help="JSON profile for repository, timezone, and daily run time")
    args = parser.parse_args()
    home = args.codex_home.expanduser().resolve()
    sqlite_home = (args.sqlite_home or Path(os.environ.get("CODEX_SQLITE_HOME", home))).expanduser().resolve()
    profile = load_profile(args.profile)
    if args.action == "snapshot":
        if args.output is None:
            parser.error("snapshot requires --output")
        result = snapshot(home, args.output.resolve(), current_identity(home), profile.zone, sqlite_home)
        print(f"{result} session files updated.")
        return
    if not profile.repository:
        parser.error("sync and install require a repository in --profile")
    if args.action == "install" and sys.platform != "darwin":
        parser.error("install is for macOS. Use sync for a manual backup on Linux or Windows.")
    profile.state.mkdir(parents=True, exist_ok=True)
    with sync_lock(profile.state / "sync.lock"):
        if args.action == "install":
            install(home, profile, sqlite_home)
        else:
            sync(home, profile, sqlite_home)


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, ValueError, sqlite3.Error, subprocess.CalledProcessError) as error:
        sys.exit(f"Codex archive failed: {error}")
