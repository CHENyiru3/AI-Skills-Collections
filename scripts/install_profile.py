#!/usr/bin/env python3
"""
install_profile.py

Install skills for a deployment profile or taskpack by filtering marketplace.json.
This controls which skills Claude Code loads when working in this repository.

Usage:
    python scripts/install_profile.py --profile macos-personal
    python scripts/install_profile.py --taskpack single-cell-analysis
    python scripts/install_profile.py --profile gpu-server --taskpack paper-writing
    python scripts/install_profile.py --dry-run --profile research-server
    python scripts/install_profile.py --reset
    python scripts/install_profile.py --list
"""

import argparse
import shutil
import sys
import yaml
from pathlib import Path

from build_marketplace import build_marketplace_data, write_marketplace_file, MARKETPLACE_PATH

ROOT = Path(__file__).resolve().parents[1]
DEPLOYMENTS_DIR = ROOT / "deployments"
TASKPACKS_DIR = ROOT / "taskpacks"
REGISTRY_SKILLS = ROOT / "registry" / "skills.yaml"
BACKUP_PATH = MARKETPLACE_PATH.with_suffix(".json.bak")


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


def backup_marketplace():
    """Copy current marketplace.json to .bak."""
    if MARKETPLACE_PATH.exists():
        shutil.copy2(MARKETPLACE_PATH, BACKUP_PATH)
        print(f"Backed up {MARKETPLACE_PATH.name} -> {BACKUP_PATH.name}")


def restore_marketplace():
    """Restore full marketplace from registry."""
    marketplace = build_marketplace_data()
    write_marketplace_file(marketplace, MARKETPLACE_PATH)
    return marketplace


def print_skill_summary(marketplace):
    """Print a summary of plugins and their skill counts."""
    total = 0
    for plugin in marketplace["plugins"]:
        count = len(plugin["skills"])
        total += count
        print(f"  {plugin['name']:<20} {count} skills")
    print(f"\nTotal: {total} skills across {len(marketplace['plugins'])} plugin groups")


def main():
    parser = argparse.ArgumentParser(
        description="Install skills from a profile or taskpack by filtering marketplace.json"
    )
    parser.add_argument("--profile", help="Deployment profile ID to install")
    parser.add_argument("--taskpack", help="Taskpack ID to install")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    parser.add_argument("--list", action="store_true", help="List all available profiles and taskpacks")
    parser.add_argument("--reset", action="store_true", help="Restore full marketplace (all skills)")
    args = parser.parse_args()

    # --list mode: print available profiles and taskpacks
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

    # --reset mode: restore full marketplace
    if args.reset:
        if args.dry_run:
            print("=== Dry run: would reset to full marketplace ===")
            marketplace = build_marketplace_data()
            print_skill_summary(marketplace)
            print("\n(would write full marketplace.json & backup current)")
            return

        print("=== Resetting to full marketplace ===")
        backup_marketplace()
        marketplace = restore_marketplace()
        print("\nRestored: all active skills")
        return

    # Must have --profile, --taskpack, or both
    if not (args.profile or args.taskpack):
        print("Specify --profile and/or --taskpack, or --list to see options, or --reset to restore full.")
        return

    # Resolve skill IDs
    combined_skills = set()
    kind_parts = []

    if args.profile:
        all_profiles = {}
        for f in DEPLOYMENTS_DIR.glob("*.yaml"):
            meta = load_yaml(f)
            pid = meta.get("id")
            if pid:
                all_profiles[pid] = meta
        if args.profile not in all_profiles:
            print(f"Unknown profile: {args.profile}")
            print("Available profiles:")
            for pid in sorted(all_profiles):
                print(f"  {pid}")
            sys.exit(1)
        profile_skills = resolve_extended_skills(args.profile, all_profiles)
        combined_skills |= profile_skills
        kind_parts = [f"profile '{args.profile}'"]

    if args.taskpack:
        taskpacks = {f.stem: load_yaml(f) for f in TASKPACKS_DIR.glob("*.yaml")}
        if args.taskpack not in taskpacks:
            print(f"Unknown taskpack: {args.taskpack}")
            print("Available taskpacks:")
            for tid in sorted(taskpacks):
                print(f"  {tid}")
            sys.exit(1)
        taskpack_skills = set(taskpacks[args.taskpack].get("skills", []))
        combined_skills |= taskpack_skills
        kind_parts.append(f"taskpack '{args.taskpack}'")

    kind = " + ".join(kind_parts)

    # Warn about any skill IDs not in the registry
    skill_paths = load_skill_paths()
    missing_ids = combined_skills - set(skill_paths.keys())
    if missing_ids:
        print(f"Warning: {len(missing_ids)} skill(s) in {kind} not found in registry:")
        for sid in sorted(missing_ids):
            print(f"  - {sid}")
        print()

    # Build filtered marketplace
    header = "=== Dry run:" if args.dry_run else "==="
    print(f"{header} Installing {kind} ({len(combined_skills)} skills) ===")

    if args.dry_run:
        print("(preview — no changes made)\n")
        marketplace = build_marketplace_data(skill_ids=combined_skills)
        print_skill_summary(marketplace)
        if MARKETPLACE_PATH.exists():
            print(f"\nBackup would be saved to: {BACKUP_PATH.name}")
        return

    # Real installation
    backup_marketplace()

    marketplace = build_marketplace_data(skill_ids=combined_skills)
    write_marketplace_file(marketplace, MARKETPLACE_PATH)

    print()
    print_skill_summary(marketplace)

    if missing_ids:
        print(f"\n(Note: {len(missing_ids)} missing skills not in registry — see warnings above)")


if __name__ == "__main__":
    main()
