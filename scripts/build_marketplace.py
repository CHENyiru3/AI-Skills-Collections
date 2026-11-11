#!/usr/bin/env python3
"""
build_marketplace.py

Generates .claude-plugin/marketplace.json from registry/skills.yaml.

This ensures the marketplace always stays in sync with the registry.
Regenerate this file after any change to registry/skills.yaml.

Usage:
    python scripts/build_marketplace.py
    python scripts/build_marketplace.py --dry-run
    python scripts/build_marketplace.py --check

Importable functions:
    build_marketplace_data(skill_ids=None) -> dict
    write_marketplace_file(marketplace, path) -> int
"""

import argparse
import json
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_SKILLS = ROOT / "registry" / "skills.yaml"
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"

# Map from domain to plugin definition
PLUGIN_DEFINITIONS = {
    "documents": {
        "name": "documents",
        "description": "Document processing — OfficeCLI, Excel, Word, PowerPoint, PDF, web design, and collaboration",
        "source_prefix": "./skills-market/documents",
        "subdirs": ["office", "formats", "design", "collaboration", "media"],
    },
    "programming": {
        "name": "programming",
        "description": "Python library development — project setup, testing, packaging, performance, security, API design",
        "source_prefix": "./skills-market/programming",
        "subdirs": ["python"],
    },
    "ai-ml": {
        "name": "ai-ml",
        "description": "AI/ML — VI methodology, PyTorch, Transformers, PEFT, TRL, distributed training",
        "source_prefix": "./skills-market/ai-ml",
        "subdirs": ["deep-learning", "llm", "training", "theory", "utility"],
    },
    "compbio": {
        "name": "compbio",
        "description": "Computational biology — perturbation analysis, single-cell, spatial omics, databases, project continuity",
        "source_prefix": "./skills-market/compbio",
        "subdirs": ["single-cell", "spatial-omics", "multiomics", "databases", "workflows", "expert-workflows"],
    },
    "writing": {
        "name": "writing",
        "description": "Academic writing, literature review, Marp presentations, LaTeX, Obsidian, and knowledge management",
        "source_prefix": "./skills-market/writing",
        "subdirs": ["academic", "literature", "presentations", "latex", "obsidian"],
    },
    "agents": {
        "name": "agents",
        "description": "Coding agents — Claude Code, Codex, MCP, handoffs, engineering guidelines",
        "source_prefix": "./skills-market/agents",
        "subdirs": ["claude-code", "codex", "mcp", "guidelines", "workflows", "ag-ui"],
    },
    "frontend": {
        "name": "frontend",
        "description": "Website maintenance — page keeper and academic site maintenance",
        "source_prefix": "./skills-market/frontend",
        "subdirs": ["site-maintenance"],
    },
    "platforms": {
        "name": "platforms",
        "description": "Platform integrations — GitHub workflows and Google Workspace CLI/Drive transfers",
        "source_prefix": "./skills-market/platforms",
        "subdirs": ["github", "google-workspace", "gitlab", "huggingface", "zotero"],
    },
    "core": {
        "name": "core",
        "description": "Core utilities — skill authoring, security, scientific ideation and coding governance",
        "source_prefix": "./skills-market/core",
        "subdirs": ["dev", "security", "performance", "research"],
    },
    "projects": {
        "name": "projects",
        "description": "Project-specific skill bundles",
        "source_prefix": "./skills-market/projects",
        "subdirs": [],
    },
}


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def build_plugin(plugin_def, skills):
    """Build a single plugin entry from skills in that domain."""
    domain = plugin_def["name"]  # same as domain key here
    prefix = plugin_def["source_prefix"]

    # Collect all active skills for this domain
    domain_skills = []
    for sid, meta in sorted(skills.items()):
        if meta.get("domain") != domain:
            continue
        if meta.get("status") == "missing":
            continue

        # Component paths are relative to the plugin source, not skills-market/.
        plugin_root = (ROOT / prefix).resolve()
        skill_root = (ROOT / meta["canonical_path"]).resolve()
        if not plugin_root.is_relative_to(ROOT.resolve()):
            raise ValueError(f"Plugin source escapes the repository: {prefix}")
        if not skill_root.is_relative_to(plugin_root):
            raise ValueError(f"[{sid}] skill path is outside plugin source {prefix}")
        if not (skill_root / "SKILL.md").is_file():
            raise ValueError(f"[{sid}] SKILL.md missing at {skill_root}")
        rel = skill_root.relative_to(plugin_root).as_posix()
        domain_skills.append(f"./{rel}")

    return {
        "name": plugin_def["name"],
        "description": plugin_def["description"],
        "source": prefix,
        "strict": False,
        "skills": sorted(domain_skills),
    }


