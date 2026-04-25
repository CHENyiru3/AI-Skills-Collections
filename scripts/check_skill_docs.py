#!/usr/bin/env python3
"""
check_skill_docs.py

Checks the health of all skill SKILL.md files.

For each active skill:
1. SKILL.md exists
2. Has required YAML frontmatter (name, description)
3. Has required content sections
4. No empty placeholder content
5. Registry entry points to a real canonical path under skills-market/

For each SKILL.md found in skills-market/ but NOT in registry:
- Warn (orphan file)

Usage:
    python scripts/check_skill_docs.py
    python scripts/check_skill_docs.py --fix   # attempt auto-fixes where safe
    python scripts/check_skill_docs.py --json    # machine-readable output
"""

import argparse
import json
import re
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_SKILLS = ROOT / "registry" / "skills.yaml"
SKILLS_MARKET = ROOT / "skills-market"

REQUIRED_FRONTMATTER = ["name", "description"]
MIN_CONTENT_WORDS = 10


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def parse_frontmatter(content):
    """Extract YAML frontmatter from a SKILL.md file. Returns (meta_dict, body_text)."""
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return {}, content
    try:
        meta = yaml.safe_load(match.group(1))
    except Exception:
        return {}, content
    body = content[match.end() :].strip()
    return (meta or {}), body


def check_skill_md(skill_path, sid):
    """Check a single SKILL.md file. Returns list of (severity, message)."""
    issues = []
    try:
        content = skill_path.read_text(encoding="utf-8")
    except Exception as e:
        issues.append(("ERROR", f"[{sid}] cannot read: {e}"))
        return issues

    meta, body = parse_frontmatter(content)

    # Check required frontmatter
    for field in REQUIRED_FRONTMATTER:
        if field not in meta:
            issues.append(("ERROR", f"[{sid}] missing frontmatter: {field}"))
        elif not meta[field]:
            issues.append(("ERROR", f"[{sid}] empty frontmatter: {field}"))

    # Check frontmatter has at least name and description
    if "name" not in meta or not meta["name"]:
        issues.append(("ERROR", f"[{sid}] missing or empty 'name' in frontmatter"))
    if "description" not in meta or not meta["description"]:
        issues.append(("ERROR", f"[{sid}] missing or empty 'description' in frontmatter"))

    # Check body is not empty
    words = len(body.split())
    if words < MIN_CONTENT_WORDS:
        issues.append(("WARNING", f"[{sid}] body has only {words} words (expected >={MIN_CONTENT_WORDS})"))

    # Check for empty placeholder indicators
    placeholder_patterns = [
        r"^todo",
        r"^placeholder",
        r"^fill this in",
        r"^replace this",
        r"^not yet implemented",
    ]
    for pat in placeholder_patterns:
        if re.search(pat, body[:200], re.IGNORECASE):
            issues.append(("WARNING", f"[{sid}] body appears to be a placeholder"))
            break

    return issues


def check_all():
    errors = []
    warnings = []

    # Load registry
    registry_data = load_yaml(REGISTRY_SKILLS)
    skills = registry_data.get("skills", {})

    # Build set of all known skill dirs from registry
    registry_skill_dirs = set()
    for sid, meta in skills.items():
        cp = meta.get("canonical_path", "")
        if cp.startswith("skills-market/"):
            registry_skill_dirs.add(cp[len("skills-market/") :])

    # Check every active skill in registry
    for sid, meta in sorted(skills.items()):
        if meta.get("status") == "missing":
            continue
        cp = meta.get("canonical_path", "")
        if not cp.startswith("skills-market/"):
            errors.append(("ERROR", f"[{sid}] canonical_path '{cp}' is not under skills-market/"))
            continue
        skill_dir = SKILLS_MARKET / cp[len("skills-market/") :]
        skill_md = skill_dir / "SKILL.md"

        if not skill_dir.exists():
            errors.append(("ERROR", f"[{sid}] canonical_path does not exist: {skill_dir}"))
            continue
        if not skill_md.exists():
            errors.append(("ERROR", f"[{sid}] SKILL.md missing in {skill_dir}"))
            continue

        issues = check_skill_md(skill_md, sid)
        for sev, msg in issues:
            if sev == "ERROR":
                errors.append((sev, msg))
            else:
                warnings.append((sev, msg))

    # Scan skills-market for orphan SKILL.md files (in registry but not registered)
    orphan_count = 0
    for skill_md in SKILLS_MARKET.rglob("SKILL.md"):
        rel = skill_md.parent.relative_to(SKILLS_MARKET)
        if str(rel) not in registry_skill_dirs:
            sid = rel.name
            issues = check_skill_md(skill_md, sid)
            for sev, msg in issues:
                if sev == "ERROR":
                    errors.append((sev, f"[orphan] {msg}"))
                else:
                    warnings.append((sev, f"[orphan] {msg}"))
            if not issues:
                warnings.append(("WARNING", f"[orphan] SKILL.md not in registry: {rel}"))
            orphan_count += 1

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Check skill SKILL.md quality")
    parser.add_argument("--json", action="store_true", help="Machine-readable JSON output")
    parser.add_argument("--fix", action="store_true", help="Auto-fix safe issues (not yet implemented)")
    args = parser.parse_args()

    errors, warnings = check_all()

    if args.json:
        output = {
            "errors": [{"severity": e, "message": m} for e, m in errors],
            "warnings": [{"severity": w, "message": m} for w, m in warnings],
            "summary": {
                "errors": len(errors),
                "warnings": len(warnings),
                "passed": len(errors) == 0,
            },
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
        return

    print("=== Skill Doc Health Check ===\n")

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for _, msg in errors:
            print(f"  ✗ {msg}")
        print()

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for _, msg in warnings:
            print(f"  ⚠ {msg}")
        print()

    if errors:
        print("FAILED — fix errors above")
        exit(1)
    elif warnings:
        print(f"PASSED (with {len(warnings)} warnings)")
        exit(0)
    else:
        print("PASSED — all skills healthy")
        exit(0)


if __name__ == "__main__":
    main()
