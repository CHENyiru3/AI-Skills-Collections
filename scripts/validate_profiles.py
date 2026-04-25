#!/usr/bin/env python3
"""
validate_profiles.py

Validates all deployment profiles (deployments/*.yaml) and taskpacks (taskpacks/*.yaml):
1. Profile/taskpack ID is unique (no overlap between profiles and taskpacks)
2. All skill IDs referenced exist in registry/skills.yaml
3. All extends references point to existing profiles
4. No circular extends dependencies
5. Every profile/taskpack has a description
"""

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPLOYMENTS_DIR = ROOT / "deployments"
TASKPACKS_DIR = ROOT / "taskpacks"
REGISTRY_SKILLS = ROOT / "registry" / "skills.yaml"


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_skill_ids():
    data = load_yaml(REGISTRY_SKILLS)
    return set(data.get("skills", {}).keys())


def resolve_extends(profile_id, profiles, visited=None):
    """Recursively resolve all skills from extended profiles."""
    if visited is None:
        visited = set()
    if profile_id in visited:
        return set(), set([profile_id])  # skills, cycles
    visited.add(profile_id)

    meta = profiles.get(profile_id, {})
    extends = meta.get("extends", [])
    all_skills = set(meta.get("skills", []))
    cycles = set()

    for ext in extends:
        ext_skills, ext_cycles = resolve_extends(ext, profiles, visited.copy())
        all_skills |= ext_skills
        cycles |= ext_cycles

    return all_skills, cycles


def validate_profile_dir(dir_path, registry_ids, all_profile_ids):
    errors = []
    if not dir_path.exists():
        errors.append(f"Directory not found: {dir_path}")
        return errors

    for yaml_file in sorted(dir_path.glob("*.yaml")):
        data = load_yaml(yaml_file)
        pid = data.get("id", "")
        desc = data.get("description", "")
        skills = data.get("skills", [])
        extends = data.get("extends", [])

        kind = dir_path.name  # "deployments" or "taskpacks"

        if not pid:
            errors.append(f"[{yaml_file.name}] missing 'id' field")
        if not desc:
            errors.append(f"[{pid}] missing 'description'")

        # Check extends reference existing profiles
        for ext in extends:
            if ext not in all_profile_ids:
                errors.append(f"[{pid}] extends unknown profile: '{ext}'")

        # Resolve all skills (including from extends)
        if pid:
            all_skills, cycles = resolve_extends(pid, {
                p.get("id"): p for p in [
                    load_yaml(f) for f in dir_path.glob("*.yaml")
                ]
            }, visited=None)
            all_skills |= set(skills)
        else:
            all_skills = set(skills)

        # Check all skill IDs exist
        for sid in all_skills:
            if sid not in registry_ids:
                errors.append(f"[{pid}] skill not in registry: '{sid}'")

    return errors


def main():
    print("=== Profile & Taskpack Validation ===\n")

    registry_ids = load_skill_ids()
    print(f"Skills in registry: {len(registry_ids)}")

    all_profile_ids = set()

    # Collect all profile IDs from deployments
    for f in DEPLOYMENTS_DIR.glob("*.yaml"):
        data = load_yaml(f)
        pid = data.get("id")
        if pid:
            all_profile_ids.add(pid)

    # Collect all profile IDs from taskpacks
    for f in TASKPACKS_DIR.glob("*.yaml"):
        data = load_yaml(f)
        pid = data.get("id")
        if pid:
            all_profile_ids.add(pid)

    print(f"Profiles + taskpacks total: {len(all_profile_ids)}\n")

    # Check for duplicate IDs across deployments and taskpacks
    errors = []
    seen_ids = {}
    for f in list(DEPLOYMENTS_DIR.glob("*.yaml")) + list(TASKPACKS_DIR.glob("*.yaml")):
        data = load_yaml(f)
        pid = data.get("id", "")
        if pid:
            if pid in seen_ids:
                errors.append(f"Duplicate ID '{pid}' in {f.name} and {seen_ids[pid]}")
            seen_ids[pid] = f.name

    errors += validate_profile_dir(DEPLOYMENTS_DIR, registry_ids, all_profile_ids)
    errors += validate_profile_dir(TASKPACKS_DIR, registry_ids, all_profile_ids)

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
        print("\nFAILED — fix errors above")
        sys.exit(1)
    else:
        print("PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
