#!/usr/bin/env python3
"""
resolve_alias.py

Resolve a skill ID or legacy path to its canonical information.

Usage:
    python scripts/resolve_alias.py scanpy
    python scripts/resolve_alias.py compbio-skills/single-cell/analysis/scanpy
    python scripts/resolve_alias.py --json scanpy
"""

import argparse
import json
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_SKILLS = ROOT / "registry" / "skills.yaml"
ALIASES_FILE = ROOT / "registry" / "aliases.yaml"


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def resolve(query):
    """
    Resolve a query (skill ID or legacy path) to skill metadata.
    Returns (result_dict, resolution_type) or (None, None) if not found.
    """
    skills = load_yaml(REGISTRY_SKILLS).get("skills", {})
    aliases = load_yaml(ALIASES_FILE).get("aliases", {})

    # Direct skill ID lookup
    if query in skills:
        meta = skills[query]
        return {"id": query, **meta}, "skill_id"

    # Alias lookup: old path -> skill ID -> metadata
    if query in aliases:
        skill_id = aliases[query]
        if skill_id in skills:
            meta = skills[skill_id]
            return {"id": skill_id, **meta, "resolved_from_alias": query}, "alias"
        else:
            return {"id": skill_id, "status": "missing", "error": f"skill '{skill_id}' not in registry"}, "broken_alias"

    # Check if query looks like an old path (try matching old_paths in each skill)
    for sid, meta in skills.items():
        if query in meta.get("old_paths", []):
            return {"id": sid, **meta, "resolved_from_old_path": query}, "old_path"

    return None, "not_found"


def main():
    parser = argparse.ArgumentParser(description="Resolve skill ID or legacy path")
    parser.add_argument("query", nargs="?", help="Skill ID or legacy path to resolve")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if not args.query:
        print("Usage: resolve_alias.py <skill-id-or-old-path>")
        print("\nExample skill IDs: scanpy, pytorch, latex-writing, zotpilot")
        print("Example old paths: compbio-skills/single-cell/analysis/scanpy, python-skills/project-setup")
        return

    result, rtype = resolve(args.query)

    if result is None:
        print(f"Not found: '{args.query}'")
        return

    if args.json:
        result["resolution_type"] = rtype
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    # Human-readable output
    print(f"=== Resolution: '{args.query}' ===")
    print(f"Type: {rtype}")
    print(f"Skill ID: {result['id']}")
    print(f"Name: {result.get('name', 'N/A')}")
    print(f"Status: {result.get('status', 'active')}")
    print(f"Domain: {result.get('domain', 'N/A')}")
    print(f"Canonical path: {result.get('canonical_path', 'N/A')}")

    old_paths = result.get("old_paths", [])
    if old_paths:
        print(f"Old paths: {', '.join(old_paths)}")

    if "resolved_from_alias" in result:
        print(f"(resolved from alias: {result['resolved_from_alias']})")
    if "resolved_from_old_path" in result:
        print(f"(matched old_path: {result['resolved_from_old_path']})")

    tags = result.get("tags", [])
    if tags:
        print(f"Tags: {', '.join(tags)}")


if __name__ == "__main__":
    main()
