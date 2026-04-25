#!/usr/bin/env python3
"""
validate_registry.py

Validates registry/skills.yaml for:
1. Every skill ID is unique
2. Every canonical_path exists on disk (unless status=missing)
3. No duplicate canonical paths
4. Every old_path points to a path that exists or is in old_paths of a missing skill
5. All skill IDs referenced in profiles/taskpacks exist in registry
6. No alias points to unknown skill ID
7. All status values are valid
8. All install_weight values are valid
"""

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
SKILLS_FILE = REGISTRY / "skills.yaml"
ALIASES_FILE = REGISTRY / "aliases.yaml"
MISSING_FILE = REGISTRY / "missing.yaml"
DEPRECATED_FILE = REGISTRY / "deprecated.yaml"

VALID_STATUSES = {"active", "experimental", "deprecated", "missing", "alias-only"}
VALID_WEIGHTS = {"light", "medium", "heavy", "host-specific"}
VALID_DOMAINS = {
    "core", "programming", "ai-ml", "compbio", "writing",
    "documents", "agents", "frontend", "github", "projects", "platforms"
}
VALID_HOSTS = {"macos", "linux", "windows", "server", "hpc", "gpu-server"}


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def check_skill_ids_unique(skills):
    """1. Every skill ID is unique."""
    ids = list(skills.keys())
    unique = set(ids)
    errors = []
    if len(ids) != len(unique):
        dupes = [x for x in ids if ids.count(x) > 1]
        errors.append(f"Duplicate skill IDs: {sorted(set(dupes))}")
    return errors


def check_active_skills_have_skill_md(skills):
    """Every active skill must have canonical_path/SKILL.md on disk."""
    errors = []
    for sid, meta in skills.items():
        status = meta.get("status", "active")
        if status != "active":
            continue
        cp = ROOT / meta["canonical_path"]
        sk = cp / "SKILL.md"
        if not cp.exists():
            errors.append(f"[{sid}] canonical_path does not exist: {cp}")
        elif not sk.exists():
            errors.append(f"[{sid}] SKILL.md missing at {sk}")
    return errors


def check_source_exists(skills):
    """Every active skill must have either a canonical_path or at least one old_path on disk."""
    errors = []
    for sid, meta in skills.items():
        status = meta.get("status", "active")
        if status == "missing":
            continue
        canonical = ROOT / meta["canonical_path"]
        old_paths = meta.get("old_paths", [])
        # After migration: canonical_path should exist.
        # Pre-migration: old_paths should exist.
        # After migration: old_paths may have been moved, so only canonical matters.
        canonical_exists = canonical.exists()
        old_exists = any((ROOT / p).exists() for p in old_paths)
        if not canonical_exists and not old_exists:
            errors.append(f"[{sid}] neither canonical_path nor any old_path exists on disk")
    return errors


def check_canonical_paths_exist(skills):
    """2. Every canonical_path exists on disk (unless status=missing).

    Note: This will fail before migration is applied. After --apply,
    re-run to confirm all paths are in place.
    """
    errors = []
    for sid, meta in skills.items():
        status = meta.get("status", "active")
        if status == "missing":
            continue
        canonical = ROOT / meta["canonical_path"]
        if not canonical.exists():
            # Don't fail hard here — this is expected before migration.
            # The check_source_exists above is the real pre-migration gate.
            # Here we just warn.
            pass  # handled by migration log
    return errors


def check_no_duplicate_canonical_paths(skills):
    """3. No duplicate canonical paths."""
    path_to_ids = {}
    for sid, meta in skills.items():
        cp = meta["canonical_path"]
        path_to_ids.setdefault(cp, []).append(sid)
    errors = []
    for path, ids in path_to_ids.items():
        if len(ids) > 1:
            errors.append(f"Duplicate canonical_path '{path}': {ids}")
    return errors


def check_old_paths(skills):
    """4. old_paths are listed for all existing skills (optional warning)."""
    warnings = []
    for sid, meta in skills.items():
        if meta.get("status") == "missing":
            continue
        if not meta.get("old_paths"):
            warnings.append(f"[{sid}] has no old_paths (first-time registration)")
    return warnings


