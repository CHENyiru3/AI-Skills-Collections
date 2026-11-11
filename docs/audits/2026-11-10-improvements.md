# Active skill improvements — 2026-11-10

Implemented the [individual audit](2026-11-10-active-skills-audit.md) sequentially across **111 active skills**: **108 updated**, **3 retained unchanged**. This report covers canonical repository copies. Per-skill decisions, versions, validation limits, changed files and content hashes are in the [implementation ledger](2026-11-10-improvements.json).

## Size and version changes

| Metric | Before implementation | After implementation |
| --- | ---: | ---: |
| SKILL.md lines | 25,985 | 4,821 |
| SKILL.md whitespace-separated words | 112,150 | 42,712 |
| Files in active skill folders | 684 | 684 |

Entrypoint words decreased by **61.9%**; this is a file-text measure, not measured model-token savings. Domain contracts and useful optional resources were preserved. No skill folder/support file was moved or removed in this implementation pass. The 51 archived files retain their saved hashes.

Versions match between frontmatter and registry for all 111 skills. There are 106 patch corrections, UniProt **1.1.0** for added paged-retrieval interfaces, and PyDESeq2 **2.0.0** for the changed CLI contract. JEPA development, ChimeraX MCP and computational biology retrospective remain at **1.0.0**, byte-for-byte unchanged from the versioned baseline.

