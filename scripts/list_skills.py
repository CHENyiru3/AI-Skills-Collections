#!/usr/bin/env python3
"""
list_skills.py

List skills from the registry with optional filtering.

Usage:
    python scripts/list_skills.py                    # list all
    python scripts/list_skills.py --domain compbio   # filter by domain
    python scripts/list_skills.py --status missing   # filter by status
    python scripts/list_skills.py --tag single-cell  # filter by tag
    python scripts/list_skills.py --profile research-server  # skills in profile
    python scripts/list_skills.py --taskpack single-cell-analysis
    python scripts/list_skills.py --domain ai-ml --format json
"""

import argparse
import json
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_SKILLS = ROOT / "registry" / "skills.yaml"
DEPLOYMENTS_DIR = ROOT / "deployments"
TASKPACKS_DIR = ROOT / "taskpacks"


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def resolve_extended_skills(profile_id, profiles_cache):
    """Resolve skills from a profile including all extended profiles."""
    data = profiles_cache.get(profile_id, {})
    extends = data.get("extends", [])
    skills = set(data.get("skills", []))
    for ext in extends:
        skills |= resolve_extended_skills(ext, profiles_cache)
    return skills


def main():
    parser = argparse.ArgumentParser(description="List skills from registry")
    parser.add_argument("--domain", help="Filter by domain (e.g. compbio, ai-ml)")
    parser.add_argument("--status", help="Filter by status (e.g. missing, active)")
    parser.add_argument("--tag", help="Filter by tag (substring match)")
    parser.add_argument("--profile", help="List skills in a deployment profile")
    parser.add_argument("--taskpack", help="List skills in a taskpack")
    parser.add_argument("--format", choices=["table", "json", "ids"], default="table")
    args = parser.parse_args()

    data = load_yaml(REGISTRY_SKILLS)
    skills = data.get("skills", {})

    # If filtering by profile, resolve skills from that profile
    profile_skills_filter = None
    if args.profile:
        profiles = {f.stem: load_yaml(f) for f in DEPLOYMENTS_DIR.glob("*.yaml")}
        profile_skills_filter = resolve_extended_skills(args.profile, profiles)
        if profile_skills_filter is not None and not profile_skills_filter:
            print(f"No such profile: {args.profile}")
            return

    # If filtering by taskpack, resolve skills from that taskpack
    taskpack_skills_filter = None
    if args.taskpack:
        taskpacks = {f.stem: load_yaml(f) for f in TASKPACKS_DIR.glob("*.yaml")}
        tp = taskpacks.get(args.taskpack)
        if not tp:
            print(f"No such taskpack: {args.taskpack}")
            return
        taskpack_skills_filter = set(tp.get("skills", []))

    filtered = []
    for sid, meta in sorted(skills.items()):
        if args.domain and meta.get("domain") != args.domain:
            continue
        if args.status and meta.get("status") != args.status:
            continue
        if args.tag:
            tags = meta.get("tags", [])
            if args.tag not in tags:
                continue
        if profile_skills_filter is not None and sid not in profile_skills_filter:
            continue
        if taskpack_skills_filter is not None and sid not in taskpack_skills_filter:
            continue

        filtered.append((sid, meta))

    # Output
    if args.format == "ids":
        for sid, _ in filtered:
            print(sid)
    elif args.format == "json":
        output = [{"id": sid, **meta} for sid, meta in filtered]
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        # Table format
        print(f"{'ID':<40} {'DOMAIN':<12} {'STATUS':<12} {'CANONICAL PATH'}")
        print("-" * 120)
        for sid, meta in filtered:
            print(f"{sid:<40} {meta.get('domain',''):<12} {meta.get('status','active'):<12} {meta.get('canonical_path','')}")
        print(f"\n{len(filtered)} skills")

    if args.profile:
        print(f"\nProfile '{args.profile}' includes {len(profile_skills_filter)} unique skills")
    if args.taskpack:
        print(f"\nTaskpack '{args.taskpack}' includes {len(taskpack_skills_filter)} unique skills")


if __name__ == "__main__":
    main()