def build_marketplace_data(skill_ids=None):
    """Build the marketplace dict from registry.

    Args:
        skill_ids: Optional set of skill IDs to include.
            When None, all active skills are included.

    Returns:
        dict: The marketplace structure ready for JSON serialization.
    """
    data = load_yaml(REGISTRY_SKILLS)
    skills = data.get("skills", {})

    # Filter out missing skills for marketplace
    active_skills = {sid: meta for sid, meta in skills.items() if meta.get("status") != "missing"}

    # If filtering by specific skill IDs, reduce the set
    if skill_ids is not None:
        active_skills = {sid: meta for sid, meta in active_skills.items() if sid in skill_ids}

    # Build plugins for each known domain
    plugins = []
    for domain, plugin_def in PLUGIN_DEFINITIONS.items():
        plugin = build_plugin(plugin_def, active_skills)
        if plugin["skills"]:  # only include plugins that have skills
            plugins.append(plugin)

    # Check for skills in unknown domains
    known_domains = set(PLUGIN_DEFINITIONS.keys())
    unknown_domain_skills = []
    for sid, meta in active_skills.items():
        if meta.get("domain") not in known_domains:
            cp = meta.get("canonical_path", "")
            unknown_domain_skills.append((sid, meta.get("domain", "?"), cp))

    if unknown_domain_skills:
        print(f"WARNING: {len(unknown_domain_skills)} skills in unknown domains:")
        for sid, dom, cp in unknown_domain_skills:
            print(f"  [{sid}] domain={dom} path={cp}")
        print("Add to PLUGIN_DEFINITIONS in build_marketplace.py\n")

    marketplace = {
        "name": "ai-skills",
        "owner": {
            "name": "Eric Yiru",
            "email": "contact@example.com",
        },
        "metadata": {
            "description": "AI agent skills for document workflows, website maintenance, Python library development, AI/ML, computational biology, and writing",
            "version": "2.0.0",
        },
        "plugins": plugins,
    }

    return marketplace


def write_marketplace_file(marketplace, path):
    """Write marketplace dict to a JSON file.

    Args:
        marketplace: dict to serialize.
        path: Path to write to.

    Returns:
        int: Total number of skill references written.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    output = json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n"
    path.write_text(output)
    total_skills = sum(len(p["skills"]) for p in marketplace["plugins"])
    print(f"Written {path.name}: {len(marketplace['plugins'])} plugins, {total_skills} skill references")
    return total_skills


def main():
    parser = argparse.ArgumentParser(description="Generate marketplace.json from registry/skills.yaml")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing file")
    parser.add_argument("--check", action="store_true", help="Check source paths and generated-file agreement without writing")
    args = parser.parse_args()

    marketplace = build_marketplace_data()

    output = json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n"

    if args.check:
        if not MARKETPLACE_PATH.is_file() or MARKETPLACE_PATH.read_text() != output:
            parser.exit(1, "Marketplace differs from registry; run scripts/build_marketplace.py\n")
        print("PASSED — marketplace paths exist inside their plugin roots and match the registry")
        return

    if args.dry_run:
        print(output)
        print(f"(dry run — not written to {MARKETPLACE_PATH})")
        return

    write_marketplace_file(marketplace, MARKETPLACE_PATH)


if __name__ == "__main__":
    main()
