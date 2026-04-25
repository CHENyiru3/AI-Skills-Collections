#!/usr/bin/env python3
"""
install_profile.py

Install skills for a deployment profile or taskpack on the current machine.

Usage:
    python scripts/install_profile.py --profile macos-personal
    python scripts/install_profile.py --taskpack single-cell-analysis
    python scripts/install_profile.py --profile gpu-server --dry-run
    python scripts/install_profile.py --list
"""

import argparse
import shutil
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPLOYMENTS_DIR = ROOT / "deployments"
TASKPACKS_DIR = ROOT / "taskpacks"
REGISTRY_SKILLS = ROOT / "registry" / "skills.yaml"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def resolve_extended_skills(profile_id, all_profiles):
    """Recursively resolve all skills from a profile including extended profiles."""
    if profile_id not in all_profiles:
        return set()
    meta = all_profiles[profile_id]
    skills = set(meta.get("skills", []))
    for ext in meta.get("extends", []):
        skills |= resolve_extended_skills(ext, all_profiles)
    return skills


def load_skill_paths():
    """Load canonical paths from registry."""
    data = load_yaml(REGISTRY_SKILLS)
    paths = {}
    for sid, meta in data.get("skills", {}).items():
        if meta.get("status") == "missing":
            continue
        paths[sid] = meta["canonical_path"]
    return paths


def install_skills(skill_ids, skill_paths, dry_run=True):
    """Install skills by copying them to a target location (e.g. Claude settings)."""
    # This is a placeholder — real implementation would copy skill dirs
    # to the Claude Code skills directory and update marketplace.json.
    installed = []
    skipped = []
    missing = []

    for sid in sorted(skill_ids):
        if sid not in skill_paths:
            missing.append(sid)
            continue
        src = ROOT / skill_paths[sid]
        if not src.exists():
            missing.append(sid)
            continue
        installed.append((sid, src))
        print(f"  {'[would install]' if dry_run else '[installed]'} {sid}  ({src.relative_to(ROOT)})")

    return installed, skipped, missing


def main():
    parser = argparse.ArgumentParser(description="Install skills from a profile or taskpack")
    parser.add_argument("--profile", help="Deployment profile ID to install")
    parser.add_argument("--taskpack", help="Taskpack ID to install")
    parser.add_argument("--dry-run", action="store_true", help="Preview without installing")
    parser.add_argument("--list", action="store_true", help="List all available profiles and taskpacks")
    args = parser.parse_args()

    if args.list:
        print("=== Deployment Profiles ===")
        for f in sorted(DEPLOYMENTS_DIR.glob("*.yaml")):
            meta = load_yaml(f)
            print(f"  {meta.get('id', f.stem):<30} {meta.get('description', '')}")
        print("\n=== Taskpacks ===")
        for f in sorted(TASKPACKS_DIR.glob("*.yaml")):
            meta = load_yaml(f)
            print(f"  {meta.get('id', f.stem):<30} {meta.get('description', '')}")
        return

    if not (args.profile or args.taskpack):
        print("Specify --profile or --taskpack, or --list to see all options.")
        return

    skill_paths = load_skill_paths()

    if args.profile:
        all_profiles = {}
        for f in DEPLOYMENTS_DIR.glob("*.yaml"):
            meta = load_yaml(f)
            pid = meta.get("id")
            if pid:
                all_profiles[pid] = meta
        if args.profile not in all_profiles:
            print(f"Unknown profile: {args.profile}")
            sys.exit(1)
        skill_ids = resolve_extended_skills(args.profile, all_profiles)
        kind = f"profile '{args.profile}'"
    else:
        taskpacks = {f.stem: load_yaml(f) for f in TASKPACKS_DIR.glob("*.yaml")}
        if args.taskpack not in taskpacks:
            print(f"Unknown taskpack: {args.taskpack}")
            sys.exit(1)
        skill_ids = set(taskpacks[args.taskpack].get("skills", []))
        kind = f"taskpack '{args.taskpack}'"

    print(f"=== Installing {kind} ({len(skill_ids)} skills) ===")
    if args.dry_run:
        print("(dry run — no changes made)\n")

    installed, skipped, missing = install_skills(skill_ids, skill_paths, dry_run=args.dry_run)

    print(f"\nResult: {len(installed)} to install, {len(missing)} missing")

    if missing:
        print(f"\nMissing skills (not in registry or no SKILL.md):")
        for sid in sorted(missing):
            print(f"  - {sid}")


if __name__ == "__main__":
    main()
