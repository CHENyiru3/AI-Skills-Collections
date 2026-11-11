# Provenance and maintenance

## Snapshot

- Source requested by the user: [pertpy stable documentation](https://pertpy.scverse.org/en/stable/index.html).
- Retrieval date: **2026-10-08**.
- Release anchor: **pertpy 1.4.0**, checked through [version-specific PyPI metadata](https://pypi.org/pypi/pertpy/1.4.0/json) and its published `pertpy-1.4.0-py3-none-any.whl`.
- Method: focused manual distillation from 53 documentation pages (installation, changelog, tool APIs, and tutorials), with release-source inspection to resolve inconsistencies. Skill Seekers' source-to-skill workflow informed organization; its CLI was not installed or run.
- This is a curated workflow guide, not a mirrored manual. Local references contain the actionable material; linked APIs provide full parameter detail. No external MCP service is required to read the skill.
- Creation checks: skill validator passed; all local reference links resolved; 14 Python blocks compiled; 43 pertpy calls bound successfully to signatures extracted from the 1.4.0 release source. These are static checks, not execution of the statistical workflows.

## Source map

| Local reference | Primary documentation |
|---|---|
| [Setup and data](setup-data.md) | [Installation](https://pertpy.scverse.org/en/stable/installation.html), [API](https://pertpy.scverse.org/en/stable/api.html), [Changelog](https://pertpy.scverse.org/en/stable/changelog.html), version-specific PyPI metadata |
| [Guides and efficacy](guides-efficacy.md) | [Guide assignment](https://pertpy.scverse.org/en/stable/tutorials/notebooks/guide_rna_assignment.html), [efficacy tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/perturbation_efficacy.html), GuideAssignment/Mixscape/Mixscale APIs linked there |
| [Expression and abundance](expression-abundance.md) | [DE](https://pertpy.scverse.org/en/stable/tutorials/notebooks/differential_gene_expression.html), [Milo](https://pertpy.scverse.org/en/stable/tutorials/notebooks/milo.html), [scCODA](https://pertpy.scverse.org/en/stable/tutorials/notebooks/sccoda.html), [tascCODA](https://pertpy.scverse.org/en/stable/tutorials/notebooks/tasccoda.html) |
| [Distances and prioritization](distances-prioritization.md) | [Distances](https://pertpy.scverse.org/en/stable/tutorials/notebooks/distances.html), [distance tests](https://pertpy.scverse.org/en/stable/tutorials/notebooks/distance_tests.html), [Augur](https://pertpy.scverse.org/en/stable/tutorials/notebooks/augur.html), corresponding APIs |
| [Spaces and prediction](spaces-prediction.md) | [Spaces](https://pertpy.scverse.org/en/stable/tutorials/notebooks/perturbation_space.html), [Scgen API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Scgen.html), [CINEMA-OT](https://pertpy.scverse.org/en/stable/tutorials/notebooks/cinemaot.html) |
| [Annotation and programs](annotation-programs.md) | [Metadata](https://pertpy.scverse.org/en/stable/tutorials/notebooks/metadata_annotation.html), [enrichment](https://pertpy.scverse.org/en/stable/tutorials/notebooks/enrichment.html), [DIALOGUE](https://pertpy.scverse.org/en/stable/tutorials/notebooks/dialogue.html) |

## Known mismatches resolved in the skill

1. The stable scGen prediction notebook uses `SCGEN` and old framework details. The 1.4.0 wheel exports `Scgen`; its setup, training, prediction, and serialization methods govern the local template.
2. Installation text combines extras in a way that can obscure Milo's Python versus R requirements. The release's `Requires-Dist` entries govern the dependency table.
3. Older perturbation-space examples and method names predate the 1.2.0 redesign. Templates use the 1.4.0 `.compute` signatures and explicit representation keys.
4. DistanceTest's API has no RNG/seed parameter; release source creates unseeded generators internally. Seed guidance is specific to methods that actually expose seeds.
5. Notebook outputs may show historic native result columns, broad warning suppression, or already-processed matrices. Templates use current public result names and state the required input provenance.

The guidance on experimental units, confounding, control matching, and holdout leakage is analytical implementation guidance. It is not a claim that pertpy automatically enforces these properties or that the user has selected a particular study design.

## Refreshing

Determine the project's installed version first. For an update, compare the changelog, relevant API page, and that release's metadata/source. Revise only affected templates and dependency notes; avoid transplanting `main`-branch behavior into instructions for an older release. Retain the user's analysis choices and explain numerical changes that follow from a version migration.

Validate skill frontmatter and links, parse all Python examples, and compare used class/method signatures with the selected release. For runtime validation, use the appropriate project environment and a small representative dataset; optional dependencies and statistical fits require separate execution checks. Skill creation did not install pertpy or run full analyses.

When writing research outputs, cite pertpy and the underlying method(s) used: [Pertpy: an end-to-end framework for perturbation analysis](https://doi.org/10.1038/s41592-025-02909-7), plus the references linked by the relevant tool documentation.
