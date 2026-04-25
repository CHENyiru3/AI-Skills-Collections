#!/usr/bin/env python3
"""
migrate_skills.py

Physically moves skill folders from old paths to canonical skills-market/ paths.

Usage:
    python scripts/migrate_skills.py --dry-run     # preview moves
    python scripts/migrate_skills.py --apply        # execute moves
    python scripts/migrate_skills.py --validate     # check state after migration
    python scripts/migrate_skills.py --rollback     # undo last --apply run

Migration manifest is written to registry/migration-log.yaml after each --apply run.
"""

import argparse
import shutil
import sys
import yaml
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_SKILLS = ROOT / "registry" / "skills.yaml"
MIGRATION_LOG = ROOT / "registry" / "migration-log.yaml"


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def save_yaml(path, data):
    with open(path, "w") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)


def get_source(skill_id, meta):
    """Find the existing source path for a skill (first old_path that exists)."""
    for old in meta.get("old_paths", []):
        candidate = ROOT / old
        if candidate.exists():
            return candidate
    return None


def plan_migration(skills):
    """Build a list of (skill_id, source, destination) tuples to migrate."""
    moves = []
    conflicts = []
    missing = []

    for sid, meta in skills.items():
        status = meta.get("status", "active")
        if status == "missing":
            missing.append(sid)
            continue

        source = get_source(sid, meta)
        if source is None:
            missing.append(sid)
            continue

        dest = ROOT / meta["canonical_path"]
        if dest.exists():
            # Already migrated or manually placed
            if dest != source:
                conflicts.append((sid, source, dest, "already_exists"))
            continue

        moves.append((sid, source, dest))

    return moves, conflicts, missing


def dry_run(moves, conflicts, missing, skills):
    print("=== Migration Dry Run ===\n")
    print(f"Skills to move: {len(moves)}")
    for sid, src, dst in moves:
        print(f"  [move] {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")

    if conflicts:
        print(f"\nAlready migrated (skipping): {len(conflicts)}")
        for sid, src, dst, reason in conflicts:
            print(f"  [skip] {src.relative_to(ROOT)} -> already at {dst.relative_to(ROOT)}")

    if missing:
        print(f"\nMissing source (cannot migrate): {len(missing)}")
        for sid in missing:
            meta = skills.get(sid, {})
            status = meta.get("status", "active")
            if status == "missing":
                print(f"  [missing-skipped] {sid} (status=missing)")
            else:
                old = meta.get("old_paths", [])
                print(f"  [not-found] {sid} — expected at {old}")


def apply_migration(moves, skills):
    """Execute the migration moves."""
    print(f"=== Applying Migration ({len(moves)} moves) ===\n")

    log_entries = []
    succeeded = []
    failed = []

    for sid, src, dst in moves:
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            print(f"  [moved] {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
            succeeded.append({"skill_id": sid, "from": str(src.relative_to(ROOT)), "to": str(dst.relative_to(ROOT))})
        except Exception as e:
            print(f"  [FAILED] {sid}: {e}")
            failed.append({"skill_id": sid, "from": str(src.relative_to(ROOT)), "error": str(e)})

    log = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total_moves": len(moves),
        "succeeded": succeeded,
        "failed": failed,
    }
    save_yaml(MIGRATION_LOG, log)
    print(f"\nMigration log written to {MIGRATION_LOG}")

    if failed:
        print(f"\nWARNING: {len(failed)} moves failed:")
        for f in failed:
            print(f"  ✗ {f['skill_id']}: {f['error']}")
    else:
        print(f"\nAll {len(succeeded)} skills migrated successfully.")


def rollback():
    """Undo the last migration run."""
    print("=== Rollback ===\n")
    if not MIGRATION_LOG.exists():
        print("No migration log found. Nothing to rollback.")
        return

    log = load_yaml(MIGRATION_LOG)
    entries = log.get("succeeded", [])
    if not entries:
        print("No successful moves in last log to rollback.")
        return

    restored = []
    errors = []

    # Reverse in reverse order
    for entry in reversed(entries):
        src = ROOT / entry["to"]
        dst = ROOT / entry["from"]
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            print(f"  [restored] {entry['to']} -> {entry['from']}")
            restored.append(entry)
        except Exception as e:
            print(f"  [failed] {entry['skill_id']}: {e}")
            errors.append(entry)

    # Update log
    log["rollback_timestamp"] = datetime.utcnow().isoformat() + "Z"
    log["restored"] = restored
    log["rollback_errors"] = errors
    save_yaml(MIGRATION_LOG, log)

    print(f"\nRestored {len(restored)} skills. {len(errors)} errors.")


def validate_state():
    """Check the current state of the migration."""
    print("=== Migration State Validation ===\n")

    data = load_yaml(REGISTRY_SKILLS)
    skills = data.get("skills", {})

    canonical_exists = []
    canonical_missing = []
    already_migrated = []

    for sid, meta in skills.items():
        if meta.get("status") == "missing":
            continue
        canonical = ROOT / meta["canonical_path"]
        if canonical.exists():
            canonical_exists.append(sid)
            # Check if old paths still exist
            src = get_source(sid, meta)
            if src and src.exists() and src != canonical:
                already_migrated.append((sid, src, canonical))
        else:
            # Not migrated yet
            src = get_source(sid, meta)
            if src and src.exists():
                canonical_missing.append((sid, src, canonical))
            elif not src:
                # No old path found at all
                pass

    print(f"Skills at canonical path: {len(canonical_exists)}")
    print(f"Skills NOT yet migrated: {len(canonical_missing)}")

    if canonical_missing:
        print("\nPending migrations:")
        for sid, src, dst in canonical_missing[:10]:
            print(f"  [pending] {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
        if len(canonical_missing) > 10:
            print(f"  ... and {len(canonical_missing) - 10} more")

    if already_migrated:
        print("\nNote: old paths still exist alongside canonical (may need cleanup):")
        for sid, src, dst in already_migrated[:5]:
            print(f"  [duplicate] {src.relative_to(ROOT)} also exists")


def main():
    parser = argparse.ArgumentParser(description="Migrate skills from old paths to canonical skills-market/ paths")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Preview moves without executing")
    group.add_argument("--apply", action="store_true", help="Execute the migration")
    group.add_argument("--validate", action="store_true", help="Validate current migration state")
    group.add_argument("--rollback", action="store_true", help="Rollback last --apply run")
    args = parser.parse_args()

    data = load_yaml(REGISTRY_SKILLS)
    skills = data.get("skills", {})
    moves, conflicts, missing = plan_migration(skills)

    if args.validate:
        validate_state()
        return

    if args.rollback:
        rollback()
        return

    if args.dry_run:
        dry_run(moves, conflicts, missing, skills)
        return

    if args.apply:
        apply_migration(moves, skills)
        return


if __name__ == "__main__":
    main()