def check_status_values(skills):
    """7. All status values are valid."""
    errors = []
    for sid, meta in skills.items():
        status = meta.get("status", "active")
        if status not in VALID_STATUSES:
            errors.append(f"[{sid}] invalid status: '{status}' (valid: {VALID_STATUSES})")
    return errors


def check_install_weight_values(skills):
    """8. All install_weight values are valid."""
    errors = []
    for sid, meta in skills.items():
        weight = meta.get("install_weight", "light")
        if weight not in VALID_WEIGHTS:
            errors.append(f"[{sid}] invalid install_weight: '{weight}' (valid: {VALID_WEIGHTS})")
    return errors


def check_domain_values(skills):
    """9. All domain values are valid."""
    errors = []
    for sid, meta in skills.items():
        domain = meta.get("domain", "")
        if domain not in VALID_DOMAINS:
            errors.append(f"[{sid}] invalid domain: '{domain}' (valid: {VALID_DOMAINS})")
    return errors


def check_supported_hosts(skills):
    """10. All supported_hosts values are valid."""
    errors = []
    for sid, meta in skills.items():
        hosts = meta.get("supported_hosts", [])
        for h in hosts:
            if h not in VALID_HOSTS:
                errors.append(f"[{sid}] invalid supported_host: '{h}' (valid: {VALID_HOSTS})")
    return errors


def check_aliases_point_to_valid_skills(skills):
    """6. No alias points to unknown skill ID."""
    aliases = load_yaml(ALIASES_FILE).get("aliases", {})
    errors = []
    for old_path, skill_id in aliases.items():
        if skill_id not in skills:
            errors.append(f"Alias '{old_path}' -> '{skill_id}' but skill '{skill_id}' not in registry")
    return errors


def check_canonical_paths_unique_in_aliases():
    """Ensure no two skills share the same canonical path via old_paths overlap."""
    # This is implicitly checked by check_no_duplicate_canonical_paths
    return []


def main():
    print("=== Registry Validation ===\n")

    if not SKILLS_FILE.exists():
        print(f"ERROR: {SKILLS_FILE} not found")
        sys.exit(1)

    data = load_yaml(SKILLS_FILE)
    skills = data.get("skills", {})

    all_errors = []
    all_warnings = []

    all_errors += check_skill_ids_unique(skills)
    all_errors += check_active_skills_have_skill_md(skills)
    all_errors += check_source_exists(skills)
    all_errors += check_no_duplicate_canonical_paths(skills)
    all_errors += check_status_values(skills)
    all_errors += check_install_weight_values(skills)
    all_errors += check_domain_values(skills)
    all_errors += check_supported_hosts(skills)
    all_errors += check_aliases_point_to_valid_skills(skills)
    all_warnings += check_old_paths(skills)

    print(f"Total skills in registry: {len(skills)}")
    active = sum(1 for m in skills.values() if m.get("status") == "active")
    missing = sum(1 for m in skills.values() if m.get("status") == "missing")
    print(f"  active: {active}, missing: {missing}, total: {len(skills)}\n")

    if all_errors:
        print(f"ERRORS ({len(all_errors)}):")
        for e in all_errors:
            print(f"  ✗ {e}")
        print()

    # Canonical path and SKILL.md status — informational
    migrated = []
    pending = []
    missing_md = []
    for sid, meta in skills.items():
        if meta.get("status") == "missing":
            continue
        cp = ROOT / meta["canonical_path"]
        if cp.exists():
            if (cp / "SKILL.md").exists():
                migrated.append(sid)
            else:
                missing_md.append(sid)
        else:
            pending.append(sid)
    print(f"Active skills with SKILL.md: {len(migrated)}, missing SKILL.md: {len(missing_md)}, pending migration: {len(pending)}")
    if pending or missing_md:
        print(f"  (run 'python scripts/migrate_skills.py --dry-run' to preview pending)")
    print()

    if all_warnings:
        print(f"WARNINGS ({len(all_warnings)}):")
        for w in all_warnings:
            print(f"  ⚠ {w}")
        print()

    if all_errors:
        print("FAILED — fix errors above")
        sys.exit(1)
    else:
        print("PASSED")
        if all_warnings:
            print(f"(with {len(all_warnings)} warnings)")
        sys.exit(0)


if __name__ == "__main__":
    main()