PyDESeq2 now requires an explicit `--shrink-coeff` to opt into shrinkage, keeps unshrunk results, rejects invalid/mismatched inputs, and propagates `--alpha` to exports and plots. Existing users should review that CLI change before replacing a local copy. Compare actual content and hashes as well as versions when reconciling copies; see the [conflict policy](../guides/architecture.md#skill-versions-and-conflicts).

## Material decisions

- Preserved domain-specific data alignment, statistical design, file-format, session identity, evidence and export contracts. Required sequences remain explicit where their order affects correctness.
- Narrowed product-name and artifact catchall triggers; generic document skills honor a requested backend, and specialized H5AD/Seurat/ML workflows state their actual scope.
- Removed duplicated manuals, unrelated promotions, fabricated preferences, unsupported API examples, fixed scientific thresholds/labels and mandatory improvement or approval loops.
- Repaired directly implicated helpers rather than shortening their documentation around known failures: isolated spreadsheet recalculation, server-process cleanup, scaffold/version writes, opt-in ZotPilot installation and protected registration, paged API retrieval, input checks and schema handling.
- Kept Scribble active for explicit identification follow-up, with a narrow trigger and clear unresolved status. It cannot select/install a generic package or claim a validated integration workflow.

## Repository repairs

Marketplace skill paths now resolve relative to each plugin source and must remain inside it with a real `SKILL.md`. The generator has a read-only `--check` mode. All 9 plugins and 111 references pass.

The registry validator now rejects duplicate YAML keys before parsing can silently overwrite skill IDs or fields. Identical duplicate `profiles`/`taskpacks` fields were removed from the GitHub repository-management entry. Duplicate-ID and duplicate-version fixtures are rejected.

## Validation

Registry, skill-document, deployment/profile, marketplace and whitespace checks passed. Registry validation has eight informational warnings for first registrations without legacy paths. Strict static checks verified 111 matching quoted versions, 126 relative links in entrypoints, all 8 UI YAML files, applicable fenced examples, and changed Python syntax. Archived files passed 51 hash checks.

- Actual LibreOffice on temporary XLSX working copies: SUM cached 5; divide-by-zero error recognized; valid empty-string cache accepted; literal #REF! text not misclassified; failed/timeout runs preserve input.
- Actual temporary noisy HTTP server with 1 MB output: client 200, cleanup, and occupied-port refusal passed.
- Project scaffold fixtures: TOML escaping, complete MIT license, development dependencies, invalid project names and existing destination refusal passed.
- Version-bump fixture: only project.version changed, unrelated tool versions preserved, dry run left bytes unchanged.
- ZotPilot mocked missing CLI/help invoked no installer; credential-bearing CLI registration refused before spawning any subprocess.
- GitHub helper stub fixtures: exact HTTPS/SSH hosts, repository parsing, and no token output passed.
- UniProt mocked JSON/TSV pagination, mapping redirect/deadline/failure, one-to-many/failed IDs and input bounds passed.
- KEGG mocked pacing/timeouts, binary images and explicit input-limit failure passed.
- Reactome mocked nested pathway identity and distinct output path preserving source passed.
- Ensembl mocked FASTA/text path shares timeout/status/format handling.
- PyDESeq2 fixture: metadata reordered by exact sample set, invalid/duplicate/mismatched input rejected, selected alpha propagated to result export. No statistical fit performed.
- Changed CLI --help checks passed; changed Python helpers parsed; shell helpers passed bash -n. No bulk dataset, model training, cloud job, credential registration, publication or installed-skill synchronization performed.

Routine repository checks (in an environment with PyYAML):

```bash
python scripts/validate_registry.py
python scripts/check_skill_docs.py
python scripts/validate_profiles.py
python scripts/build_marketplace.py --check
git diff --check
```

## Remaining limits

- All 111 SKILL.md entrypoints and their available UI metadata received individual review. Supporting resources were inspected and repaired where directly implicated; all bundled resources were not exhaustively revalidated.
- Scribble identity remains unresolved. The entry and catalog now state that identification is required; placeholder installation and integration APIs were removed.
- Most ML/biology workflows were corrected by source/static review, not executed on real scientific datasets or accelerators. Exact APIs remain version-specific.
- Some provider documentation was inaccessible by direct fetch; primary-source search excerpts or project documentation were used where available. No claimed live provider job was run.
- Local baseline versions are repository versions, not upstream package releases; no per-skill Git release tags, commit or push were created.

The remaining blockers are task-specific: a verified package identity for Scribble; supported input/schema/version for a named operation; and the evidence needed for the requested scientific claim. They do not require unrelated infrastructure or repeated approvals. Stop after the requested artifact/behavior and its relevant checks pass. No further length target is an acceptance criterion.

## Individual implementation index

The order below is the actual sequential implementation order. The ledger retains each skill’s keep/condense/delete reasoning and deliberate uncertainties. “Retained” means the versioned folder hash is unchanged.

| # | Skill | Version before → after | Lines before → after | Words before → after | Decision |
| ---: | --- | --- | ---: | ---: | --- |
| 1 | [skill-cutter](../../skills-market/core/dev/skill-cutter/SKILL.md) | 1.0.0 → 1.0.1 | 132 → 79 | 900 → 570 | Updated: Repeated explanations and proportionate reporting. |
| 2 | [skill-creator](../../skills-market/core/dev/skill-creator/SKILL.md) | 1.0.0 → 1.0.1 | 503 → 84 | 5170 → 604 | Updated: Authoring process and evaluation/benchmark instructions into task-dependent workflows. |
| 3 | [security-audit](../../skills-market/core/security/security-audit/SKILL.md) | 1.0.0 → 1.0.1 | 108 → 63 | 427 → 411 | Updated: Tool patterns and CI into conditional workflows. |
| 4 | [codex](../../skills-market/agents/codex/SKILL.md) | 1.0.0 → 1.0.1 | 114 → 55 | 527 → 349 | Updated: Batch/review/worktree mechanics into conditional guidance. |
| 5 | [claude-code](../../skills-market/agents/claude-code/SKILL.md) | 2.2.0 → 2.2.1 | 745 → 69 | 4893 → 428 | Updated: CLI operations into help-driven interaction and execution contracts. |
| 6 | [karpathy-guidelines](../../archive/skills/agents/guidelines/karpathy-guidelines/SKILL.md) | 1.0.0 → 1.0.1 | 70 → 28 | 376 → 184 | Updated: Repeated maxims into concrete decisions. |
| 7 | [mcp-builder](../../skills-market/agents/mcp/mcp-builder/SKILL.md) | 1.0.0 → 1.0.1 | 239 → 59 | 1148 → 434 | Updated: Language/setup guidance into conditional references and pinned-SDK checks. |
| 8 | [api-design](../../skills-market/programming/python/api-design/SKILL.md) | 1.0.0 → 1.0.1 | 123 → 36 | 387 → 268 | Updated: Naming/style advice and conditional pattern references. |
| 9 | [cli-development](../../skills-market/programming/python/cli-development/SKILL.md) | 1.0.0 → 1.0.1 | 127 → 36 | 374 → 274 | Updated: Framework catalogs and testing into focused decisions. |
| 10 | [code-quality](../../skills-market/programming/python/code-quality/SKILL.md) | 1.0.0 → 1.0.1 | 137 → 36 | 463 → 252 | Updated: Tool selection/configuration through conditional resources. |
| 11 | [community](../../skills-market/programming/python/community/SKILL.md) | 1.0.0 → 1.0.1 | 134 → 33 | 407 → 228 | Updated: Template options and safe automation scope. |
| 12 | [documentation](../../skills-market/programming/python/documentation/SKILL.md) | 1.0.0 → 1.0.1 | 132 → 33 | 366 → 243 | Updated: Build/tutorial variants into selective references. |
| 13 | [jupyter](../../skills-market/programming/python/jupyter/SKILL.md) | 1.0.0 → 1.0.1 | 61 → 30 | 193 → 226 | Updated: Basic JSON and conversion recipes into operation-specific guidance. |
| 14 | [library-review](../../skills-market/programming/python/library-review/SKILL.md) | 1.0.0 → 1.0.1 | 106 → 40 | 455 → 293 | Updated: Review dimensions and optional report/checklist resources. |
| 15 | [packaging](../../skills-market/programming/python/packaging/SKILL.md) | 1.0.0 → 1.0.1 | 135 → 42 | 364 → 316 | Updated: Backend/template variants into selective resources. |
| 16 | [performance](../../skills-market/programming/python/performance/SKILL.md) | 1.0.0 → 1.0.1 | 129 → 34 | 415 → 251 | Updated: Tool catalogs and benchmark advice. |
| 17 | [project-setup](../../skills-market/programming/python/project-setup/SKILL.md) | 1.0.0 → 1.0.1 | 110 → 39 | 379 → 270 | Updated: Setup decisions and optional templates. |
| 18 | [release-management](../../skills-market/programming/python/release-management/SKILL.md) | 1.0.0 → 1.0.1 | 132 → 39 | 377 → 289 | Updated: Changelog/deprecation/automation variants. |
| 19 | [sqlite](../../skills-market/programming/python/sqlite/SKILL.md) | 1.0.0 → 1.0.1 | 78 → 55 | 512 → 378 | Updated: Type/schema/performance guidance into workload-dependent decisions. |
| 20 | [testing-strategy](../../skills-market/programming/python/testing-strategy/SKILL.md) | 1.0.0 → 1.0.1 | 120 → 35 | 365 → 270 | Updated: Fixtures/property/CI options into conditional resources. |
| 21 | [officecli](../../skills-market/documents/office/officecli/SKILL.md) | 1.0.0 → 1.0.1 | 112 → 38 | 347 → 273 | Updated: Command catalog and batch/resident guidance. |
| 22 | [officecli-docx](../../skills-market/documents/office/officecli-docx/SKILL.md) | 1.0.0 → 1.0.1 | 52 → 28 | 186 → 206 | Updated: Duplicated commands and QA. |
| 23 | [officecli-pptx](../../skills-market/documents/office/officecli-pptx/SKILL.md) | 1.0.0 → 1.0.1 | 51 → 25 | 182 → 190 | Updated: Read/edit/preview command duplication. |
| 24 | [officecli-xlsx](../../skills-market/documents/office/officecli-xlsx/SKILL.md) | 1.0.0 → 1.0.1 | 52 → 29 | 185 → 223 | Updated: Repeated commands and batch advice. |
| 25 | [docx](../../skills-market/documents/formats/docx/SKILL.md) | 1.0.0 → 1.0.1 | 593 → 102 | 2616 → 743 | Updated: Creation recipes into rendering contracts and conditional helper routing. |
| 26 | [pdf](../../skills-market/documents/formats/pdf/SKILL.md) | 1.0.0 → 1.0.1 | 317 → 55 | 1012 → 397 | Updated: Basic extraction/merge/OCR/library tutorials. |
| 27 | [pptx](../../skills-market/documents/formats/pptx/SKILL.md) | 1.0.0 → 1.0.1 | 235 → 48 | 1420 → 344 | Updated: Creation/editing/QA into scoped workflows. |
| 28 | [xlsx](../../skills-market/documents/formats/xlsx/SKILL.md) | 1.0.0 → 1.0.1 | 295 → 58 | 1613 → 418 | Updated: Generic pandas/openpyxl tutorials and financial-model variants. |
| 29 | [algorithmic-art](../../skills-market/documents/design/algorithmic-art/SKILL.md) | 1.0.0 → 1.0.1 | 408 → 41 | 2766 → 295 | Updated: Creative planning and optional template usage. |
| 30 | [canvas-design](../../skills-market/documents/design/canvas-design/SKILL.md) | 1.0.0 → 1.0.1 | 133 → 35 | 1754 → 277 | Updated: Concept development and export guidance. |
| 31 | [frontend-design](../../skills-market/documents/design/frontend-design/SKILL.md) | 1.0.0 → 1.0.1 | 45 → 31 | 588 → 241 | Updated: Aesthetic options into contextual choices. |
| 32 | [brand-guidelines](../../skills-market/documents/design/brand-guidelines/SKILL.md) | 1.0.0 → 1.0.1 | 76 → 34 | 334 → 233 | Updated: Duplicated styling instructions. |
| 33 | [theme-factory](../../skills-market/documents/design/theme-factory/SKILL.md) | 1.0.0 → 1.0.1 | 62 → 28 | 491 → 209 | Updated: Theme catalog and application process. |
| 34 | [web-artifacts-builder](../../skills-market/documents/design/web-artifacts-builder/SKILL.md) | 1.0.0 → 1.0.1 | 77 → 37 | 451 → 293 | Updated: Optional stack/bootstrap/bundle instructions. |
| 35 | [webapp-testing](../../skills-market/documents/design/webapp-testing/SKILL.md) | 1.0.0 → 1.0.1 | 99 → 42 | 506 → 285 | Updated: Automation recipes and example routing. |
| 36 | [doc-coauthoring](../../skills-market/documents/collaboration/doc-coauthoring/SKILL.md) | 1.0.0 → 1.0.1 | 378 → 37 | 2471 → 281 | Updated: Three-stage process into scope-dependent authoring. |
| 37 | [internal-comms](../../skills-market/documents/collaboration/internal-comms/SKILL.md) | 1.0.0 → 1.0.1 | 35 → 27 | 216 → 177 | Updated: Repeated activation list. |
| 38 | [scientific-figure-polish](../../skills-market/documents/design/scientific-figure-polish/SKILL.md) | 1.0.0 → 1.0.1 | 67 → 67 | 1149 → 1144 | Updated: Figure-specific anecdote and overwrite protection to named mutation risk. |
| 39 | [imgur-cli](../../skills-market/documents/media/imgur-cli/SKILL.md) | 1.0.0 → 1.0.1 | 64 → 64 | 287 → 326 | Updated: Environment discovery and bounded failure handling. |
| 40 | [slack-gif-creator](../../skills-market/documents/media/slack-gif-creator/SKILL.md) | 1.0.0 → 1.0.1 | 257 → 38 | 1108 → 312 | Updated: Pillow drawing and animation tutorials. |
| 41 | [academic-writing-editor](../../skills-market/writing/academic/academic-writing-editor/SKILL.md) | 1.0.0 → 1.0.1 | 42 → 32 | 400 → 238 | Updated: Narrative frameworks into optional lenses. |
| 42 | [draft-spatial-methods](../../skills-market/compbio/expert-workflows/draft-spatial-methods/SKILL.md) | 1.0.0 → 1.0.1 | 23 → 36 | 207 → 244 | Updated: Fixed section requirements into applicable analysis stages. |
| 43 | [critique-bio-manuscript](../../skills-market/compbio/expert-workflows/critique-bio-manuscript/SKILL.md) | 1.0.0 → 1.0.1 | 21 → 34 | 200 → 251 | Updated: Review criteria to claim-dependent questions. |
| 44 | [explain-bio-dl-model](../../skills-market/compbio/expert-workflows/explain-bio-dl-model/SKILL.md) | 1.0.0 → 1.0.1 | 18 → 28 | 184 → 204 | Updated: Problem/rationale/validation structure into conditional narrative. |
| 45 | [humanizer](../../skills-market/writing/academic/humanizer/SKILL.md) | 3.0.0 → 3.0.1 | 160 → 35 | 759 → 241 | Updated: Repeated academic/general modes and final audits. |
| 46 | [duke-nus-marp](../../skills-market/writing/presentations/duke-nus-marp/SKILL.md) | 1.0.0 → 1.0.1 | 73 → 71 | 1004 → 1006 | Updated: Asset provenance and delivery defaults. |
| 47 | [humanizer-zh](../../skills-market/writing/academic/humanizer-zh/SKILL.md) | 1.0.0 → 1.0.1 | 487 → 51 | 787 → 68 | Updated: Pattern catalog to diagnosed expression problems and a faithful example. |
| 48 | [asd-ste100](../../skills-market/writing/technical/asd-ste100/SKILL.md) | 0.4.0 → 0.4.1 | 140 → 40 | 2656 → 331 | Updated: Modes, overlapping rule tables, repeated output/boundary explanations. |
| 49 | [compile-latex](../../skills-market/writing/latex/compile-latex/SKILL.md) | 1.0.0 → 1.0.1 | 260 → 51 | 1211 → 384 | Updated: Build and error workflows. |
| 50 | [latex-writing](../../skills-market/writing/latex/latex-writing/SKILL.md) | 1.0.0 → 1.0.1 | 283 → 42 | 1242 → 329 | Updated: Repeated examples and academic prose advice. |
| 51 | [obsidian-bases](../../skills-market/writing/obsidian/obsidian-bases/SKILL.md) | 1.0.0 → 1.0.1 | 502 → 61 | 1797 → 331 | Updated: Duplicated schema/function/view recipes to one adaptable example and conditional reference. |
| 52 | [json-canvas](../../skills-market/writing/obsidian/json-canvas/SKILL.md) | 1.0.0 → 1.0.1 | 249 → 50 | 1275 → 392 | Updated: Repeated workflows, examples and layout size tables. |
| 53 | [obsidian-markdown](../../skills-market/writing/obsidian/obsidian-markdown/SKILL.md) | 1.0.0 → 1.0.1 | 201 → 42 | 724 → 295 | Updated: Tutorials and complete examples through conditional references. |
| 54 | [obsidian-cli](../../skills-market/writing/obsidian/obsidian-cli/SKILL.md) | 1.0.0 → 1.0.1 | 111 → 37 | 487 → 254 | Updated: Command catalog and examples. |
| 55 | [defuddle](../../skills-market/writing/obsidian/defuddle/SKILL.md) | 1.0.0 → 1.0.1 | 44 → 31 | 189 → 200 | Updated: Metadata/format flag catalog into help-driven operation. |
| 56 | [wiki-keeper](../../skills-market/writing/obsidian/wiki-keeper/SKILL.md) | 1.0.0 → 1.0.1 | 177 → 42 | 887 → 317 | Updated: Discovery/output rituals and mode-specific workflows. |
| 57 | [zotpilot](../../skills-market/writing/literature/zotpilot/SKILL.md) | 1.0.0 → 1.0.1 | 275 → 57 | 1912 → 427 | Updated: Legacy tool catalogs and setup decision tree into conditional resources/discovery. |
| 58 | [github-auth](../../skills-market/platforms/github/github-auth/SKILL.md) | 1.1.0 → 1.1.1 | 247 → 54 | 1139 → 355 | Updated: SSH/HTTPS/gh paths into task-dependent setup. |
| 59 | [github-codebase-inspection](../../skills-market/platforms/github/codebase-inspection/SKILL.md) | 1.0.0 → 1.0.1 | 116 → 45 | 475 → 250 | Updated: Command catalogs and duplicate pitfalls. |
| 60 | [github-issues](../../skills-market/platforms/github/github-issues/SKILL.md) | 1.1.0 → 1.1.1 | 370 → 49 | 1220 → 310 | Updated: gh/REST duplicate recipes into shared operation contracts. |
| 61 | [github-code-review](../../skills-market/platforms/github/github-code-review/SKILL.md) | 1.1.0 → 1.1.1 | 481 → 51 | 1868 → 324 | Updated: Review categories and optional report template. |
| 62 | [github-pr-workflow](../../skills-market/platforms/github/github-pr-workflow/SKILL.md) | 1.1.0 → 1.1.1 | 367 → 58 | 1439 → 376 | Updated: Lifecycle/REST/CLI catalogs and conditional references. |
| 63 | [github-repo-management](../../skills-market/platforms/github/github-repo-management/SKILL.md) | 1.1.0 → 1.1.1 | 516 → 58 | 1657 → 367 | Updated: Large gh/REST action catalog into operation contracts and selective reference. |
| 64 | [page-keeper](../../skills-market/frontend/site-maintenance/page-keeper/SKILL.md) | 1.0.0 → 1.0.1 | 208 → 37 | 1100 → 269 | Updated: Map/rulebook/template/eval stages into conditional aids. |
| 65 | [chen-academic-page-maintainer](../../skills-market/frontend/site-maintenance/chen-academic-page-maintainer/SKILL.md) | 1.0.0 → 1.0.1 | 221 → 56 | 1931 → 446 | Updated: Repo map and long section rules through relevant existing references. |
| 66 | [latent-identifiability](../../skills-market/ai-ml/theory/latent-identifiability/SKILL.md) | 1.0.0 → 1.0.1 | 98 → 98 | 1407 → 1399 | Updated: Ledger/table work to the current proof/application scope. |
| 67 | [jepa-pytorch-development](../../skills-market/ai-ml/deep-learning/jepa-pytorch-development/SKILL.md) | 1.0.0 → 1.0.0 | 82 → 82 | 1093 → 1093 | Retained: None justified beyond existing selective reference routing. |
| 68 | [browser-use](../../skills-market/ai-ml/llm/browser-use/SKILL.md) | 1.1.0 → 1.1.1 | 116 → 28 | 508 → 339 | Updated: Replaced import inventory and deployment tutorial with setup/diagnosis/verification decisions. |
| 69 | [pytorch](../../skills-market/ai-ml/deep-learning/pytorch/SKILL.md) | 1.0.0 → 1.0.1 | 470 → 52 | 1536 → 450 | Updated: Removed generic API catalog; kept one complete CPU example and failure-sensitive training rules. |
| 70 | [pytorch-lightning](../../skills-market/ai-ml/training/pytorch-lightning/SKILL.md) | 1.0.0 → 1.0.1 | 452 → 36 | 1176 → 380 | Updated: Replaced multiple partial tutorial models with one version-aware workflow. |
| 71 | [bitsandbytes](../../skills-market/ai-ml/llm/bitsandbytes/SKILL.md) | 1.0.0 → 1.0.1 | 331 → 35 | 1055 → 355 | Updated: Removed repeated gated-model loading examples and misleading fixed VRAM table. |
| 72 | [transformers](../../skills-market/ai-ml/llm/transformers/SKILL.md) | 1.0.0 → 1.0.1 | 457 → 38 | 1508 → 481 | Updated: Replaced repetitive model/API tutorial with task-dependent checks. |
| 73 | [peft](../../skills-market/ai-ml/llm/peft/SKILL.md) | 1.0.0 → 1.0.1 | 404 → 38 | 1247 → 422 | Updated: Removed duplicated gated-model recipes and fixed memory/default hyperparameter tables. |
| 74 | [trl](../../skills-market/ai-ml/llm/trl/SKILL.md) | 1.0.0 → 1.0.1 | 484 → 38 | 1286 → 424 | Updated: Replaced incompatible partial recipes with schema and algorithm checks. |
| 75 | [accelerate](../../skills-market/ai-ml/training/accelerate/SKILL.md) | 1.0.0 → 1.0.1 | 405 → 47 | 1240 → 386 | Updated: Removed repeated loops and API inventory. |
| 76 | [deepspeed](../../skills-market/ai-ml/training/deepspeed/SKILL.md) | 1.0.0 → 1.0.1 | 441 → 42 | 1094 → 438 | Updated: Replaced repeated speculative JSON blocks with stage- and integration-specific configuration rules. |
| 77 | [huggingface-hub](../../skills-market/ai-ml/llm/huggingface-hub/SKILL.md) | 1.0.0 → 1.0.1 | 467 → 35 | 1298 → 391 | Updated: Removed broad API tutorial and sample artifacts with invented metrics. |
| 78 | [datasets](../../skills-market/ai-ml/training/datasets/SKILL.md) | 1.0.0 → 1.0.1 | 419 → 46 | 1265 → 432 | Updated: Replaced broad repetitive API catalog with type/schema/split contracts and one local example. |
| 79 | [spatialdata](../../skills-market/compbio/spatial-omics/analysis/spatialdata/SKILL.md) | 1.0.0 → 1.0.1 | 97 → 36 | 275 → 338 | Updated: Replaced platform list and empty integrations with element/identity contracts. |
| 80 | [vitessce](../../skills-market/compbio/spatial-omics/visualization/vitessce/SKILL.md) | 1.0.0 → 1.0.1 | 94 → 31 | 271 → 332 | Updated: Replaced unsupported runnable-looking dashboard with loader/config/coordination workflow. |
| 81 | [stereo-seq](../../skills-market/compbio/spatial-omics/platforms/stereo-seq/SKILL.md) | 1.0.0 → 1.0.1 | 114 → 34 | 326 → 358 | Updated: Replaced generic Scanpy/Seurat boilerplate with format/resolution and alignment rules. |
| 82 | [giotto](../../skills-market/compbio/spatial-omics/analysis/giotto/SKILL.md) | 1.0.0 → 1.0.1 | 147 → 25 | 362 → 297 | Updated: Version-specific workflow replaces mixed-package setup/tutorial. |
| 83 | [scribble](../../skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md) | 1.0.0 → 1.0.1 | 85 → 25 | 227 → 262 | Updated: Converted unsupported tutorial into an identity gate and post-identification validation contract. |
| 84 | [human-cell-atlas](../../skills-market/compbio/databases/human-cell-atlas/SKILL.md) | 1.0.0 → 1.0.1 | 86 → 30 | 262 → 308 | Updated: Replaced broad atlas overview and placeholder marker/mapping blocks with provenance workflow. |
| 85 | [anndatar](../../skills-market/compbio/single-cell/analysis/anndatar/SKILL.md) | 1.0.0 → 1.0.1 | 227 → 37 | 692 → 349 | Updated: Replaced slot catalog and ecosystem comparison with explicit semantic mapping and round-trip checks. |
| 86 | [schard](../../skills-market/compbio/single-cell/analysis/schard/SKILL.md) | 1.0.0 → 1.0.1 | 129 → 30 | 432 → 308 | Updated: Removed fixed public data downloads and sample-specific plotting tutorial. |
| 87 | [snakemake](../../skills-market/compbio/workflows/snakemake/SKILL.md) | 1.0.0 → 1.0.1 | 225 → 35 | 419 → 399 | Updated: Replaced generic and incomplete pipeline tutorials with dependency and file-format checks. |
| 88 | [nextflow](../../skills-market/compbio/workflows/nextflow/SKILL.md) | 1.0.0 → 1.0.1 | 264 → 37 | 554 → 433 | Updated: Replaced incompatible partial single-cell example and command catalog with tuple/dependency/resume contracts. |
| 89 | [squidpy](../../skills-market/compbio/spatial-omics/analysis/squidpy/SKILL.md) | 1.0.0 → 1.0.1 | 333 → 36 | 717 → 353 | Updated: Removed duplicated Scanpy pipeline and speculative plotting/API catalog. |
| 90 | [archr](../../skills-market/compbio/multiomics/scATAC-seq/archr/SKILL.md) | 1.0.0 → 1.0.1 | 267 → 32 | 679 → 367 | Updated: Replaced unsupported function catalog with ordered dependencies and interpretation boundaries. |
| 91 | [signac](../../skills-market/compbio/multiomics/scATAC-seq/signac/SKILL.md) | 1.0.0 → 1.0.1 | 214 → 42 | 530 → 360 | Updated: Replaced mixed API snippets with assay/reduction contracts and a correct GeneActivity fragment. |
| 92 | [cellxgene](../../skills-market/compbio/single-cell/visualization/cellxgene/SKILL.md) | 1.0.0 → 1.0.1 | 206 → 36 | 650 → 350 | Updated: Removed UI inventory and speculative embedding/config tutorial. |
| 93 | [scanpy](../../skills-market/compbio/single-cell/analysis/scanpy/SKILL.md) | 1.0.0 → 1.0.1 | 388 → 44 | 1391 → 467 | Updated: Replaced tutorial API catalog with layer, graph, evidence and replicate decision rules. |
| 94 | [anndata](../../skills-market/compbio/single-cell/analysis/anndata/SKILL.md) | 1.0.0 → 1.0.1 | 402 → 40 | 1342 → 403 | Updated: Removed duplicate full Scanpy pipeline and broad ecosystem installation tutorial. |
| 95 | [seurat](../../skills-market/compbio/single-cell/analysis/seurat/SKILL.md) | 1.0.0 → 1.0.1 | 294 → 36 | 1093 → 399 | Updated: Replaced generic PBMC walkthrough with assay/version/replicate decisions. |
| 96 | [scvi-tools](../../skills-market/compbio/single-cell/analysis/scvi-tools/SKILL.md) | 1.0.0 → 1.0.1 | 192 → 36 | 930 → 425 | Updated: Replaced broad model catalog and incomplete universal example with model-specific data/evidence contracts. |
| 97 | [monocle3](../../skills-market/compbio/single-cell/analysis/monocle3/SKILL.md) | 1.0.0 → 1.0.1 | 578 → 35 | 1944 → 392 | Updated: Removed repeated pseudotime/testing/3D tutorials and example-specific biology. |
| 98 | [seurat-v5](../../skills-market/compbio/single-cell/integration/seurat-v5/SKILL.md) | 1.0.0 → 1.0.1 | 278 → 37 | 909 → 438 | Updated: Removed repeated CITE walkthrough and inaccurate v4/v5 comparison. |
| 99 | [harmony](../../skills-market/compbio/single-cell/integration/harmony/SKILL.md) | 1.0.0 → 1.0.1 | 242 → 34 | 903 → 344 | Updated: Replaced generic integration tutorial and method ranking with correction/output contracts. |
| 100 | [scanorama](../../skills-market/compbio/single-cell/integration/scanorama/SKILL.md) | 1.0.0 → 1.0.1 | 292 → 34 | 863 → 336 | Updated: Replaced broken complete workflow and speculative parameter catalog. |
| 101 | [bbknn](../../skills-market/compbio/single-cell/integration/bbknn/SKILL.md) | 1.0.0 → 1.0.1 | 264 → 35 | 748 → 347 | Updated: Removed repeated pipeline and method comparison with unsupported accuracy rankings. |
| 102 | [chimerax-mcp](../../skills-market/compbio/structural-biology/chimerax-mcp/SKILL.md) | 1.0.0 → 1.0.0 | 65 → 65 | 933 → 933 | Retained: None: current 69-line root already provides a specific workflow and conditional references. |
| 103 | [computational-biology-retrospective](../../skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md) | 1.0.0 → 1.0.0 | 120 → 120 | 1645 → 1645 | Retained: None: current detail supports evidence recovery and avoids rerunning research by default. |
| 104 | [pydeseq2](../../skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md) | 1.0.0 → 2.0.0 | 561 → 37 | 1965 → 504 | Updated: Removed repeated examples and stale requirements/API inventory. |
| 105 | [cellxgene-census](../../skills-market/compbio/single-cell/visualization/cellxgene-census/SKILL.md) | 1.0.0 → 1.0.1 | 513 → 36 | 1837 → 425 | Updated: Replaced repeated broad query examples and stale inventory metrics with data/denominator contracts. |
| 106 | [metabolomics-workbench](../../skills-market/compbio/multiomics/metabolomics/metabolomics-workbench/SKILL.md) | 1.0.0 → 1.0.1 | 261 → 36 | 1207 → 372 | Updated: Replaced endpoint catalog and repeated workflows with identity/measurement contracts. |
| 107 | [uniprot](../../skills-market/compbio/multiomics/proteomics/uniprot/SKILL.md) | 1.0.0 → 1.1.0 | 197 → 36 | 952 → 362 | Updated: Replaced repeated query catalog and fixed job-limit claims with operation/completeness contracts. |
| 108 | [kegg](../../skills-market/compbio/databases/kegg/SKILL.md) | 1.0.0 → 1.0.1 | 379 → 33 | 1612 → 353 | Updated: Removed repetitive API/workflow/category catalog. |
| 109 | [reactome](../../skills-market/compbio/databases/reactome/SKILL.md) | 1.0.0 → 1.0.1 | 280 → 34 | 1056 → 380 | Updated: Replaced broad API tutorial and stale statistics with schema/coverage/background interpretation. |
| 110 | [geo](../../skills-market/compbio/databases/geo/SKILL.md) | 1.0.0 → 1.0.1 | 817 → 39 | 2665 → 406 | Updated: Removed repeated tutorial, incomplete FTP helper and uncontrolled analysis/metaanalysis examples. |
| 111 | [ensembl](../../skills-market/compbio/databases/ensembl/SKILL.md) | 1.0.0 → 1.0.1 | 313 → 36 | 1116 → 363 | Updated: Replaced speculative package examples and stale release inventory with coordinate/identity contracts. |
