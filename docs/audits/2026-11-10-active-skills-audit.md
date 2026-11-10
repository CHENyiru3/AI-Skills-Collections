# Active skills audit — 2026-11-10

> Historical audit snapshot, captured before the authorized implementation. Findings, line references, versions, and hashes below describe that earlier state. See [implemented improvements](2026-11-10-improvements.md) and the [implementation ledger](2026-11-10-improvements.json) for current decisions and validation.


All **111 active skills** were reviewed individually and sequentially using skill-cutter's audit mode. The main update need is correctness and scope control, followed by context reduction. Length alone is not a reason to cut or archive a skill.

This report records recommendations. Skill instructions, scripts, references, assets and UI behavior were not rewritten. The separately requested version metadata was added to each active skill and mirrored in the registry. Archived skills remain outside the active market.

## Coverage and limits

The review read every complete active `SKILL.md` and its available `agents/openai.yaml`, and selectively inspected resources implicated by the findings. It checked local paths and consulted primary documentation for selected provider/API claims. This is a static audit, not a claim that every example or every bundled resource was executed or exhaustively tested. Statements such as “unverified,” “questionable,” and “needs verification” are open questions, not confirmed API failures.

Priorities describe the update queue: **P1** means repair a concrete defect or resolve a material correctness, data-integrity, authorization or API question before trusting the affected workflow; **P2** means narrow routing, remove excessive gates, condense generic material or strengthen a contract; **P3** means retain the core with optional targeted cleanup. P1 is not a vulnerability severity score, and it does not automatically justify archiving.

| Priority | Skills |
| --- | ---: |
| P1 | 70 |
| P2 | 35 |
| P3 | 6 |

## First repairs to make

1. **Marketplace discovery:** all 111 configured skill paths resolve to nonexistent directories when interpreted relative to their plugin `source`. For example, source `./skills-market/documents` plus skill `./documents/collaboration/doc-coauthoring` becomes `skills-market/documents/documents/collaboration/doc-coauthoring`. The generator strips only `skills-market/`, leaving the domain twice. Generate component paths relative to each plugin root, then test both containment and `SKILL.md` existence. Existing registry/doc validators do not catch this. This is a local filesystem finding; the root-relative interpretation is supported by the [Claude Code manifest path rules](https://code.claude.com/docs/en/plugins-reference#path-rules). No installer runtime test was performed.
2. **Unrelated or persistent writes:** remove skill-creator's mandatory unrelated installation locations; separate audit from dependency modification, GitHub posting/publication and permission bypass. Repair the XLSX helper's shared-profile macro overwrite and timeout handling before relying on it.
3. **Broken and misleading examples:** address placeholder installation sources, syntax corruption, wrong object/API usage, count-versus-normalized-data confusion, positional feature/cell alignment, complete-confounding advice, and sparse means that exclude zeros. The individual records identify the evidence.
4. **Routing conflicts:** reconcile generic format skills with OfficeCLI adapters, Seurat with seurat-v5, H5AD interchange skills, and broad Zotero/product-name triggers. Honor an explicitly requested interface. Keep narrow Marp, JEPA, retrospective, ChimeraX and theory contracts.
5. **Context and ceremony:** remove duplicated manuals, unrelated product promotion (present in 21 active skills), fabricated user preferences and mandatory improvement loops. Move a variant to references only when it is useful and conditionally needed; do not merely relocate bulk to meet a length target.

The generator issue is recorded in `scripts/build_marketplace.py` (`build_plugin`) and `.claude-plugin/marketplace.json`; it was unapplied at this audit snapshot. Its repair and validation are recorded in the implementation report.

## Acceptance force and stopping rules

| Material | Treatment | Reason and proportional proof |
| --- | --- | --- |
| Target identity, data alignment, count/assay meaning, evidence fidelity, secret protection | Keep as narrow invariants | Errors can change scientific meaning, expose data or mutate the wrong target. Verify only what the requested action depends on. |
| A format's actual file contract, an estimable statistical design, current API signature | Keep for the named task | Required to produce a valid artifact or interpretable result. Do not apply across unrelated tasks. |
| Executing unfamiliar code, overwriting user files/profiles, publishing or sending information | Keep risk-triggered controls | Establish the exact target, authorization and appropriate isolation or recovery for that action. Read-only inspection does not require publication permission. |
| Extra coverage targets, aesthetic motifs, benchmark suites, new CI, optional external services | Condense as non-blocking advice | These are not prerequisites unless requested or needed to address a concrete risk. |
| Duplicate tutorial prose, unsupported rankings, unrelated branding/promotion, invented preferences | Delete or verify first | These do not improve execution and may redirect the user or fabricate evidence. |
| Useful modality/tool variants and long API tables | Selectively load references | Keep the entrypoint's decision and data contracts; avoid hiding the same mandatory manual behind a link. |

For each future update, stop when the requested outcome and the checks needed for the changed behavior are satisfied. Do not require finding a defect in an already acceptable artifact, repeated user approvals for authorized reversible work, fresh-reader loops for every small edit, a fixed number of improvement cycles, or unrelated infrastructure changes. Specific exceptions and useful retained controls are recorded below.

## Version baseline and conflict management

All 111 active skills now declare a quoted `metadata.version` in their frontmatter, with the identical `version` in `registry/skills.yaml`. **100** previously unversioned skills received the local baseline `1.0.0`; **11** existing declared versions were retained, normalizing humanizer's `3.0` to `3.0.0`. Legacy top-level versions were moved under metadata. This does not claim that local baseline versions are upstream releases. No per-skill Git release tags were created.

For later changes to instructions or bundled resources, update both fields: PATCH for compatible corrections, MINOR for compatible added capabilities, MAJOR for incompatible behavioral or file contracts. Do not bump versions merely because this report recommends a change. Compare stable ID, version and actual file differences before reconciling copies; equal versions can still contain different edits. Never overwrite user changes solely because another version is higher. See the [version policy](../guides/architecture.md#skill-versions-and-conflicts).

| Metric | Before version metadata | After |
| --- | ---: | ---: |
| SKILL.md lines | 25,825 | 25,985 |
| SKILL.md whitespace-separated words | 111,889 | 112,150 |
| Files inside active skill directories | 684 | 684 |

Instruction bodies changed: **0**. Other bundled resources changed: **0**. The small line/word increase is version metadata, not a behavioral expansion. These are file/word counts, not model token counts or a measured context reduction. Per-skill metrics, current hashes, versions and evidence are retained in the [machine-readable audit](2026-11-10-active-skills-audit.json).

## Individual review index

Entries below follow the actual review sequence. Registry IDs remain stable even where a frontmatter name differs. Versioning does not silently rename skills or change their invocation aliases.

| # | Skill | Version | Priority | Lines before → after |
| ---: | --- | --- | --- | ---: |
| 1 | [skill-cutter](#skill-skill-cutter) | 1.0.0 | P2 | 130 → 132 |
| 2 | [skill-creator](#skill-skill-creator) | 1.0.0 | P1 | 501 → 503 |
| 3 | [security-audit](#skill-security-audit) | 1.0.0 | P1 | 106 → 108 |
| 4 | [codex](#skill-codex) | 1.0.0 | P1 | 114 → 114 |
| 5 | [claude-code](#skill-claude-code) | 2.2.0 | P1 | 745 → 745 |
| 6 | [karpathy-guidelines](#skill-karpathy-guidelines) | 1.0.0 | P2 | 68 → 70 |
| 7 | [mcp-builder](#skill-mcp-builder) | 1.0.0 | P2 | 237 → 239 |
| 8 | [api-design](#skill-api-design) | 1.0.0 | P2 | 121 → 123 |
| 9 | [cli-development](#skill-cli-development) | 1.0.0 | P2 | 125 → 127 |
| 10 | [code-quality](#skill-code-quality) | 1.0.0 | P2 | 135 → 137 |
| 11 | [community](#skill-community) | 1.0.0 | P2 | 132 → 134 |
| 12 | [documentation](#skill-documentation) | 1.0.0 | P2 | 130 → 132 |
| 13 | [jupyter](#skill-jupyter) | 1.0.0 | P2 | 59 → 61 |
| 14 | [library-review](#skill-library-review) | 1.0.0 | P1 | 104 → 106 |
| 15 | [packaging](#skill-packaging) | 1.0.0 | P1 | 133 → 135 |
| 16 | [performance](#skill-performance) | 1.0.0 | P2 | 127 → 129 |
| 17 | [project-setup](#skill-project-setup) | 1.0.0 | P1 | 108 → 110 |
| 18 | [release-management](#skill-release-management) | 1.0.0 | P1 | 130 → 132 |
| 19 | [sqlite](#skill-sqlite) | 1.0.0 | P1 | 78 → 78 |
| 20 | [testing-strategy](#skill-testing-strategy) | 1.0.0 | P2 | 118 → 120 |
| 21 | [officecli](#skill-officecli) | 1.0.0 | P2 | 110 → 112 |
| 22 | [officecli-docx](#skill-officecli-docx) | 1.0.0 | P2 | 50 → 52 |
| 23 | [officecli-pptx](#skill-officecli-pptx) | 1.0.0 | P2 | 49 → 51 |
| 24 | [officecli-xlsx](#skill-officecli-xlsx) | 1.0.0 | P2 | 50 → 52 |
| 25 | [docx](#skill-docx) | 1.0.0 | P2 | 591 → 593 |
| 26 | [pdf](#skill-pdf) | 1.0.0 | P1 | 315 → 317 |
| 27 | [pptx](#skill-pptx) | 1.0.0 | P1 | 233 → 235 |
| 28 | [xlsx](#skill-xlsx) | 1.0.0 | P1 | 293 → 295 |
| 29 | [algorithmic-art](#skill-algorithmic-art) | 1.0.0 | P1 | 406 → 408 |
| 30 | [canvas-design](#skill-canvas-design) | 1.0.0 | P1 | 131 → 133 |
| 31 | [frontend-design](#skill-frontend-design) | 1.0.0 | P2 | 43 → 45 |
| 32 | [brand-guidelines](#skill-brand-guidelines) | 1.0.0 | P2 | 74 → 76 |
| 33 | [theme-factory](#skill-theme-factory) | 1.0.0 | P2 | 60 → 62 |
| 34 | [web-artifacts-builder](#skill-web-artifacts-builder) | 1.0.0 | P1 | 75 → 77 |
| 35 | [webapp-testing](#skill-webapp-testing) | 1.0.0 | P1 | 97 → 99 |
| 36 | [doc-coauthoring](#skill-doc-coauthoring) | 1.0.0 | P1 | 376 → 378 |
| 37 | [internal-comms](#skill-internal-comms) | 1.0.0 | P2 | 33 → 35 |
| 38 | [scientific-figure-polish](#skill-scientific-figure-polish) | 1.0.0 | P2 | 65 → 67 |
| 39 | [imgur-cli](#skill-imgur-cli) | 1.0.0 | P3 | 62 → 64 |
| 40 | [slack-gif-creator](#skill-slack-gif-creator) | 1.0.0 | P2 | 255 → 257 |
| 41 | [academic-writing-editor](#skill-academic-writing-editor) | 1.0.0 | P1 | 40 → 42 |
| 42 | [draft-spatial-methods](#skill-draft-spatial-methods) | 1.0.0 | P1 | 21 → 23 |
| 43 | [critique-bio-manuscript](#skill-critique-bio-manuscript) | 1.0.0 | P2 | 19 → 21 |
| 44 | [explain-bio-dl-model](#skill-explain-bio-dl-model) | 1.0.0 | P1 | 16 → 18 |
| 45 | [humanizer](#skill-humanizer) | 3.0.0 | P2 | 160 → 160 |
| 46 | [humanizer-zh](#skill-humanizer-zh) | 1.0.0 | P1 | 486 → 487 |
| 47 | [asd-ste100](#skill-asd-ste100) | 0.4.0 | P2 | 139 → 140 |
| 48 | [compile-latex](#skill-compile-latex) | 1.0.0 | P1 | 258 → 260 |
| 49 | [latex-writing](#skill-latex-writing) | 1.0.0 | P1 | 281 → 283 |
| 50 | [duke-nus-marp](#skill-duke-nus-marp) | 1.0.0 | P3 | 71 → 73 |
| 51 | [obsidian-bases](#skill-obsidian-bases) | 1.0.0 | P2 | 500 → 502 |
| 52 | [json-canvas](#skill-json-canvas) | 1.0.0 | P2 | 247 → 249 |
| 53 | [obsidian-markdown](#skill-obsidian-markdown) | 1.0.0 | P2 | 199 → 201 |
| 54 | [obsidian-cli](#skill-obsidian-cli) | 1.0.0 | P2 | 109 → 111 |
| 55 | [defuddle](#skill-defuddle) | 1.0.0 | P2 | 42 → 44 |
| 56 | [wiki-keeper](#skill-wiki-keeper) | 1.0.0 | P1 | 175 → 177 |
| 57 | [zotpilot](#skill-zotpilot) | 1.0.0 | P1 | 273 → 275 |
| 58 | [github-auth](#skill-github-auth) | 1.1.0 | P1 | 247 → 247 |
| 59 | [github-codebase-inspection](#skill-github-codebase-inspection) | 1.0.0 | P1 | 116 → 116 |
| 60 | [github-issues](#skill-github-issues) | 1.1.0 | P1 | 370 → 370 |
| 61 | [github-code-review](#skill-github-code-review) | 1.1.0 | P1 | 481 → 481 |
| 62 | [github-pr-workflow](#skill-github-pr-workflow) | 1.1.0 | P1 | 367 → 367 |
| 63 | [github-repo-management](#skill-github-repo-management) | 1.1.0 | P1 | 516 → 516 |
| 64 | [page-keeper](#skill-page-keeper) | 1.0.0 | P2 | 206 → 208 |
| 65 | [chen-academic-page-maintainer](#skill-chen-academic-page-maintainer) | 1.0.0 | P1 | 219 → 221 |
| 66 | [latent-identifiability](#skill-latent-identifiability) | 1.0.0 | P3 | 96 → 98 |
| 67 | [jepa-pytorch-development](#skill-jepa-pytorch-development) | 1.0.0 | P3 | 80 → 82 |
| 68 | [browser-use](#skill-browser-use) | 1.1.0 | P1 | 115 → 116 |
| 69 | [pytorch](#skill-pytorch) | 1.0.0 | P1 | 469 → 470 |
| 70 | [pytorch-lightning](#skill-pytorch-lightning) | 1.0.0 | P1 | 451 → 452 |
| 71 | [bitsandbytes](#skill-bitsandbytes) | 1.0.0 | P1 | 330 → 331 |
| 72 | [transformers](#skill-transformers) | 1.0.0 | P1 | 456 → 457 |
| 73 | [peft](#skill-peft) | 1.0.0 | P1 | 403 → 404 |
| 74 | [trl](#skill-trl) | 1.0.0 | P1 | 483 → 484 |
| 75 | [accelerate](#skill-accelerate) | 1.0.0 | P1 | 404 → 405 |
| 76 | [deepspeed](#skill-deepspeed) | 1.0.0 | P1 | 440 → 441 |
| 77 | [huggingface-hub](#skill-huggingface-hub) | 1.0.0 | P1 | 466 → 467 |
| 78 | [datasets](#skill-datasets) | 1.0.0 | P1 | 418 → 419 |
| 79 | [spatialdata](#skill-spatialdata) | 1.0.0 | P1 | 96 → 97 |
| 80 | [vitessce](#skill-vitessce) | 1.0.0 | P1 | 93 → 94 |
| 81 | [stereo-seq](#skill-stereo-seq) | 1.0.0 | P1 | 113 → 114 |
| 82 | [giotto](#skill-giotto) | 1.0.0 | P1 | 146 → 147 |
| 83 | [scribble](#skill-scribble) | 1.0.0 | P1 | 84 → 85 |
| 84 | [human-cell-atlas](#skill-human-cell-atlas) | 1.0.0 | P1 | 85 → 86 |
| 85 | [anndatar](#skill-anndatar) | 1.0.0 | P1 | 225 → 227 |
| 86 | [schard](#skill-schard) | 1.0.0 | P1 | 127 → 129 |
| 87 | [snakemake](#skill-snakemake) | 1.0.0 | P1 | 224 → 225 |
| 88 | [nextflow](#skill-nextflow) | 1.0.0 | P1 | 263 → 264 |
| 89 | [squidpy](#skill-squidpy) | 1.0.0 | P1 | 332 → 333 |
| 90 | [archr](#skill-archr) | 1.0.0 | P1 | 266 → 267 |
| 91 | [signac](#skill-signac) | 1.0.0 | P1 | 213 → 214 |
| 92 | [cellxgene](#skill-cellxgene) | 1.0.0 | P1 | 205 → 206 |
| 93 | [scanpy](#skill-scanpy) | 1.0.0 | P1 | 387 → 388 |
| 94 | [anndata](#skill-anndata) | 1.0.0 | P1 | 401 → 402 |
| 95 | [seurat](#skill-seurat) | 1.0.0 | P1 | 293 → 294 |
| 96 | [scvi-tools](#skill-scvi-tools) | 1.0.0 | P2 | 191 → 192 |
| 97 | [monocle3](#skill-monocle3) | 1.0.0 | P1 | 577 → 578 |
| 98 | [seurat-v5](#skill-seurat-v5) | 1.0.0 | P1 | 277 → 278 |
| 99 | [harmony](#skill-harmony) | 1.0.0 | P1 | 241 → 242 |
| 100 | [scanorama](#skill-scanorama) | 1.0.0 | P1 | 291 → 292 |
| 101 | [bbknn](#skill-bbknn) | 1.0.0 | P1 | 263 → 264 |
| 102 | [chimerax-mcp](#skill-chimerax-mcp) | 1.0.0 | P3 | 63 → 65 |
| 103 | [computational-biology-retrospective](#skill-computational-biology-retrospective) | 1.0.0 | P3 | 118 → 120 |
| 104 | [pydeseq2](#skill-pydeseq2) | 1.0.0 | P1 | 560 → 561 |
| 105 | [cellxgene-census](#skill-cellxgene-census) | 1.0.0 | P1 | 512 → 513 |
| 106 | [metabolomics-workbench](#skill-metabolomics-workbench) | 1.0.0 | P2 | 260 → 261 |
| 107 | [uniprot](#skill-uniprot) | 1.0.0 | P1 | 196 → 197 |
| 108 | [kegg](#skill-kegg) | 1.0.0 | P1 | 378 → 379 |
| 109 | [reactome](#skill-reactome) | 1.0.0 | P2 | 279 → 280 |
| 110 | [geo](#skill-geo) | 1.0.0 | P1 | 816 → 817 |
| 111 | [ensembl](#skill-ensembl) | 1.0.0 | P2 | 312 → 313 |

## Individual findings

<a id="skill-skill-cutter"></a>

### 1. skill-cutter — P2

Source: [skills-market/core/dev/skill-cutter/SKILL.md](../../skills-market/core/dev/skill-cutter/SKILL.md) · version `1.0.0`.

**Retain:** Separate audit from authorized edits; classify acceptance force and content; preserve action-specific risks and stop when the user outcome is established.

**Findings:** The body makes audit read-only, but the default UI prompt ends by asking to cut. The reporting list is useful for a substantial rewrite but unnecessarily uniform for a tiny edit.

**Keep / condense / move / delete:** Keep narrow metadata and explicit audit/cut modes. Make the UI default audit-only and offer cutting when requested; make before/after and gate reporting proportional to the actual revision.

**Trigger boundary:** Keep current concrete intents and nearby-task exclusion.

**Acceptance force:** Keep read-before-edit and authorization boundaries (action-required); retain risk-specific controls. Treat exhaustive classifications as report detail, not prerequisites to a bounded small edit.

**Stop condition:** Requested audit findings or authorized revision delivered with relevant verification; no mandatory further trimming.

**Evidence:**

- [skills-market/core/dev/skill-cutter/SKILL.md:15](../../skills-market/core/dev/skill-cutter/SKILL.md#L15) — `- **Audit:** When asked to review`: Read-only contract conflicts with the broader cut-oriented UI default.
- [skills-market/core/dev/skill-cutter/SKILL.md:120](../../skills-market/core/dev/skill-cutter/SKILL.md#L120) — `- before/after lines, words, and files;`: Reporting should scale with the change rather than block small edits.

<a id="skill-skill-creator"></a>

### 2. skill-creator — P1

Source: [skills-market/core/dev/skill-creator/SKILL.md](../../skills-market/core/dev/skill-creator/SKILL.md) · version `1.0.0`.

**Retain:** Capture intent, construct a self-contained skill, and use optional representative evaluations to improve behavior.

**Findings:** Mandates saving to an unrelated absolute repository and ~/.claude, including updates; this conflicts with canonical registry paths and can modify consumers outside the task. It explicitly recommends pushy broad triggers. Repeated full benchmark/viewer/review loops and provider-specific sections overwhelm simple creation tasks.

**Keep / condense / move / delete:** Delete the two-location policy and pushy trigger advice. Keep packaging/eval file contracts and conditional reference links; condense generic communication and economic motivation. Make eval/viewer workflows conditional on evaluation requests, preserve genuine iteration feedback, and define an explicit stop.

**Trigger boundary:** Split skill construction/evaluation from audit-only trimming handled by skill-cutter; require concrete intent rather than related product nouns.

**Acceptance force:** Requested artifact and necessary validation are action-required; comparison runs and viewer feedback are optional unless evaluation is the requested outcome. Do not require new user approval when intent and scope are already known.

**Stop condition:** The requested skill or evaluation report is delivered and relevant checks pass; user satisfaction is not an unbounded mandatory loop.

**Evidence:**

- [skills-market/core/dev/skill-creator/SKILL.md:76](../../skills-market/core/dev/skill-creator/SKILL.md#L76) — `ALWAYS save it to BOTH`: Incident-specific policy introduces unauthorized writes outside the current canonical repository.
- [skills-market/core/dev/skill-creator/SKILL.md:70](../../skills-market/core/dev/skill-creator/SKILL.md#L70) — `a little bit "pushy"`: Broad activation advice conflicts with deliberate trigger narrowing.
- [skills-market/core/dev/skill-creator/SKILL.md:344](../../skills-market/core/dev/skill-creator/SKILL.md#L344) — `The feedback is all empty`: Unbounded user-review loops should be optional evaluation workflows.

<a id="skill-security-audit"></a>

### 3. security-audit — P1

Source: [skills-market/core/security/security-audit/SKILL.md](../../skills-market/core/security/security-audit/SKILL.md) · version `1.0.0`.

**Retain:** Identify exploitable Python code and dependency risks, show evidence, and preserve containment checks and scoped remediation.

**Findings:** Quick start labels bandit -ll as high-only and maps B108 to path traversal. The dependency section includes pip-audit --fix without a distinct read-only audit/remediation boundary. The checklist turns minimal dependencies and weekly CI scanning into apparent acceptance requirements for every audit.

**Keep / condense / move / delete:** Verify and correct Bandit severity/identifier labels using primary docs; keep parameterization and path containment examples. Separate read-only findings from dependency-changing fixes. Condense generic checklists and make CI cadence follow-up advice.

**Trigger boundary:** Current Python security intent is specific; preserve scope and do not turn ordinary code edits into a security audit.

**Acceptance force:** Evidence for actual vulnerabilities and secret redaction are risk-triggered. Dependency modifications require task authorization. Weekly scanning and minimizing dependencies are optional recommendations, not audit completion gates.

**Stop condition:** Scoped risks and remediation options reported with evidence; no CI rollout or dependency update is required for a read-only audit.

**Evidence:**

- [skills-market/core/security/security-audit/SKILL.md:15](../../skills-market/core/security/security-audit/SKILL.md#L15) — `bandit -r src/ -ll`: Severity comment needs correction against Bandit CLI semantics.
- [skills-market/core/security/security-audit/SKILL.md:43](../../skills-market/core/security/security-audit/SKILL.md#L43) — `Path traversal | B108`: Bandit rule mapping needs correction.
- [skills-market/core/security/security-audit/SKILL.md:31](../../skills-market/core/security/security-audit/SKILL.md#L31) — `pip-audit --fix`: Mutation is mixed into an audit workflow.
- [skills-market/core/security/security-audit/SKILL.md:95](../../skills-market/core/security/security-audit/SKILL.md#L95) — `Weekly dependency scan`: Recurring infrastructure work is advice unless requested.

Primary documentation checked: [Bandit severity flags](https://bandit.readthedocs.io/en/latest/man/bandit.html), [Bandit B108](https://bandit.readthedocs.io/en/latest/plugins/b108_hardcoded_tmp_directory.html).

<a id="skill-codex"></a>

### 4. codex — P1

Source: [skills-market/agents/codex/SKILL.md](../../skills-market/agents/codex/SKILL.md) · version `1.0.0`.

**Retain:** Run an explicitly delegated coding/review task with bounded capabilities and report results.

**Findings:** Requires Hermes-only terminal/process APIs, insists on a PTY for non-interactive exec, says git checks cannot be skipped, and recommends --yolo plus commits/pushes in ordinary batch examples. Local codex exec --help explicitly supports non-interactive execution and --skip-git-repo-check.

**Keep / condense / move / delete:** Keep task isolation and result monitoring. Replace host-specific tool calls with discovered tools, use supported help-confirmed flags, remove bypass as a default, and keep commits/publication within requested authorization. Remove archived related-skill names.

**Trigger boundary:** Require explicit delegation to Codex; exclude ordinary coding already handled by the current agent.

**Acceptance force:** Capability and scope checks are risk-triggered; PTY and a scratch git init are not universal prerequisites.

**Stop condition:** Delegated task finishes and its relevant result is verified; no automatic push or PR comment.

**Evidence:**

- [skills-market/agents/codex/SKILL.md:108](../../skills-market/agents/codex/SKILL.md#L108) — ``Always use `pty=true```: Conflicts with documented non-interactive exec.
- [skills-market/agents/codex/SKILL.md:78](../../skills-market/agents/codex/SKILL.md#L78) — `codex --yolo exec`: Permission bypass is bundled with otherwise ordinary work.

Primary documentation checked: [Codex non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).

<a id="skill-claude-code"></a>

### 5. claude-code — P1

Source: [skills-market/agents/claude-code/SKILL.md](../../skills-market/agents/claude-code/SKILL.md) · version `2.2.0`.

**Retain:** Delegate explicitly requested work using print mode or an interactive session, observe status, and return results.

**Findings:** Automatically accepts workspace trust and permission-bypass dialogs. Describes allowedTools as a capability whitelist, although current official docs describe auto-approval; restriction is a separate concern. Extensive flags, hooks, keyboard shortcuts, and speculative context-quality thresholds obscure the delegation workflow. Hermes references include archived skills.

**Keep / condense / move / delete:** Keep mode choice, scoped tool use, exit/result handling, and auth discovery. Delete blind trust/bypass acceptance. Verify permissions against current docs, move genuinely conditional orchestration detail, and delete unsubstantiated universal context thresholds and duplicated catalogs.

**Trigger boundary:** Use for explicit Claude Code delegation/configuration; exclude generic coding.

**Acceptance force:** User authorization for external changes and trust are risk-triggered; tmux is a possible adapter, not a provider-wide prerequisite.

**Stop condition:** The delegated result is complete and checked; no automatic retries, trust acceptance, or publication.

**Evidence:**

- [skills-market/agents/claude-code/SKILL.md:90](../../skills-market/agents/claude-code/SKILL.md#L90) — `default selection is correct.`: Workspace trust is treated as an automatic choice.
- [skills-market/agents/claude-code/SKILL.md:99](../../skills-market/agents/claude-code/SKILL.md#L99) — `Down && sleep 0.3`: Blind acceptance of permission bypass.
- [skills-market/agents/claude-code/SKILL.md:280](../../skills-market/agents/claude-code/SKILL.md#L280) — `Whitelist specific tools`: Auto-approval versus available-tool restriction must be distinguished.
- [skills-market/agents/claude-code/SKILL.md:692](../../skills-market/agents/claude-code/SKILL.md#L692) — `Hallucination risk spikes`: Quantitative claim lacks supporting evidence.

Primary documentation checked: [Claude Code programmatic use](https://code.claude.com/docs/en/headless).

<a id="skill-karpathy-guidelines"></a>

### 6. karpathy-guidelines — P2

Source: [skills-market/agents/guidelines/karpathy-guidelines/SKILL.md](../../skills-market/agents/guidelines/karpathy-guidelines/SKILL.md) · version `1.0.0`.

**Retain:** Keep changes scoped, avoid speculative abstractions, and define evidence of success.

**Findings:** The trigger covers nearly all coding and repeats higher-level repository/agent instructions. Unconditional stopping for ambiguity and tests-first examples can block low-impact tasks.

**Keep / condense / move / delete:** Keep as an explicitly selected review checklist or repository policy. Condense repeated general advice and make clarification/tests proportional to uncertainty and risk.

**Trigger boundary:** Narrow to explicit overengineering/scope review rather than all code writing.

**Acceptance force:** Relevant correctness verification is action-required; a new test and clarification are not universal gates.

**Stop condition:** Scoped implementation meets the requested behavior and relevant checks pass.

**Evidence:**

- [skills-market/agents/guidelines/karpathy-guidelines/SKILL.md:4](../../skills-market/agents/guidelines/karpathy-guidelines/SKILL.md#L4) — `Use when writing, reviewing, or refactoring code`: Near-universal activation overlaps repository policy.
- [skills-market/agents/guidelines/karpathy-guidelines/SKILL.md:24](../../skills-market/agents/guidelines/karpathy-guidelines/SKILL.md#L24) — `If something is unclear, stop.`: Needs an uncertainty/materiality threshold.

<a id="skill-mcp-builder"></a>

### 7. mcp-builder — P2

Source: [skills-market/agents/mcp/mcp-builder/SKILL.md](../../skills-market/agents/mcp/mcp-builder/SKILL.md) · version `1.0.0`.

**Retain:** Design usable MCP schemas, annotations, pagination, transports, and test actual tool calls.

**Findings:** Defaults to comprehensive API coverage and always adds ten complex evaluation questions, even for a small server. A draft-spec URL and SDK examples need version-specific verification.

**Keep / condense / move / delete:** Keep schema/error/transport constraints; condense generic phases; make benchmark generation optional and scope endpoints to the user's workflow. Preserve scripts until their evaluation callers are inspected.

**Trigger boundary:** Keep explicit server-building intent; exclude merely using an existing MCP tool.

**Evidence:**

- [skills-market/agents/mcp/mcp-builder/SKILL.md:77](../../skills-market/agents/mcp/mcp-builder/SKILL.md#L77) — `Prioritize comprehensive API coverage.`: Opportunity is promoted to implementation scope.
- [skills-market/agents/mcp/mcp-builder/SKILL.md:164](../../skills-market/agents/mcp/mcp-builder/SKILL.md#L164) — `Create 10 Evaluation Questions`: Fixed evaluation count is not a correctness requirement for every server.

<a id="skill-api-design"></a>

### 8. api-design — P2

Source: [skills-market/programming/python/api-design/SKILL.md](../../skills-market/programming/python/api-design/SKILL.md) · version `1.0.0`.

**Retain:** Preserve caller compatibility, explicit parameter semantics, and actionable exception contracts.

**Findings:** Mostly generic Python advice with a registry/frontmatter name mismatch; incomplete illustrative snippets can be mistaken for runnable examples.

**Keep / condense / move / delete:** Keep compatibility and deprecation decision rules; condense naming/checklist repetition; label snippets or provide one runnable example. Normalize the stable skill name deliberately with installation aliases considered.

**Trigger boundary:** Retain public-interface design intent; distinguish from whole-library review.

**Evidence:**

- [skills-market/programming/python/api-design/SKILL.md:2](../../skills-market/programming/python/api-design/SKILL.md#L2) — `name: designing-python-apis`: Frontmatter identity differs from registry api-design.

<a id="skill-cli-development"></a>

### 9. cli-development — P2

Source: [skills-market/programming/python/cli-development/SKILL.md](../../skills-market/programming/python/cli-development/SKILL.md) · version `1.0.0`.

**Retain:** Design input/output streams, exit codes, package entry points, and representative CLI tests.

**Findings:** Trigger includes any mention of a command-line tool. Tests call a required-existing input path without creating a fixture; Click is declared recommended regardless of project needs.

**Keep / condense / move / delete:** Narrow to Python CLI implementation. Keep stream/exit contracts, make framework choice contextual, and repair example fixture setup; condense generic checklist.

**Trigger boundary:** Exclude simply running an existing terminal command.

**Evidence:**

- [skills-market/programming/python/cli-development/SKILL.md:4](../../skills-market/programming/python/cli-development/SKILL.md#L4) — `whenever a user mentions a command-line tool`: Routing overlaps every terminal-based workflow.
- [skills-market/programming/python/cli-development/SKILL.md:81](../../skills-market/programming/python/cli-development/SKILL.md#L81) — `runner.invoke(cli, ['process', 'input.txt'])`: Example needs an isolated real input fixture.

<a id="skill-code-quality"></a>

### 10. code-quality — P2

Source: [skills-market/programming/python/code-quality/SKILL.md](../../skills-market/programming/python/code-quality/SKILL.md) · version `1.0.0`.

**Retain:** Apply requested lint/type changes with repository-consistent configuration.

**Findings:** Forces strict mypy/py.typed defaults and Python 3.10 conventions without checking existing targets; generic idioms repeat normal model knowledge.

**Keep / condense / move / delete:** Keep targeted diagnostics and public typing decisions, condense basic syntax, and treat stricter policies as recommendations. Preserve caller-owned empty containers rather than routinely replacing them with items or [].

**Trigger boundary:** Keep explicit Python quality tasks; exclude unrelated cleanup during narrow fixes.

**Evidence:**

- [skills-market/programming/python/code-quality/SKILL.md:123](../../skills-market/programming/python/code-quality/SKILL.md#L123) — `mypy passes (strict mode)`: Project policy is presented as a universal completion gate.

<a id="skill-community"></a>

### 11. community — P2

Source: [skills-market/programming/python/community/SKILL.md](../../skills-market/programming/python/community/SKILL.md) · version `1.0.0`.

**Retain:** Create contributor/governance artifacts appropriate to the requested project.

**Findings:** Dictates commit prefixes, response SLAs, and a full community stack. The workflow example should be verified with current action inputs and least-required token permissions before reuse.

**Keep / condense / move / delete:** Keep conditional templates and ownership decisions; delete invented universal SLAs and commit policy; separate drafting from publishing welcome messages or changing labels.

**Trigger boundary:** Current governance/contributor intent is appropriate.

**Evidence:**

- [skills-market/programming/python/community/SKILL.md:120](../../skills-market/programming/python/community/SKILL.md#L120) — `Respond to issues within 48h`: Organization-specific service target masquerades as required policy.

<a id="skill-documentation"></a>

### 12. documentation — P2

Source: [skills-market/programming/python/documentation/SKILL.md](../../skills-market/programming/python/documentation/SKILL.md) · version `1.0.0`.

**Retain:** Document real public behavior and build the requested documentation accurately.

**Findings:** Broad mention-based trigger; assumes Google docstrings, Furo, Sphinx, and a full public API checklist even when editing one docstring.

**Keep / condense / move / delete:** Keep build/config references conditionally; honor the project's existing style and limit checks to the requested surface. Condense generic README material.

**Trigger boundary:** Require Python documentation work rather than any mention of tutorials or API docs.

**Evidence:**

- [skills-market/programming/python/documentation/SKILL.md:11](../../skills-market/programming/python/documentation/SKILL.md#L11) — `## Docstring Style (Google)`: A house-style example needs to remain optional.

<a id="skill-jupyter"></a>

### 13. jupyter — P2

Source: [skills-market/programming/python/jupyter/SKILL.md](../../skills-market/programming/python/jupyter/SKILL.md) · version `1.0.0`.

**Retain:** Edit notebook structure while preserving metadata, outputs, and intended execution state.

**Findings:** Defaults to in-place execution and raw JSON editing without distinguishing inspection from executing arbitrary notebook code. New-cell examples omit version-aware notebook validation.

**Keep / condense / move / delete:** Keep output-clearing semantics; prefer nbformat for structural validation and execute only when requested, with an explicit output path when preservation matters. Narrow noun-only activation.

**Trigger boundary:** Exclude merely discussing a notebook; require notebook reading/editing/execution intent.

**Evidence:**

- [skills-market/programming/python/jupyter/SKILL.md:32](../../skills-market/programming/python/jupyter/SKILL.md#L32) — `--execute --inplace`: Execution and overwrite should not be the default for read-only inspection.

<a id="skill-library-review"></a>

### 14. library-review — P1

Source: [skills-market/programming/python/library-review/SKILL.md](../../skills-market/programming/python/library-review/SKILL.md) · version `1.0.0`.

**Retain:** Produce evidence-backed, scoped assessment of library health and material adoption risks.

**Findings:** Quick review runs arbitrary tests and installs packages before establishing an isolated environment. Coverage thresholds disagree across sections; last-commit age alone is treated as a defect.

**Keep / condense / move / delete:** Start with static evidence; gate code execution on the source/environment risk. Replace star ratings and conflicting 70/80/85 thresholds with justified findings; distinguish recommendation from release blockers.

**Trigger boundary:** Keep explicit package audit intent.

**Evidence:**

- [skills-market/programming/python/library-review/SKILL.md:17](../../skills-market/programming/python/library-review/SKILL.md#L17) — `pytest --cov=package`: Running reviewed repository code is an execution action, not mere inspection.
- [skills-market/programming/python/library-review/SKILL.md:41](../../skills-market/programming/python/library-review/SKILL.md#L41) — `Last commit > 1 year ago`: Maintenance age alone does not establish unsuitability.

<a id="skill-packaging"></a>

### 15. packaging — P1

Source: [skills-market/programming/python/packaging/SKILL.md](../../skills-market/programming/python/packaging/SKILL.md) · version `1.0.0`.

**Retain:** Build installable artifacts with correct metadata/data inclusion and verify clean installation.

**Findings:** Packaging trigger overlaps any pyproject edit. Build examples invoke twine without installing it; ordinary packaging guidance flows directly into production upload and GitHub release acceptance.

**Keep / condense / move / delete:** Separate build/validation from authorized publishing; keep package-data and clean-install checks. Make license/build-backend examples contextual and verify current metadata conventions before replacing them.

**Trigger boundary:** Exclude lint-only pyproject changes; require packaging or distribution intent.

**Evidence:**

- [skills-market/programming/python/packaging/SKILL.md:61](../../skills-market/programming/python/packaging/SKILL.md#L61) — `twine upload dist/*`: Publication is a separate authorized outcome.
- [skills-market/programming/python/packaging/SKILL.md:127](../../skills-market/programming/python/packaging/SKILL.md#L127) — `GitHub release created`: Not required for a wheel-building request.

<a id="skill-performance"></a>

### 16. performance — P2

Source: [skills-market/programming/python/performance/SKILL.md](../../skills-market/programming/python/performance/SKILL.md) · version `1.0.0`.

**Retain:** Measure representative bottlenecks and verify correctness and performance after a change.

**Findings:** Broad rules and a complexity table omit index-versus-value lookup and amortized costs; universal regression-benchmark addition expands small profiling tasks.

**Keep / condense / move / delete:** Keep measurements and resource evidence; qualify table operations and move basic Python optimization recipes to optional reading. Add a regression check only when it can protect the changed behavior.

**Trigger boundary:** Retain measured Python performance intent.

**Evidence:**

- [skills-market/programming/python/performance/SKILL.md:95](../../skills-market/programming/python/performance/SKILL.md#L95) — `| Lookup | O(n)`: List indexed access differs from membership lookup.
- [skills-market/programming/python/performance/SKILL.md:118](../../skills-market/programming/python/performance/SKILL.md#L118) — `Add benchmarks to prevent regression`: A recommendation should not gate every profiling-only answer.

<a id="skill-project-setup"></a>

### 17. project-setup — P1

Source: [skills-market/programming/python/project-setup/SKILL.md](../../skills-market/programming/python/project-setup/SKILL.md) · version `1.0.0`.

**Retain:** Create a usable package scaffold without overwriting existing work.

**Findings:** Required setup steps include pre-commit, but generated dev dependencies omit it. Helper writes LICENSE as only 'MIT License' and interpolates author text into TOML without escaping. A generic scaffold installs a fixed full tool stack.

**Keep / condense / move / delete:** Keep refusal to overwrite; repair incomplete license/dependency metadata and validate generated TOML. Make scaffolding choices follow the user's targets; consolidate duplicate templates with helper output.

**Trigger boundary:** Use for explicit package creation/modernization, not every repository change.

**Evidence:**

- [skills-market/programming/python/project-setup/SKILL.md:64](../../skills-market/programming/python/project-setup/SKILL.md#L64) — `pre-commit install`: The helper's generated dev extra does not install this advertised prerequisite.
- [skills-market/programming/python/project-setup/SKILL.md:100](../../skills-market/programming/python/project-setup/SKILL.md#L100) — `python scripts/create_project.py`: Helper inspection confirms incomplete license text and unescaped TOML interpolation.

<a id="skill-release-management"></a>

### 18. release-management — P1

Source: [skills-market/programming/python/release-management/SKILL.md](../../skills-market/programming/python/release-management/SKILL.md) · version `1.0.0`.

**Retain:** Prepare a coherent version/changelog/artifact release and publish only the intended ref/artifacts.

**Findings:** Example git commit -am can include unrelated tracked edits and git push origin main --tags publishes every local tag. It conflates release preparation with publication.

**Keep / condense / move / delete:** Keep version/deprecation compatibility decisions; use explicit staged paths and a single release ref after scope is established. Separate preparation from requested publication, and verify built artifact identity.

**Trigger boundary:** Keep release intent; a changelog-only edit must not trigger publishing.

**Evidence:**

- [skills-market/programming/python/release-management/SKILL.md:102](../../skills-market/programming/python/release-management/SKILL.md#L102) — `git commit -am`: Broad staging can include unrelated work.
- [skills-market/programming/python/release-management/SKILL.md:104](../../skills-market/programming/python/release-management/SKILL.md#L104) — `git push origin main --tags`: All local tags exceed a single-release scope.

<a id="skill-sqlite"></a>

### 19. sqlite — P1

Source: [skills-market/programming/python/sqlite/SKILL.md](../../skills-market/programming/python/sqlite/SKILL.md) · version `1.0.0`.

**Retain:** Preserve transaction integrity, valid backups, and workload-aware concurrency decisions.

**Findings:** Says BEGIN EXCLUSIVE blocks all connections without its WAL exception; treats all concurrent-user web apps as unsuitable; prescribes VACUUM after every bulk deletion; mixes raw WAL file copying with safe backup APIs.

**Keep / condense / move / delete:** Keep per-connection foreign keys and backup APIs. Verify WAL-specific locking and backup constraints against SQLite docs; replace categorical suitability/performance claims with workload conditions and maintenance as optional.

**Trigger boundary:** Add concrete schema/backup/concurrency intents; normalize uppercase name only with compatibility considered.

**Evidence:**

- [skills-market/programming/python/sqlite/SKILL.md:70](../../skills-market/programming/python/sqlite/SKILL.md#L70) — `blocks all other connections`: Transaction locking depends on journal mode.
- [skills-market/programming/python/sqlite/SKILL.md:50](../../skills-market/programming/python/sqlite/SKILL.md#L50) — `After bulk deletes, always vacuum`: Maintenance is promoted to a universal prerequisite.
- [skills-market/programming/python/sqlite/SKILL.md:75](../../skills-market/programming/python/sqlite/SKILL.md#L75) — `Using SQLite for web app with concurrent users`: Workload suitability is overgeneralized.

Primary documentation checked: [SQLite transaction modes](https://sqlite.org/lang_transaction.html).

<a id="skill-testing-strategy"></a>

### 20. testing-strategy — P2

Source: [skills-market/programming/python/testing-strategy/SKILL.md](../../skills-market/programming/python/testing-strategy/SKILL.md) · version `1.0.0`.

**Retain:** Test meaningful observable behavior with appropriate fixtures, isolation, and error coverage.

**Findings:** Mandates 85% coverage and sub-100ms unit tests as universal standards. Mocker example requires pytest-mock but prerequisites are not stated.

**Keep / condense / move / delete:** Keep behavioral tests and deterministic fixtures; make coverage/speed targets project policy, document plugin requirements, and avoid generating tests that merely mirror implementation.

**Trigger boundary:** Keep explicit test-design intent; exclude unrelated coding changes.

**Evidence:**

- [skills-market/programming/python/testing-strategy/SKILL.md:26](../../skills-market/programming/python/testing-strategy/SKILL.md#L26) — `--cov-fail-under=85`: Illustrative threshold becomes a blocking default.
- [skills-market/programming/python/testing-strategy/SKILL.md:75](../../skills-market/programming/python/testing-strategy/SKILL.md#L75) — `def test_api_call(mocker):`: Requires an additional fixture-providing plugin.

<a id="skill-officecli"></a>

### 21. officecli — P2

Source: [skills-market/documents/office/officecli/SKILL.md](../../skills-market/documents/office/officecli/SKILL.md) · version `1.0.0`.

**Retain:** Inspect existing files, use supported DOM operations before raw XML, and validate the changed document.

**Findings:** Broad format-based trigger competes with three specialized adapters and generic format skills. Local binary location and three-operation resident-mode rule are user/environment choices.

**Keep / condense / move / delete:** Make this the explicit OfficeCLI backend router, discover installed help/version, retain structural validation, and treat resident/batch mode as optimization advice.

**Trigger boundary:** Use when OfficeCLI is requested or selected as the available backend; delegate the format contract to one owner.

**Evidence:**

- [skills-market/documents/office/officecli/SKILL.md:11](../../skills-market/documents/office/officecli/SKILL.md#L11) — `Use the local binary at`: Machine-specific executable location should be a fallback.

<a id="skill-officecli-docx"></a>

### 22. officecli-docx — P2

Source: [skills-market/documents/office/officecli-docx/SKILL.md](../../skills-market/documents/office/officecli-docx/SKILL.md) · version `1.0.0`.

**Retain:** Preserve Word styles and use quoted paths, supported operations, and relevant validation.

**Findings:** Any-time DOCX trigger collides directly with docx and officecli despite the adapter being concise.

**Keep / condense / move / delete:** Keep format-specific path/style pitfalls and references; narrow activation to the OfficeCLI backend. Keep rendering validation conditional on layout changes.

**Trigger boundary:** OfficeCLI Word tasks only, not all DOCX mentions.

**Evidence:**

- [skills-market/documents/office/officecli-docx/SKILL.md:4](../../skills-market/documents/office/officecli-docx/SKILL.md#L4) — ``any time a `.docx` file is involved``: Backend-specific adapter claims the whole format.

<a id="skill-officecli-pptx"></a>

### 23. officecli-pptx — P2

Source: [skills-market/documents/office/officecli-pptx/SKILL.md](../../skills-market/documents/office/officecli-pptx/SKILL.md) · version `1.0.0`.

**Retain:** Respect shape-index changes, quoted paths, and visual validation of modified slides.

**Findings:** Any-time PPTX trigger duplicates generic deck tooling and would also compete with a requested Marp workflow.

**Keep / condense / move / delete:** Keep z-order/path failure modes and concise references; activate only for OfficeCLI PPTX operations and verify help examples in the installed binary before reuse.

**Trigger boundary:** Exclude Marp, Google Slides, and alternate PPTX backends unless conversion is requested.

**Evidence:**

- [skills-market/documents/office/officecli-pptx/SKILL.md:4](../../skills-market/documents/office/officecli-pptx/SKILL.md#L4) — ``any time a `.pptx` file is involved``: Backend routing is broader than the actual implementation.

<a id="skill-officecli-xlsx"></a>

### 24. officecli-xlsx — P2

Source: [skills-market/documents/office/officecli-xlsx/SKILL.md](../../skills-market/documents/office/officecli-xlsx/SKILL.md) · version `1.0.0`.

**Retain:** Preserve formulas and cross-sheet dependencies while using supported cell operations.

**Findings:** Any-time XLSX trigger overlaps xlsx; formula-error queries and resident-mode choices need to remain targeted to changed ranges.

**Keep / condense / move / delete:** Keep quoted paths and formula checks; narrow to OfficeCLI workbook editing and avoid repeated whole-file QA for a bounded edit.

**Trigger boundary:** Explicit or selected OfficeCLI spreadsheet backend.

**Evidence:**

- [skills-market/documents/office/officecli-xlsx/SKILL.md:4](../../skills-market/documents/office/officecli-xlsx/SKILL.md#L4) — ``any time a `.xlsx` file is involved``: Duplicates the generic spreadsheet skill's responsibility.

<a id="skill-docx"></a>

### 25. docx — P2

Source: [skills-market/documents/formats/docx/SKILL.md](../../skills-market/documents/formats/docx/SKILL.md) · version `1.0.0`.

**Retain:** Preserve OOXML relationships, tracked-change semantics, table geometry, and document validity.

**Findings:** A long docx-js tutorial repeats its rules and embeds universal aesthetic choices and a ban on Python XML editing. Structural validation is detailed but an explicit visual acceptance step is weaker than the layout risk warrants.

**Keep / condense / move / delete:** Keep fragile XML/redlining constraints and helper scripts. Condense duplicate API recipes, load creation/XML detail conditionally, remove method/style mandates unsupported by the requested artifact, and use rendering for layout-sensitive changes.

**Trigger boundary:** Require actual Word artifact work; distinguish read-only extraction from formatting and backend selection.

**Evidence:**

- [skills-market/documents/formats/docx/SKILL.md:417](../../skills-market/documents/formats/docx/SKILL.md#L417) — `Do not write Python scripts.`: Implementation preference is promoted to universal prohibition.
- [skills-market/documents/formats/docx/SKILL.md:381](../../skills-market/documents/formats/docx/SKILL.md#L381) — `### Critical Rules for docx-js`: Duplicates many preceding recipe constraints; preserve each unique failure mode once.

<a id="skill-pdf"></a>

### 26. pdf — P1

Source: [skills-market/documents/formats/pdf/SKILL.md](../../skills-market/documents/formats/pdf/SKILL.md) · version `1.0.0`.

**Retain:** Choose extraction/OCR/forms/layout operations based on the PDF and preserve page/form geometry.

**Findings:** Routes to uppercase REFERENCE.md and FORMS.md while the files are lowercase; this breaks case-sensitive installations. Basic recipes dominate and quick extraction concatenates values without handling missing text. Unicode font advice is broader than the stated built-in-font limitation.

**Keep / condense / move / delete:** Repair exact-case resource contracts first; keep form-specific scripts and rendering evidence. Condense basic API tutorials, handle scanned/missing text, and distinguish fonts with supported glyphs from built-in limitations.

**Trigger boundary:** Require PDF work rather than a filename mention alone; retain forms routing.

**Evidence:**

- [skills-market/documents/formats/pdf/SKILL.md:14](../../skills-market/documents/formats/pdf/SKILL.md#L14) — `see REFERENCE.md`: Actual resource basename is reference.md.
- [skills-market/documents/formats/pdf/SKILL.md:14](../../skills-market/documents/formats/pdf/SKILL.md#L14) — `read FORMS.md`: Actual resource basename is forms.md.
- [skills-market/documents/formats/pdf/SKILL.md:28](../../skills-market/documents/formats/pdf/SKILL.md#L28) — `text += page.extract_text()`: Needs a missing-text/OCR branch.

<a id="skill-pptx"></a>

### 27. pptx — P1

Source: [skills-market/documents/formats/pptx/SKILL.md](../../skills-market/documents/formats/pptx/SKILL.md) · version `1.0.0`.

**Retain:** Preserve deck/template content and verify visual readability and file integrity.

**Findings:** Requires finding and fixing an issue even when the initial output passes; insists on subagents for tiny decks; turns subjective motifs and palette preferences into universal rules. Broad slides trigger also claims non-PPTX workflows.

**Keep / condense / move / delete:** Keep rendering, template fidelity, overflow/citation checks and package helpers. Delete compulsory invented-fault/fix cycles; make independent review optional and aesthetic choices subordinate to user templates.

**Trigger boundary:** Actual PPTX artifact tasks; exclude Marp decks and general presentation advice.

**Acceptance force:** Relevant visual/content integrity checks are action-required. A mandatory fix or subagent pass is not evidence of correctness and should not block acceptance.

**Stop condition:** Requested content passes relevant structural and visual checks, even if the first render is already correct.

**Evidence:**

- [skills-market/documents/formats/pptx/SKILL.md:168](../../skills-market/documents/formats/pptx/SKILL.md#L168) — `USE SUBAGENTS`: Unconditional resource requirement is disproportionate.
- [skills-market/documents/formats/pptx/SKILL.md:206](../../skills-market/documents/formats/pptx/SKILL.md#L206) — `at least one fix-and-verify cycle`: Requires a mutation even after a clean initial result.
- [skills-market/documents/formats/pptx/SKILL.md:84](../../skills-market/documents/formats/pptx/SKILL.md#L84) — `Every slide needs a visual element`: Subjective recommendation becomes a universal artifact rule.

<a id="skill-xlsx"></a>

### 28. xlsx — P1

Source: [skills-market/documents/formats/xlsx/SKILL.md](../../skills-market/documents/formats/xlsx/SKILL.md) · version `1.0.0`.

**Retain:** Preserve workbook formulas/templates, validate changed calculations, and keep sources and units interpretable.

**Findings:** Requires LibreOffice and its macro configuration for every formula workflow, assumes installation, applies financial presentation conventions broadly, and treats every error cell as necessarily unintended. Opening/saving with other engines can have workbook feature consequences. The inspected recalc helper overwrites an existing user-profile Module1.xba unless it already contains the macro name, and continues after timeout exit 124 without proving recalculation completed.

**Keep / condense / move / delete:** Keep formula preservation, source provenance, and changed-cell checks. Discover a suitable recalculation engine and replace persistent macro overwrites with isolated setup and fail on incomplete recalculation; make financial styling conditional and distinguish intentional error signals from new defects. Scope QA to affected dependency ranges unless full verification is requested.

**Trigger boundary:** Good primary-artifact boundary; coordinate explicit backend choice with OfficeCLI.

**Evidence:**

- [skills-market/documents/formats/xlsx/SKILL.md:77](../../skills-market/documents/formats/xlsx/SKILL.md#L77) — `You can assume LibreOffice is installed`: Environment assumption needs discovery.
- [skills-market/documents/formats/xlsx/SKILL.md:224](../../skills-market/documents/formats/xlsx/SKILL.md#L224) — `Automatically sets up LibreOffice macro`: Persistent helper setup requires inspection and scoped use.
- [skills-market/documents/formats/xlsx/SKILL.md:133](../../skills-market/documents/formats/xlsx/SKILL.md#L133) — `This applies to ALL calculations`: Dynamic-model requirement overreaches static analysis exports.
- [skills-market/documents/formats/xlsx/scripts/recalc.py:64](../../skills-market/documents/formats/xlsx/scripts/recalc.py#L64) — `Path(macro_file).write_text(RECALCULATE_MACRO)`: Can overwrite a user macro module in the shared LibreOffice profile.
- [skills-market/documents/formats/xlsx/scripts/recalc.py:94](../../skills-market/documents/formats/xlsx/scripts/recalc.py#L94) — `result.returncode != 124`: Timeout is allowed to continue into reading existing cached values.

<a id="skill-algorithmic-art"></a>

### 29. algorithmic-art — P1

Source: [skills-market/documents/design/algorithmic-art/SKILL.md](../../skills-market/documents/design/algorithmic-art/SKILL.md) · version `1.0.0`.

**Retain:** Create reproducible generative artwork with working seed and parameter controls.

**Findings:** Requires a four-to-six-paragraph manifesto, repeated craftsmanship claims, fixed Anthropic branding, and a template for every request; says user instructions should not constrain creative freedom. Output guidance conflicts about separate JS versus inline-only HTML and claims CDN output is wholly self-contained.

**Keep / condense / move / delete:** Delete invented creative ceremony and user-scope override. Keep seeded generation, working controls and template contracts when that template is requested; make branding optional and disclose network dependencies.

**Trigger boundary:** Keep code-generated art intent; distinguish static bitmap generation.

**Evidence:**

- [skills-market/documents/design/algorithmic-art/SKILL.md:27](../../skills-market/documents/design/algorithmic-art/SKILL.md#L27) — `it should not constrain creative freedom`: User requirements must remain authoritative.
- [skills-market/documents/design/algorithmic-art/SKILL.md:52](../../skills-market/documents/design/algorithmic-art/SKILL.md#L52) — `Emphasize craftsmanship REPEATEDLY`: Filler is explicitly mandated.

<a id="skill-canvas-design"></a>

### 30. canvas-design — P1

Source: [skills-market/documents/design/canvas-design/SKILL.md](../../skills-market/documents/design/canvas-design/SKILL.md) · version `1.0.0`.

**Retain:** Produce a readable static design that preserves requested content and fits the output canvas.

**Findings:** Fabricates a prior user demand for perfection, requires an extra polish pass and a manifesto, and imposes minimal-text and non-cartoon style regardless of the brief.

**Keep / condense / move / delete:** Delete fabricated user speech and mandatory philosophy/craftsmanship repetition. Keep actual clipping/readability checks, bundled font routing and scope-faithful design choices; make styles optional.

**Trigger boundary:** Narrow static artifact intent; distinguish scientific figure editing and web UI.

**Stop condition:** The requested artifact meets its content/layout requirements; a clean first result does not require an invented revision.

**Evidence:**

- [skills-market/documents/design/canvas-design/SKILL.md:125](../../skills-market/documents/design/canvas-design/SKILL.md#L125) — `The user ALREADY said`: Invents user intent and escalates the acceptance criterion.
- [skills-market/documents/design/canvas-design/SKILL.md:51](../../skills-market/documents/design/canvas-design/SKILL.md#L51) — `Emphasize craftsmanship REPEATEDLY`: Repeated quality rhetoric does not change execution correctly.

<a id="skill-frontend-design"></a>

### 31. frontend-design — P2

Source: [skills-market/documents/design/frontend-design/SKILL.md](../../skills-market/documents/design/frontend-design/SKILL.md) · version `1.0.0`.

**Retain:** Build functioning, context-appropriate interfaces with coherent visual hierarchy.

**Findings:** Blanket font bans, mandatory novelty and extreme aesthetics can conflict with existing design systems or accessibility. Broad trigger includes posters and any UI styling.

**Keep / condense / move / delete:** Retain context, functionality and visual hierarchy; condense promotional language, make visual choices recommendations, and explicitly preserve existing branding and reduced-motion/accessibility needs.

**Trigger boundary:** Web interface design tasks only; exclude static posters and small non-design code changes.

**Evidence:**

- [skills-market/documents/design/frontend-design/SKILL.md:39](../../skills-market/documents/design/frontend-design/SKILL.md#L39) — `NEVER use generic AI-generated aesthetics`: Subjective aesthetic preference is expressed as universal policy.

<a id="skill-brand-guidelines"></a>

### 32. brand-guidelines — P2

Source: [skills-market/documents/design/brand-guidelines/SKILL.md](../../skills-market/documents/design/brand-guidelines/SKILL.md) · version `1.0.0`.

**Retain:** Apply the specifically requested Anthropic palette and typography consistently.

**Findings:** Generic company-branding trigger can apply Anthropic styling to unrelated brands. Claims automatic font handling despite containing only prose and a license.

**Keep / condense / move / delete:** Narrow to explicit Anthropic branding, describe palette as a versioned reference, remove implied executable capabilities, and keep font fallback conditional.

**Trigger boundary:** Exclude general corporate design, Duke-NUS branding and user-supplied style guides.

**Evidence:**

- [skills-market/documents/design/brand-guidelines/SKILL.md:4](../../skills-market/documents/design/brand-guidelines/SKILL.md#L4) — `when brand colors or style guidelines`: Generic branding does not imply Anthropic identity.
- [skills-market/documents/design/brand-guidelines/SKILL.md:47](../../skills-market/documents/design/brand-guidelines/SKILL.md#L47) — `Automatically falls back`: No implementation is bundled to provide this automatic behavior.

<a id="skill-theme-factory"></a>

### 33. theme-factory — P2

Source: [skills-market/documents/design/theme-factory/SKILL.md](../../skills-market/documents/design/theme-factory/SKILL.md) · version `1.0.0`.

**Retain:** Apply a chosen palette/font specification while preserving readability and requested branding.

**Findings:** Always shows a showcase and waits for explicit selection, even if a theme was already specified; descriptive text repeats theme features.

**Keep / condense / move / delete:** Keep theme assets and conditional lookups; reuse a supplied choice and ask only when a missing preference materially affects the result. Condense the duplicate catalog.

**Trigger boundary:** Explicit theme selection/application requests; exclude incidental styling when an existing theme governs.

**Evidence:**

- [skills-market/documents/design/theme-factory/SKILL.md:28](../../skills-market/documents/design/theme-factory/SKILL.md#L28) — `Wait for selection`: A redundant approval gate when the user already selected a theme.

<a id="skill-web-artifacts-builder"></a>

### 34. web-artifacts-builder — P1

Source: [skills-market/documents/design/web-artifacts-builder/SKILL.md](../../skills-market/documents/design/web-artifacts-builder/SKILL.md) · version `1.0.0`.

**Retain:** Bundle a working multi-component interactive artifact with the chosen frontend stack.

**Findings:** Discourages testing before delivery, hardcodes a large dependency stack, and references a missing Common Development Tasks section. Helper scripts install dependencies and rewrite configuration.

**Keep / condense / move / delete:** Keep single-file bundling contracts; verify essential startup/interactions before calling the artifact finished. Inspect helper mutations, respect an existing project, and move stack detail to conditional references rather than installing unused components.

**Trigger boundary:** Current complex-artifact versus simple-HTML boundary is useful; retain it.

**Evidence:**

- [skills-market/documents/design/web-artifacts-builder/SKILL.md:73](../../skills-market/documents/design/web-artifacts-builder/SKILL.md#L73) — `avoid testing the artifact upfront`: Latency advice can suppress necessary correctness checks.
- [skills-market/documents/design/web-artifacts-builder/SKILL.md:46](../../skills-market/documents/design/web-artifacts-builder/SKILL.md#L46) — `Common Development Tasks`: Named section is absent from this skill.

<a id="skill-webapp-testing"></a>

### 35. webapp-testing — P1

Source: [skills-market/documents/design/webapp-testing/SKILL.md](../../skills-market/documents/design/webapp-testing/SKILL.md) · version `1.0.0`.

**Retain:** Observe rendered state, choose real selectors, and run the requested browser checks with controlled server lifecycle.

**Findings:** Makes networkidle mandatory for all dynamic pages, forbids source inspection before running helpers, and requires Python/headless Chromium regardless of available tooling. The server helper pipes output without draining and terminates shell processes without explicit child-process cleanup.

**Keep / condense / move / delete:** Keep observable readiness and actual selector discovery; use app-specific assertions instead of universal network silence. Permit read-only helper inspection, prefer available supported browser tools, and repair process lifecycle behavior before relying on it for noisy/long-running servers.

**Trigger boundary:** Keep local web testing scope; distinguish external account browsing.

**Evidence:**

- [skills-market/documents/design/webapp-testing/SKILL.md:17](../../skills-market/documents/design/webapp-testing/SKILL.md#L17) — `DO NOT read the source`: Blocks safe inspection needed for troubleshooting or understanding side effects.
- [skills-market/documents/design/webapp-testing/SKILL.md:63](../../skills-market/documents/design/webapp-testing/SKILL.md#L63) — `CRITICAL: Wait for JS to execute`: networkidle is not a universal proof of application readiness.
- [skills-market/documents/design/webapp-testing/scripts/with_server.py:72](../../skills-market/documents/design/webapp-testing/scripts/with_server.py#L72) — `stdout=subprocess.PIPE`: No drain is present while waiting/running, so verbose server output can fill the pipe.
- [skills-market/documents/design/webapp-testing/scripts/with_server.py:96](../../skills-market/documents/design/webapp-testing/scripts/with_server.py#L96) — `process.terminate()`: Only the shell process is explicitly terminated; child cleanup is not established.

<a id="skill-doc-coauthoring"></a>

### 36. doc-coauthoring — P1

Source: [skills-market/documents/collaboration/doc-coauthoring/SKILL.md](../../skills-market/documents/collaboration/doc-coauthoring/SKILL.md) · version `1.0.0`.

**Retain:** Clarify audience and evidence, draft a coherent document, and use targeted reader feedback when helpful.

**Findings:** Requires repeated 5–10-question rounds, 5–20 options per section, multiple transition approvals and fresh-reader loops; asks users not to edit directly and requests confirmation for ordinary connected-source searches.

**Keep / condense / move / delete:** Keep audience/context and targeted revision. Make facilitated workshops and reader testing opt-in; remove quotas and redundant transitions, allow direct edits, and stop when the requested document is coherent and supported.

**Trigger boundary:** Narrow to users seeking a guided coauthoring process; exclude ordinary one-pass drafting or small corrections.

**Acceptance force:** Material missing context is action-required. Fixed interview counts, reader-agent approval and stage-by-stage consent are optional workflow choices.

**Evidence:**

- [skills-market/documents/collaboration/doc-coauthoring/SKILL.md:95](../../skills-market/documents/collaboration/doc-coauthoring/SKILL.md#L95) — `Generate 5-10 numbered questions`: Question quota can manufacture interaction costs.
- [skills-market/documents/collaboration/doc-coauthoring/SKILL.md:206](../../skills-market/documents/collaboration/doc-coauthoring/SKILL.md#L206) — `Instead of editing the doc directly`: Restricts the author's own workflow unnecessarily.

<a id="skill-internal-comms"></a>

### 37. internal-comms — P2

Source: [skills-market/documents/collaboration/internal-comms/SKILL.md](../../skills-market/documents/collaboration/internal-comms/SKILL.md) · version `1.0.0`.

**Retain:** Choose the requested communication format and preserve factual context and audience.

**Findings:** Company identity and formats are unspecified; activation covers essentially every internal update and duplicates body trigger lists.

**Keep / condense / move / delete:** Keep conditional example routing, label templates as examples rather than company policy, and ask for a format only if it cannot be inferred. Drafting never implies sending.

**Trigger boundary:** Specific internal-communication drafting intent; exclude external publication and simple status questions.

**Evidence:**

- [skills-market/documents/collaboration/internal-comms/SKILL.md:4](../../skills-market/documents/collaboration/internal-comms/SKILL.md#L4) — `formats that my company likes to use`: Undefined organization-specific preferences are presented as universal context.

<a id="skill-scientific-figure-polish"></a>

### 38. scientific-figure-polish — P2

Source: [skills-market/documents/design/scientific-figure-polish/SKILL.md](../../skills-market/documents/design/scientific-figure-polish/SKILL.md) · version `1.0.0`.

**Retain:** Preserve scientific values and registration while matching comparable plot frames and readable compact typography.

**Findings:** Strong task-specific constraints are valuable. The Figure 6 anecdote and repeated compactness justifications can be condensed; universal snapshot/hash checks should scale with overwrite/concurrency risk.

**Keep / condense / move / delete:** Keep aspect-ratio, layer-registration, label-identity, frame-measurement and parser/render checks. Delete incident narration; retain defaults explicitly as this user's style, and make hash checks conditional on reused/concurrently edited sources.

**Trigger boundary:** Good concrete figure-polish boundary and explicit scientific-recomputation exclusion; preserve it.

**Evidence:**

- [skills-market/documents/design/scientific-figure-polish/SKILL.md:19](../../skills-market/documents/design/scientific-figure-polish/SKILL.md#L19) — `The spacious first revision of Figure 6 failed`: Historical narrative can be replaced by the resulting geometric decision rule.

<a id="skill-imgur-cli"></a>

### 39. imgur-cli — P3

Source: [skills-market/documents/media/imgur-cli/SKILL.md](../../skills-market/documents/media/imgur-cli/SKILL.md) · version `1.0.0`.

**Retain:** Upload only the requested image and preserve the returned deletion handle; delete by the correct handle.

**Findings:** Already concise and specifically routed. Fixed installation path and source-derived API/client assumptions are environment/version-dependent.

**Keep / condense / move / delete:** Keep upload/delete contracts and conditional source reference; discover the binary and verify help when troubleshooting. Preserve the deletion handle with appropriate privacy.

**Trigger boundary:** Retain explicit Imgur upload/deletion/setup requests; no general image-task activation.

**Evidence:**

- [skills-market/documents/media/imgur-cli/SKILL.md:4](../../skills-market/documents/media/imgur-cli/SKILL.md#L4) — `deletehash`: Deletion-handle contract is a useful non-obvious retained constraint.

<a id="skill-slack-gif-creator"></a>

### 40. slack-gif-creator — P2

Source: [skills-market/documents/media/slack-gif-creator/SKILL.md](../../skills-market/documents/media/slack-gif-creator/SKILL.md) · version `1.0.0`.

**Retain:** Produce a valid, readable animated GIF within the requested Slack use-case limits.

**Findings:** Animation/PIL tutorials dominate. Heading calls suggested dimensions/parameters Slack requirements, while user context may vary. Basic drawing-style bans are subjective.

**Keep / condense / move / delete:** Keep builder/validator/easing contracts, inspect their actual size limits, and distinguish platform hard limits from recommendations. Condense generic drawing/animation recipes; preserve all helper modules pending caller inspection.

**Trigger boundary:** Keep explicit Slack GIF intent; distinguish ChatGPT animated pets and static images.

**Evidence:**

- [skills-market/documents/media/slack-gif-creator/SKILL.md:14](../../skills-market/documents/media/slack-gif-creator/SKILL.md#L14) — `## Slack Requirements`: Recommendations and verified platform constraints should be separated.
- [skills-market/documents/media/slack-gif-creator/SKILL.md:91](../../skills-market/documents/media/slack-gif-creator/SKILL.md#L91) — ``Always set `width=2```: Aesthetic preference is not a universal correctness condition.

<a id="skill-academic-writing-editor"></a>

### 41. academic-writing-editor — P1

Source: [skills-market/writing/academic/academic-writing-editor/SKILL.md](../../skills-market/writing/academic/academic-writing-editor/SKILL.md) · version `1.0.0`.

**Retain:** Improve argument clarity and paragraph coherence without strengthening unsupported scientific claims.

**Findings:** Forces every paragraph into context-content-conclusion and bans bullets despite requesting a bulleted critique. The figure example upgrades a neutral cross-reference into an ungrounded accuracy claim; evidence-preservation is missing.

**Keep / condense / move / delete:** Keep audience/argument editing; make narrative frameworks optional, explicitly preserve uncertainty and evidence, and separate manuscript prose from review-output formatting.

**Trigger boundary:** Specify editing supplied bioinformatics manuscript text, not general academic writing.

**Evidence:**

- [skills-market/writing/academic/academic-writing-editor/SKILL.md:18](../../skills-market/writing/academic/academic-writing-editor/SKILL.md#L18) — `Every single paragraph must begin`: A useful narrative pattern becomes a rigid requirement.
- [skills-market/writing/academic/academic-writing-editor/SKILL.md:38](../../skills-market/writing/academic/academic-writing-editor/SKILL.md#L38) — `accurately predicted the perturbation responses`: Illustrative rewrite adds a scientific claim absent from the original.

<a id="skill-draft-spatial-methods"></a>

### 42. draft-spatial-methods — P1

Source: [skills-market/compbio/expert-workflows/draft-spatial-methods/SKILL.md](../../skills-market/compbio/expert-workflows/draft-spatial-methods/SKILL.md) · version `1.0.0`.

**Retain:** Describe actual scripts, preprocessing, tensor contracts and solver settings reproducibly.

**Findings:** Requires tissue/annotation details from a specific muscle-aging workflow for every Methods request, and does not explicitly distinguish missing evidence from inferred defaults.

**Keep / condense / move / delete:** Keep reproducibility fields only when relevant and source-supported. Delete compulsory project-specific examples; request or mark missing thresholds rather than inventing them; allow algorithm-only Methods sections.

**Trigger boundary:** Retain spatial/single-cell Methods intent, exclude Results and generic architecture explanation.

**Evidence:**

- [skills-market/compbio/expert-workflows/draft-spatial-methods/SKILL.md:14](../../skills-market/compbio/expert-workflows/draft-spatial-methods/SKILL.md#L14) — `Strictly enforce the following structural requirements`: Section scope can be narrower than a full tissue-to-model pipeline.

<a id="skill-critique-bio-manuscript"></a>

### 43. critique-bio-manuscript — P2

Source: [skills-market/compbio/expert-workflows/critique-bio-manuscript/SKILL.md](../../skills-market/compbio/expert-workflows/critique-bio-manuscript/SKILL.md) · version `1.0.0`.

**Retain:** Identify evidence-backed leakage, comparator and validation limitations in a supplied manuscript.

**Findings:** Treats teardown and biological ground truth as universal framing; current-SOTA claims require sources unavailable under a Read-only tool declaration.

**Keep / condense / move / delete:** Keep train/test dependency checks, distinguish absent reporting from demonstrated flaws, and make validation/comparator requests proportionate to the paper's claims. Permit verified literature lookup when the review actually needs current comparisons.

**Trigger boundary:** Preserve explicit-review invocation policy; do not activate during drafting.

**Evidence:**

- [skills-market/compbio/expert-workflows/critique-bio-manuscript/SKILL.md:13](../../skills-market/compbio/expert-workflows/critique-bio-manuscript/SKILL.md#L13) — `tearing it down constructively`: Adversarial framing can manufacture flaws rather than assess evidence.
- [skills-market/compbio/expert-workflows/critique-bio-manuscript/SKILL.md:16](../../skills-market/compbio/expert-workflows/critique-bio-manuscript/SKILL.md#L16) — `current state-of-the-art benchmarks`: Current comparator recommendations need external verification.

<a id="skill-explain-bio-dl-model"></a>

### 44. explain-bio-dl-model — P1

Source: [skills-market/compbio/expert-workflows/explain-bio-dl-model/SKILL.md](../../skills-market/compbio/expert-workflows/explain-bio-dl-model/SKILL.md) · version `1.0.0`.

**Retain:** Explain supplied architecture and biological motivation while preserving what experiments actually establish.

**Findings:** Example claims discretization isolates biological states from technical noise without evidence. Requires rationale and biological validation even when neither is supplied.

**Keep / condense / move / delete:** Keep data-flow and architecture explanation; label motivation as design rationale, avoid claiming identifiability/denoising from architecture alone, and report missing validation rather than invent it.

**Trigger boundary:** Keep manuscript explanation intent; distinguish theorem proof and model implementation.

**Evidence:**

- [skills-market/compbio/expert-workflows/explain-bio-dl-model/SKILL.md:16](../../skills-market/compbio/expert-workflows/explain-bio-dl-model/SKILL.md#L16) — `effectively isolating distinct cellular states from continuous technical noise`: Architecture alone does not establish this scientific effect.

<a id="skill-humanizer"></a>

### 45. humanizer — P2

Source: [skills-market/writing/academic/humanizer/SKILL.md](../../skills-market/writing/academic/humanizer/SKILL.md) · version `3.0.0`.

**Retain:** Remove formulaic prose while preserving facts, justified caution, and genre-specific voice.

**Findings:** Repeats academic-mode constraints and always chains the academic editor even for a tiny style pass, inheriting that skill's rigid framework. Trigger exclusions are otherwise strong.

**Keep / condense / move / delete:** Keep meaning/register safeguards and selective references; make structure editing conditional and remove repeated mode instructions. Do not infer AI authorship from stylistic signals.

**Trigger boundary:** Keep cleanup-specific intent and general-writing exclusion.

**Evidence:**

- [skills-market/writing/academic/humanizer/SKILL.md:62](../../skills-market/writing/academic/humanizer/SKILL.md#L62) — ``use `academic-writing-editor` first``: A full structural edit is not required for every small academic cleanup.

<a id="skill-humanizer-zh"></a>

### 46. humanizer-zh — P1

Source: [skills-market/writing/academic/humanizer-zh/SKILL.md](../../skills-market/writing/academic/humanizer-zh/SKILL.md) · version `1.0.0`.

**Retain:** Improve Chinese prose naturally while preserving factual content, caution and the author's register.

**Findings:** Example invents batch processing, shortcuts, offline mode and user feedback to replace generic hype. Rules forbid lists of three and quotes mechanically, and encourage personality in scientific contexts. Many examples are literal English-pattern translations or no-op comparisons.

**Keep / condense / move / delete:** Add explicit no-new-facts/academic-register safeguards. Delete invented example facts, mechanical numeric/style rules and no-op examples; condense to Chinese-specific decisions with optional examples.

**Trigger boundary:** Narrow to requested Chinese style cleanup rather than every translation/rewrite.

**Evidence:**

- [skills-market/writing/academic/humanizer-zh/SKILL.md:479](../../skills-market/writing/academic/humanizer-zh/SKILL.md#L479) — `添加了具体功能和具体反馈`: The example obtains specificity by inventing factual content.
- [skills-market/writing/academic/humanizer-zh/SKILL.md:418](../../skills-market/writing/academic/humanizer-zh/SKILL.md#L418) — `三段式列举？`: Legitimate three-item content should not be distorted to avoid a pattern.

<a id="skill-asd-ste100"></a>

### 47. asd-ste100 — P2

Source: [skills-market/writing/technical/asd-ste100/SKILL.md](../../skills-market/writing/technical/asd-ste100/SKILL.md) · version `0.4.0`.

**Retain:** Remove ambiguity without dropping conditions, modality, or necessary precision; do not claim certified dictionary compliance.

**Findings:** Useful constraints are repeated across modes, process, output and boundaries; the routing also attracts generally dense prose beyond high-cost ambiguity. Long licensing/standard-history discussion is secondary to execution.

**Keep / condense / move / delete:** Keep modality/no-new-facts and strict-versus-advisory distinction; condense repetitions and move detailed standard provenance to the existing reference. Preserve linter and examples; do not assert linter success equals semantic correctness or certification.

**Trigger boundary:** Prioritize explicit controlled-language work or material ambiguity; exclude routine prose editing with no parsing risk.

**Evidence:**

- [skills-market/writing/technical/asd-ste100/SKILL.md:95](../../skills-market/writing/technical/asd-ste100/SKILL.md#L95) — `Never add a fact the source did not state`: Important invariant to retain.
- [skills-market/writing/technical/asd-ste100/SKILL.md:33](../../skills-market/writing/technical/asd-ste100/SKILL.md#L33) — `## Source and Scope`: Detailed provenance can be selectively loaded rather than repeated in the entrypoint.

<a id="skill-compile-latex"></a>

### 48. compile-latex — P1

Source: [skills-market/writing/latex/compile-latex/SKILL.md](../../skills-market/writing/latex/compile-latex/SKILL.md) · version `1.0.0`.

**Retain:** Compile with the project's actual engine/bibliography configuration and verify the requested PDF and reference resolution.

**Findings:** Mandates output folders, PDF copies, bibliography filenames, unrelated cloud templates and VS Code global settings. References absent literature and latex-autofix skills. Perl END copies any existing PDF even after failure; the Overleaf claim needs an exact filename distinction: official documentation specifies latexmkrc without a leading dot, while this skill says .latexmkrc is ignored. The dotted-file behavior was not verified and is not counted as a confirmed defect.

**Keep / condense / move / delete:** Delete user-specific template/global-settings policy and bibliography naming mandate. Keep dependency-aware engine/package handling and logs; copy only the current successful artifact. Discover actual project configuration and resolve missing workflow references.

**Trigger boundary:** Compilation intent only; do not author a new project/template merely to compile an existing one.

**Evidence:**

- [skills-market/writing/latex/compile-latex/SKILL.md:86](../../skills-market/writing/latex/compile-latex/SKILL.md#L86) — ``Always name the bibliography file `paperpile.bib```: Local convention overreaches general compilation.
- [skills-market/writing/latex/compile-latex/SKILL.md:128](../../skills-market/writing/latex/compile-latex/SKILL.md#L128) — `END { system`: Exit-time copying can publish stale artifacts after a failed build.
- [skills-market/writing/latex/compile-latex/SKILL.md:23](../../skills-market/writing/latex/compile-latex/SKILL.md#L23) — `Overleaf ignores this file too`: Unresolved dotted-filename behavior; provider documents the non-dotted filename.

Primary documentation checked: [Overleaf latexmkrc filename](https://docs.overleaf.com/managing-projects-and-files/the-latexmkrc-file).

<a id="skill-latex-writing"></a>

### 49. latex-writing — P1

Source: [skills-market/writing/latex/latex-writing/SKILL.md](../../skills-market/writing/latex/latex-writing/SKILL.md) · version `1.0.0`.

**Retain:** Use semantic markup and preserve mathematical meaning and class-compatible typography.

**Findings:** Mandatory preamble points to a file that is not bundled. Universal cleveref/csquotes/style mandates can conflict with journal classes; activation extends to any academic writing. Basic LaTeX examples dominate.

**Keep / condense / move / delete:** Repair/remove missing preamble contract first. Keep semantic math/noweb pitfalls, condense generic tutorial examples, and respect existing class/package conventions and requested prose style.

**Trigger boundary:** LaTeX/noweb editing intent, excluding generic manuscript prose or casual BibTeX mentions.

**Evidence:**

- [skills-market/writing/latex/latex-writing/SKILL.md:282](../../skills-market/writing/latex/latex-writing/SKILL.md#L282) — `references/preamble.tex`: Required referenced asset is absent.
- [skills-market/writing/latex/latex-writing/SKILL.md:282](../../skills-market/writing/latex/latex-writing/SKILL.md#L282) — `Copy it verbatim`: Mandatory template replacement overrides existing project constraints.

<a id="skill-duke-nus-marp"></a>

### 50. duke-nus-marp — P3

Source: [skills-market/writing/presentations/duke-nus-marp/SKILL.md](../../skills-market/writing/presentations/duke-nus-marp/SKILL.md) · version `1.0.0`.

**Retain:** Create source-grounded Duke-NUS Marp decks while preserving slide geometry, citations, and editable Markdown.

**Findings:** Narrow well-specified workflow with useful citation/rendering pitfalls. Historical original-folder path is not needed for execution. HTML/PDF exports are defaults, not universal output requirements.

**Keep / condense / move / delete:** Retain bundled theme contracts and no-invented-citations boundary. Remove unnecessary original-path provenance from the entrypoint; keep output defaults overridden by user scope and verify version-dependent CLI flags when used.

**Trigger boundary:** Keep saved-theme Marp intent and PowerPoint/library-write exclusions.

**Evidence:**

- [skills-market/writing/presentations/duke-nus-marp/SKILL.md:19](../../skills-market/writing/presentations/duke-nus-marp/SKILL.md#L19) — `the original folder is not required`: Absolute source provenance can be condensed without weakening behavior.

<a id="skill-obsidian-bases"></a>

### 51. obsidian-bases — P2

Source: [skills-market/writing/obsidian/obsidian-bases/SKILL.md](../../skills-market/writing/obsidian/obsidian-bases/SKILL.md) · version `1.0.0`.

**Retain:** Preserve valid Base YAML, defined properties/formulas, duration semantics, and intended note filtering.

**Findings:** Large schema/cookbook and duplicate formula troubleshooting; global syntax validation alone does not prove view compatibility. Hosted-image intent is routed directly to a specific upload service.

**Keep / condense / move / delete:** Keep duration/null/YAML pitfalls and one minimal example; move genuinely conditional view recipes to references. Verify installed-version/plugin-specific view types and ask no additional approval if an image service is already specified, but do not infer Imgur from generic hosting intent.

**Trigger boundary:** Explicit Obsidian Base/view work; exclude generic YAML or spreadsheet formulas.

**Evidence:**

- [skills-market/writing/obsidian/obsidian-bases/SKILL.md:200](../../skills-market/writing/obsidian/obsidian-bases/SKILL.md#L200) — `Duration does NOT support`: Useful fragile type contract to retain.
- [skills-market/writing/obsidian/obsidian-bases/SKILL.md:20](../../skills-market/writing/obsidian/obsidian-bases/SKILL.md#L20) — ``use `imgur-cli` to upload``: Generic hosting intent does not choose a service automatically.

<a id="skill-json-canvas"></a>

### 52. json-canvas — P2

Source: [skills-market/writing/obsidian/json-canvas/SKILL.md](../../skills-market/writing/obsidian/json-canvas/SKILL.md) · version `1.0.0`.

**Retain:** Preserve graph identities, valid node/edge references, geometry, and JSON string escaping.

**Findings:** Repeats validation for each workflow and presents sixteen-hex IDs as a schema requirement; one file-node example has seventeen characters. Imgur routing adds a service choice to general online-image intent.

**Keep / condense / move / delete:** Keep graph integrity and newline pitfalls, condense duplicate workflow checks, distinguish preferred generated IDs from specification requirements, and fix internal example inconsistency.

**Trigger boundary:** Require JSON Canvas/Obsidian artifact intent, excluding generic flowchart requests in other formats.

**Evidence:**

- [skills-market/writing/obsidian/json-canvas/SKILL.md:109](../../skills-market/writing/obsidian/json-canvas/SKILL.md#L109) — `a1b2c3d4e5f67890`: Seventeen-character example conflicts with its own sixteen-character rule.
- [skills-market/writing/obsidian/json-canvas/SKILL.md:72](../../skills-market/writing/obsidian/json-canvas/SKILL.md#L72) — `Unique 16-char hex identifier`: Must distinguish local generation convention from the actual specification.

Primary documentation checked: [JSON Canvas 1.0 specification](https://jsoncanvas.org/spec/1.0/).

<a id="skill-obsidian-markdown"></a>

### 53. obsidian-markdown — P2

Source: [skills-market/writing/obsidian/obsidian-markdown/SKILL.md](../../skills-market/writing/obsidian/obsidian-markdown/SKILL.md) · version `1.0.0`.

**Retain:** Preserve valid Obsidian-specific links, block IDs, embeds and note properties.

**Findings:** Body correctly avoids teaching standard Markdown, but rigid wikilink-only policy can conflict with a vault's existing links; create-note workflow always adds frontmatter/callouts and chooses Imgur for generic hosting intent.

**Keep / condense / move / delete:** Keep syntax-specific pitfalls and selective references. Honor vault link/property conventions and add optional structures only when useful; do not equate hosted images with an authorized Imgur upload.

**Trigger boundary:** Obsidian-specific syntax work; exclude generic frontmatter/tags outside a vault.

**Evidence:**

- [skills-market/writing/obsidian/obsidian-markdown/SKILL.md:22](../../skills-market/writing/obsidian/obsidian-markdown/SKILL.md#L22) — `external URLs only`: Link-style recommendation must respect the vault's established contract.

<a id="skill-obsidian-cli"></a>

### 54. obsidian-cli — P2

Source: [skills-market/writing/obsidian/obsidian-cli/SKILL.md](../../skills-market/writing/obsidian/obsidian-cli/SKILL.md) · version `1.0.0`.

**Retain:** Target the correct vault and file explicitly, discover actual CLI support, and inspect results.

**Findings:** Help-first guidance is good. Generic create example includes overwrite and defaults can target the active file/focused vault; hosted-image routing assumes a service.

**Keep / condense / move / delete:** Keep vault/path distinctions and observable development checks; default mutation examples to exact paths without overwrite, and use overwrite only for the intended existing target. Preserve available-tool discovery.

**Trigger boundary:** Keep explicit CLI/vault operation intent; distinguish content syntax and knowledge-base restructuring.

**Evidence:**

- [skills-market/writing/obsidian/obsidian-cli/SKILL.md:30](../../skills-market/writing/obsidian/obsidian-cli/SKILL.md#L30) — `silent overwrite`: A destructive flag appears in a generic creation example.
- [skills-market/writing/obsidian/obsidian-cli/SKILL.md:37](../../skills-market/writing/obsidian/obsidian-cli/SKILL.md#L37) — `the active file is used`: Target defaults are a concrete mutation risk worth preserving explicitly.

<a id="skill-defuddle"></a>

### 55. defuddle — P2

Source: [skills-market/writing/obsidian/defuddle/SKILL.md](../../skills-market/writing/obsidian/defuddle/SKILL.md) · version `1.0.0`.

**Retain:** Extract readable page content when HTML clutter materially obstructs the requested reading.

**Findings:** Claims all ordinary web URLs should use this CLI and installs it globally if missing, regardless of connected browser tools or institutional access.

**Keep / condense / move / delete:** Keep concise extraction commands; activate only when this extractor is requested/useful, prefer existing access-capable tools, and avoid global installation as an automatic prerequisite.

**Trigger boundary:** Exclude all-URL catchall, authenticated PDFs, and already available clean content.

**Evidence:**

- [skills-market/writing/obsidian/defuddle/SKILL.md:4](../../skills-market/writing/obsidian/defuddle/SKILL.md#L4) — `Use instead of WebFetch when the user provides a URL`: Tool-specific helper claims every web-reading task.

<a id="skill-wiki-keeper"></a>

### 56. wiki-keeper — P1

Source: [skills-market/writing/obsidian/wiki-keeper/SKILL.md](../../skills-market/writing/obsidian/wiki-keeper/SKILL.md) · version `1.0.0`.

**Retain:** Maintain canonical vault pages, local schemas and links coherently within authorized edits.

**Findings:** Query mode mandates saving reusable answers; default graph editing updates logs/index/inbox broadly, and output template is large even for a read-only query.

**Keep / condense / move / delete:** Keep local-schema/source discipline and graph-integrity checks. Separate read-only query/lint from authorized ingest; save only when requested or required by the actual vault contract, and update only affected navigation.

**Trigger boundary:** Keep vault maintenance/ingest scope; let simple note queries stay read-only.

**Evidence:**

- [skills-market/writing/obsidian/wiki-keeper/SKILL.md:121](../../skills-market/writing/obsidian/wiki-keeper/SKILL.md#L121) — `File reusable syntheses back into the wiki`: Reading a vault is not itself authorization to write.
- [skills-market/writing/obsidian/wiki-keeper/SKILL.md:149](../../skills-market/writing/obsidian/wiki-keeper/SKILL.md#L149) — `Do not let chat-only syntheses remain unfiled`: Local preference becomes a global mutation obligation.

<a id="skill-zotpilot"></a>

### 57. zotpilot — P1

Source: [skills-market/writing/literature/zotpilot/SKILL.md](../../skills-market/writing/literature/zotpilot/SKILL.md) · version `1.0.0`.

**Retain:** Use the appropriate existing library interface, ground citations, and distinguish exact metadata from semantic evidence and write operations.

**Findings:** Routes nearly any paper/citation task into installation, provider setup and whole-library indexing. status auto-installs, setup registers multiple clients, and cloud embeddings can transmit paper content. Current connected Zotero tools differ from the bundled legacy names.

**Keep / condense / move / delete:** Keep numeric item/library identity, citation grounding and partial-failure reporting. Discover connected tools first; make installation/indexing a separate requested setup workflow and account for provider data transfer. Condense tool catalogs and incident-specific intake/duplicate workflows into references.

**Trigger boundary:** Zotero/library or explicit ZotPilot work; exclude formatting supplied references and ordinary scientific prose.

**Acceptance force:** Existing-connector capabilities and intended write target are action/risk checks. Installation, API credentials and indexing are only gates for operations that actually need them.

**Evidence:**

- [skills-market/writing/literature/zotpilot/SKILL.md:33](../../skills-market/writing/literature/zotpilot/SKILL.md#L33) — `This auto-installs the ZotPilot CLI`: A purported readiness read mutates the environment.
- [skills-market/writing/literature/zotpilot/SKILL.md:38](../../skills-market/writing/literature/zotpilot/SKILL.md#L38) — ``doc_count` is 0``: Index absence need not block metadata lookup through another connected tool.
- [skills-market/writing/literature/zotpilot/SKILL.md:4](../../skills-market/writing/literature/zotpilot/SKILL.md#L4) — `Use when user mentions Zotero, academic papers, citations`: Product-neutral scholarly tasks are overcaptured.

<a id="skill-github-auth"></a>

### 58. github-auth — P1

Source: [skills-market/platforms/github/github-auth/SKILL.md](../../skills-market/platforms/github/github-auth/SKILL.md) · version `1.1.0`.

**Retain:** Establish only the needed GitHub authentication without exposing or replacing existing credentials.

**Findings:** Defaults to plaintext credential store, token-embedded remotes, unencrypted new SSH keys, global identity/URL rewrites and direct token extraction. Calls read-only ls-remote a push-access test. Ordinary GitHub work need not require new authentication when a connector already works.

**Keep / condense / move / delete:** Remove token-printing/remote-embedding examples and broad credential defaults. Discover connected access and existing OS helpers first; scope identity/auth configuration to the requested target. Keep public-key-only output and truthful read/write capability checks.

**Trigger boundary:** Only requested authentication setup/repair, not every GitHub task.

**Evidence:**

- [skills-market/platforms/github/github-auth/SKILL.md:68](../../skills-market/platforms/github/github-auth/SKILL.md#L68) — `credential.helper store`: Plaintext global storage is the default example.
- [skills-market/platforms/github/github-auth/SKILL.md:89](../../skills-market/platforms/github/github-auth/SKILL.md#L89) — `username>:<token>@github.com`: Secrets would persist in remote configuration and command history.
- [skills-market/platforms/github/github-auth/SKILL.md:103](../../skills-market/platforms/github/github-auth/SKILL.md#L103) — `Test push access`: ls-remote establishes read access, not push permission.

<a id="skill-github-codebase-inspection"></a>

### 59. github-codebase-inspection — P1

Source: [skills-market/platforms/github/codebase-inspection/SKILL.md](../../skills-market/platforms/github/codebase-inspection/SKILL.md) · version `1.0.0`.

**Retain:** Measure a clearly scoped codebase while excluding generated/dependency files and explaining counting conventions.

**Findings:** Automatically uses pip --break-system-packages and suppresses errors to install a metric tool; name differs from stable registry ID. Repeated CLI catalogs outweigh the few useful exclusion rules.

**Keep / condense / move / delete:** Keep exclusion/count semantics, discover tools and use an isolated environment only if needed. Remove system-package override and duplicate tutorials; preserve or explicitly map the current installation identity.

**Trigger boundary:** Keep explicit LOC/composition intent; do not load merely because a repository is inspected.

**Evidence:**

- [skills-market/platforms/github/codebase-inspection/SKILL.md:31](../../skills-market/platforms/github/codebase-inspection/SKILL.md#L31) — `--break-system-packages`: A read-only measurement should not require altering system-managed packages.

<a id="skill-github-issues"></a>

### 60. github-issues — P1

Source: [skills-market/platforms/github/github-issues/SKILL.md](../../skills-market/platforms/github/github-issues/SKILL.md) · version `1.1.0`.

**Retain:** Read or mutate the exact intended issue set and report actual outcomes.

**Findings:** Repeats ad-hoc credential scraping; list/search/bulk examples lack robust pagination and HTTP failure checks. Bulk fallback does not exclude pull_request items and can close matching PRs through the shared issues endpoint.

**Keep / condense / move / delete:** Use available connector/credential helpers first, preserve issue-versus-PR filtering in every path, add pagination/error handling where completeness matters, and treat bulk closing/commenting as separately scoped writes.

**Trigger boundary:** Keep concrete issue operations; distinguish read-only triage recommendations from applying them.

**Evidence:**

- [skills-market/platforms/github/github-issues/SKILL.md:69](../../skills-market/platforms/github/github-issues/SKILL.md#L69) — `if 'pull_request' not in i`: Correct filter exists in read examples but is omitted by the bulk-closing fallback.
- [skills-market/platforms/github/github-issues/SKILL.md:350](../../skills-market/platforms/github/github-issues/SKILL.md#L350) — `while read num; do`: Bulk mutations run on an unverified mixed issues/PR result set.

<a id="skill-github-code-review"></a>

### 61. github-code-review — P1

Source: [skills-market/platforms/github/github-code-review/SKILL.md](../../skills-market/platforms/github/github-code-review/SKILL.md) · version `1.1.0`.

**Retain:** Review the actual diff/base and report grounded findings while preserving the working checkout.

**Findings:** Generic PR review automatically posts a formal review plus duplicate summary, checks out/deletes branches in the current workspace, assumes main, and requires GitHub auth even for local diffs. Uses missing absolute Hermes auth helper paths.

**Keep / condense / move / delete:** Keep diff context and valid inline-comment target semantics. Make local review read-only by default; publish only when requested, use the real PR base and isolated checkout if needed, and never delete an existing branch as cleanup.

**Trigger boundary:** Keep review intent; explicitly distinguish report-only from authorized GitHub review submission.

**Evidence:**

- [skills-market/platforms/github/github-code-review/SKILL.md:405](../../skills-market/platforms/github/github-code-review/SKILL.md#L405) — `Step 7: Post the review to GitHub`: Review request is promoted into external communication.
- [skills-market/platforms/github/github-code-review/SKILL.md:474](../../skills-market/platforms/github/github-code-review/SKILL.md#L474) — `git branch -D pr-$PR_NUMBER`: Unconditional forced deletion can remove pre-existing work.

<a id="skill-github-pr-workflow"></a>

### 62. github-pr-workflow — P1

Source: [skills-market/platforms/github/github-pr-workflow/SKILL.md](../../skills-market/platforms/github/github-pr-workflow/SKILL.md) · version `1.1.0`.

**Retain:** Complete the authorized subset of branch/PR/CI/merge work with scoped commits and verified target revisions.

**Findings:** Auto-fix recipe uses git add .; merge examples do not bind to reviewed head SHA. Duplicated curl/auth catalogs, branch-main assumptions and fixed retry counts obscure scope and stopping rules.

**Keep / condense / move / delete:** Keep scoped file staging and status/check-run distinctions. Remove all-file staging and credential scraping; identify actual base/head, honor required checks and bind merge to the intended head where supported. Stop CI retries when evidence indicates an external blocker.

**Trigger boundary:** Match the requested lifecycle operation; opening a PR does not imply merging.

**Evidence:**

- [skills-market/platforms/github/github-pr-workflow/SKILL.md:273](../../skills-market/platforms/github/github-pr-workflow/SKILL.md#L273) — `git add . && git commit`: Can commit unrelated user changes.
- [skills-market/platforms/github/github-pr-workflow/SKILL.md:275](../../skills-market/platforms/github/github-pr-workflow/SKILL.md#L275) — `Repeat if still failing (up to 3 attempts`: Retry count does not distinguish code defects from infrastructure failures.

<a id="skill-github-repo-management"></a>

### 63. github-repo-management — P1

Source: [skills-market/platforms/github/github-repo-management/SKILL.md](../../skills-market/platforms/github/github-repo-management/SKILL.md) · version `1.1.0`.

**Retain:** Manage the exact repository configuration/publication operation and preserve visibility, secrets and user work.

**Findings:** Examples default to public repositories/gists, broad staging and global auth fallbacks; mixes read-only repo info with branch protections, secrets, workflow dispatch and release creation. A broad manual loads all variants at once.

**Keep / condense / move / delete:** Keep precise target and secret-encryption contracts. Route among read/create/configure/release modes, make visibility explicit from user intent, use scoped files and supported access tools, and load API fallback references only when needed.

**Trigger boundary:** Keep explicit repository-management intent; do not turn generic repo inspection into setup or publication.

**Evidence:**

- [skills-market/platforms/github/github-repo-management/SKILL.md:91](../../skills-market/platforms/github/github-repo-management/SKILL.md#L91) — `gh repo create my-new-project --public`: Generic creation should not infer public visibility.
- [skills-market/platforms/github/github-repo-management/SKILL.md:308](../../skills-market/platforms/github/github-repo-management/SKILL.md#L308) — `gh secret set SSH_KEY < ~/.ssh/id_rsa`: A sensitive-key publication example needs explicit intended target and scope.

<a id="skill-page-keeper"></a>

### 64. page-keeper — P2

Source: [skills-market/frontend/site-maintenance/page-keeper/SKILL.md](../../skills-market/frontend/site-maintenance/page-keeper/SKILL.md) · version `1.0.0`.

**Retain:** Derive a reusable site-maintenance skill from actual repository contracts and material user preferences.

**Findings:** Eight mandatory deliverables and confirmation categories can duplicate work even when requirements are already known. Repo map, rulebook and final skill repeat the same rules.

**Keep / condense / move / delete:** Keep inspect-first, inferred-versus-user-only distinctions and exact-content boundaries. Condense repeated inventories, produce only requested deliverables, and ask only unresolved material questions.

**Trigger boundary:** Good distinction between generating a maintenance skill and maintaining a site; preserve it.

**Evidence:**

- [skills-market/frontend/site-maintenance/page-keeper/SKILL.md:17](../../skills-market/frontend/site-maintenance/page-keeper/SKILL.md#L17) — `Always work toward these outputs, in order`: Fixed multi-artifact pipeline is disproportionate to narrow updates.

<a id="skill-chen-academic-page-maintainer"></a>

### 65. chen-academic-page-maintainer — P1

Source: [skills-market/frontend/site-maintenance/chen-academic-page-maintainer/SKILL.md](../../skills-market/frontend/site-maintenance/chen-academic-page-maintainer/SKILL.md) · version `1.0.0`.

**Retain:** Preserve this site's factual identity/publication contracts and mirrored content while applying scoped edits.

**Findings:** Trigger says this website without an executable target identifier, despite installation into a general market. It loads five references for every change and asks approval for any uncovered case, then asks to record a new rule; old absolute notes paths are embedded.

**Keep / condense / move / delete:** Add a repository identity/path match before activation. Keep exact wording, source maps, real publication-state and protected-photo rules; read only relevant references. Remove uncovered-case/repeated-rule-update gates for routine authorized edits and discover external notes paths.

**Trigger boundary:** Match this specific al-folio repository; exclude unrelated websites and this skills catalog.

**Evidence:**

- [skills-market/frontend/site-maintenance/chen-academic-page-maintainer/SKILL.md:198](../../skills-market/frontend/site-maintenance/chen-academic-page-maintainer/SKILL.md#L198) — `Any issue not explicitly covered by this skill`: Turns ordinary implementation judgment into an unbounded approval gate.
- [skills-market/frontend/site-maintenance/chen-academic-page-maintainer/SKILL.md:20](../../skills-market/frontend/site-maintenance/chen-academic-page-maintainer/SKILL.md#L20) — `Read these references before editing`: Load-all policy ignores task-specific disclosure.

<a id="skill-latent-identifiability"></a>

### 66. latent-identifiability — P3

Source: [skills-market/ai-ml/theory/latent-identifiability/SKILL.md](../../skills-market/ai-ml/theory/latent-identifiability/SKILL.md) · version `1.0.0`.

**Retain:** Specify observable law and target equivalence, test admissible symmetries, and distinguish proof status from empirical learning success.

**Findings:** Strong domain-specific reasoning and precise exclusions. Assumption ledgers and a full theory-to-implementation table can be excessive for a single lemma audit; some router provenance is not operationally needed.

**Keep / condense / move / delete:** Keep symmetry/counterexample and causal-boundary rules; make dossier/implementation sections conditional on the requested scope and condense router provenance. Preserve proof references and counterexamples.

**Trigger boundary:** Retain explicit identifiability/proof intent and empirical-benchmark exclusion.

**Evidence:**

- [skills-market/ai-ml/theory/latent-identifiability/SKILL.md:66](../../skills-market/ai-ml/theory/latent-identifiability/SKILL.md#L66) — `Each arrow is a proof obligation`: Non-obvious scientific constraint worth retaining.

<a id="skill-jepa-pytorch-development"></a>

### 67. jepa-pytorch-development — P3

Source: [skills-market/ai-ml/deep-learning/jepa-pytorch-development/SKILL.md](../../skills-market/ai-ml/deep-learning/jepa-pytorch-development/SKILL.md) · version `1.0.0`.

**Retain:** Preserve masking/information boundaries, recipe-specific gradients, EMA timing, distributed statistics, and resumed-update meaning.

**Findings:** Already distinguishes reproduction, variant and smoke-test evidence and selects checks by change scope. Could further separate trainer-only verification from small architecture questions.

**Keep / condense / move / delete:** Retain the behavioral contracts and selective recipe references; keep the smoke test optional and version-pin source-based reproduction claims. No broad rewrite justified by length.

**Trigger boundary:** Keep specific JEPA implementation/debugging requests and actual selected-family distinctions.

**Evidence:**

- [skills-market/ai-ml/deep-learning/jepa-pytorch-development/SKILL.md:60](../../skills-market/ai-ml/deep-learning/jepa-pytorch-development/SKILL.md#L60) — `Select checks relevant to the change`: Proportionate validation is already explicit.

<a id="skill-browser-use"></a>

### 68. browser-use — P1

Source: [skills-market/ai-ml/llm/browser-use/SKILL.md](../../skills-market/ai-ml/llm/browser-use/SKILL.md) · version `1.1.0`.

**Retain:** Use an explicitly chosen browser-use agent with the configured provider and a supported browser environment.

**Findings:** Claims a Google API key is universally required but later lists alternatives; labels WebKit as Firefox support; hardcodes another user's checkout and an old browser-cache symlink repair.

**Keep / condense / move / delete:** Remove provider/browser contradictions and old global symlink fixes; discover installed package/provider/browser support and prefer existing connectors for service tasks. Keep only version-checked initialization examples.

**Trigger boundary:** Explicit browser-use setup or agent execution, not all web tasks.

**Evidence:**

- [skills-market/ai-ml/llm/browser-use/SKILL.md:16](../../skills-market/ai-ml/llm/browser-use/SKILL.md#L16) — `requires a Google API key`: Contradicts the skill's own supported provider alternatives.
- [skills-market/ai-ml/llm/browser-use/SKILL.md:27](../../skills-market/ai-ml/llm/browser-use/SKILL.md#L27) — `Firefox support`: WebKit is not Firefox/Gecko.

Primary documentation checked: [Browser Use quickstart](https://docs.browser-use.com/open-source/quickstart).

<a id="skill-pytorch"></a>

### 69. pytorch — P1

Source: [skills-market/ai-ml/deep-learning/pytorch/SKILL.md](../../skills-market/ai-ml/deep-learning/pytorch/SKILL.md) · version `1.0.0`.

**Retain:** Preserve tensor/device/dtype and gradient ownership, implement the requested training behavior, and verify relevant numerical behavior.

**Findings:** Quick tensor example moves x to CUDA but creates y on CPU before adding them. Blanket zero_grad/DataParallel/AMP advice ignores accumulation and version-specific APIs; generic tutorial and advertising add substantial cost.

**Keep / condense / move / delete:** Correct runnable device examples first. Keep training/eval and checkpoint contracts; condense basic syntax/layer catalogs, remove advertising, and route AMP/export/distributed choices through installed-version docs.

**Trigger boundary:** Narrow to PyTorch-specific implementation/debugging rather than generic deep-learning discussion.

**Evidence:**

- [skills-market/ai-ml/deep-learning/pytorch/SKILL.md:60](../../skills-market/ai-ml/deep-learning/pytorch/SKILL.md#L60) — `y = torch.randn(3, 4)`: The preceding x is moved to the chosen device, leaving this y on CPU.
- [skills-market/ai-ml/deep-learning/pytorch/SKILL.md:412](../../skills-market/ai-ml/deep-learning/pytorch/SKILL.md#L412) — ``Always call `optimizer.zero_grad()```: Timing must respect intended gradient accumulation.

<a id="skill-pytorch-lightning"></a>

### 70. pytorch-lightning — P1

Source: [skills-market/ai-ml/training/pytorch-lightning/SKILL.md](../../skills-market/ai-ml/training/pytorch-lightning/SKILL.md) · version `1.0.0`.

**Retain:** Define model/data/optimizer hooks with meaningful logged metrics and reproducible checkpoint/resume behavior.

**Findings:** Trainer examples mix API eras (seed, amp_backend, legacy callbacks); val_loss callbacks are shown without matching self.log in validation_step. One lifecycle skeleton omits superclass initialization.

**Keep / condense / move / delete:** Replace the mixed-era cookbook with one supported-version example and selective current references; explicitly connect metric production to monitored callbacks. Keep data/model boundaries and remove advertising and duplicated parameter catalogs.

**Trigger boundary:** Actual Lightning work, not any structured PyTorch training request.

**Evidence:**

- [skills-market/ai-ml/training/pytorch-lightning/SKILL.md:364](../../skills-market/ai-ml/training/pytorch-lightning/SKILL.md#L364) — `seed=42,  # Set seed`: Verify against Trainer signature; seeding is a separate API in current documentation.
- [skills-market/ai-ml/training/pytorch-lightning/SKILL.md:232](../../skills-market/ai-ml/training/pytorch-lightning/SKILL.md#L232) — `amp_backend=`: Legacy option requires version-specific correction.
- [skills-market/ai-ml/training/pytorch-lightning/SKILL.md:115](../../skills-market/ai-ml/training/pytorch-lightning/SKILL.md#L115) — `return {"val_loss": loss}`: Returning a value alone is not the demonstrated self.log contract for monitored metrics.

Primary documentation checked: [Lightning Trainer API](https://lightning.ai/docs/pytorch/stable/core-api/trainer).

<a id="skill-bitsandbytes"></a>

### 71. bitsandbytes — P1

Source: [skills-market/ai-ml/llm/bitsandbytes/SKILL.md](../../skills-market/ai-ml/llm/bitsandbytes/SKILL.md) · version `1.0.0`.

**Retain:** Choose supported quantization/compute settings and distinguish inference placement from adapter-training requirements.

**Findings:** Imports BitsAndBytesConfig from bitsandbytes rather than Transformers; examples add questionable bnb_4bit_bits and use device_map=auto indiscriminately for training. Memory estimates omit activation/optimizer/context assumptions.

**Keep / condense / move / delete:** Fix imports and validate config signatures first. Keep quantization/compute dtype distinctions and frozen-weight adapter logic; condense repeated generation examples, qualify memory tables, remove advertising.

**Trigger boundary:** Keep explicit quantization or k-bit adaptation intent; exclude ordinary full-precision loading.

**Evidence:**

- [skills-market/ai-ml/llm/bitsandbytes/SKILL.md:36](../../skills-market/ai-ml/llm/bitsandbytes/SKILL.md#L36) — `from bitsandbytes import BitsAndBytesConfig`: Official Transformers integration imports this configuration from transformers.
- [skills-market/ai-ml/llm/bitsandbytes/SKILL.md:138](../../skills-market/ai-ml/llm/bitsandbytes/SKILL.md#L138) — `bnb_4bit_bits=4`: Configuration field requires verification before example reuse.

Primary documentation checked: [Transformers bitsandbytes integration](https://huggingface.co/docs/transformers/quantization/bitsandbytes).

<a id="skill-transformers"></a>

### 72. transformers — P1

Source: [skills-market/ai-ml/llm/transformers/SKILL.md](../../skills-market/ai-ml/llm/transformers/SKILL.md) · version `1.0.0`.

**Retain:** Match model/tokenizer/task/head and preserve attention masks, labels, device placement and evaluation meaning.

**Findings:** Loads variables gpt and t5 then calls model.generate on a previous unrelated model. Feature extraction computes unmasked mean pooling and returns only CLS. Large generic recipes and marketing obscure task-specific contracts.

**Keep / condense / move / delete:** Replace inconsistent snippets with one runnable task-specific example, mask padded pooling, and distinguish inference/eval from training. Keep head/tokenizer/output-shape checks; remove advertising and repeated model catalogs.

**Trigger boundary:** Actual Transformers library tasks; distinguish Hub management and adapter/preference trainers.

**Evidence:**

- [skills-market/ai-ml/llm/transformers/SKILL.md:297](../../skills-market/ai-ml/llm/transformers/SKILL.md#L297) — `gpt = GPT2LMHeadModel`: Subsequent generation calls the wrong variable, model.
- [skills-market/ai-ml/llm/transformers/SKILL.md:391](../../skills-market/ai-ml/llm/transformers/SKILL.md#L391) — `mean(dim=1)`: Pooling ignores padding when applied to padded batches.

<a id="skill-peft"></a>

### 73. peft — P1

Source: [skills-market/ai-ml/llm/peft/SKILL.md](../../skills-market/ai-ml/llm/peft/SKILL.md) · version `1.0.0`.

**Retain:** Preserve correct trainable adapter targets, k-bit preparation, loss-bearing data, and base/adapter compatibility.

**Findings:** Causal-LM example trains on tokenized IMDb labels without a language-model label/collation contract. add_adapter result is assigned back to model and generic AdapterConfig/adapter_type examples need current-API verification. Manual loop does not zero gradients.

**Keep / condense / move / delete:** Correct one runnable adaptation example with labels, target inspection and trainable-parameter checks; verify adapter creation/load/merge return contracts. Remove blanket merge advice, memory promises, generic cookbook and advertising.

**Trigger boundary:** Explicit parameter-efficient adaptation; exclude ordinary model loading and full fine-tuning.

**Evidence:**

- [skills-market/ai-ml/llm/peft/SKILL.md:299](../../skills-market/ai-ml/llm/peft/SKILL.md#L299) — `model = model.add_adapter`: Return contract must not replace the model with a non-model result.
- [skills-market/ai-ml/llm/peft/SKILL.md:211](../../skills-market/ai-ml/llm/peft/SKILL.md#L211) — `from peft import AdapterConfig`: Needs verification against the actual supported adapter APIs.

<a id="skill-trl"></a>

### 74. trl — P1

Source: [skills-market/ai-ml/llm/trl/SKILL.md](../../skills-market/ai-ml/llm/trl/SKILL.md) · version `1.0.0`.

**Retain:** Select a supported trainer and preserve instruction/preference/reward data and loss contracts.

**Findings:** Imports RLHFTrainer/RLHFConfig without verified API support, mixes trainer arguments from different versions, assumes a prompt column in the selected hh-rlhf dataset and includes undefined output_length_sampler. Cookbook labels an unspecified custom loss as directly supported.

**Keep / condense / move / delete:** Rebuild around a pinned, runnable SFT or DPO workflow and verified dataset schema; keep actual preference/reference-model distinctions. Load PPO/reward details only when selected and remove invented APIs/advertising after source checks.

**Trigger boundary:** Specific TRL trainer/data work; exclude generic model alignment discussion.

**Evidence:**

- [skills-market/ai-ml/llm/trl/SKILL.md:35](../../skills-market/ai-ml/llm/trl/SKILL.md#L35) — `from trl.trainer import PPOTrainer, RLHFTrainer`: Trainer exports require current-source verification.
- [skills-market/ai-ml/llm/trl/SKILL.md:88](../../skills-market/ai-ml/llm/trl/SKILL.md#L88) — `example["prompt"]`: The selected dataset must actually expose this field.
- [skills-market/ai-ml/llm/trl/SKILL.md:211](../../skills-market/ai-ml/llm/trl/SKILL.md#L211) — `output_length_sampler(64)`: No definition or import is provided.

<a id="skill-accelerate"></a>

### 75. accelerate — P1

Source: [skills-market/ai-ml/training/accelerate/SKILL.md](../../skills-market/ai-ml/training/accelerate/SKILL.md) · version `1.0.0`.

**Retain:** Preserve prepared model/optimizer/data ownership, accumulation scaling, distributed metric semantics and resumable state.

**Findings:** Shows unsupported-looking config_file/distributed_type/num_processes constructor arguments; manually divides loss inside accumulate despite automatic accumulation scaling; save/load/get_states examples do not match the documented Accelerator API.

**Keep / condense / move / delete:** Verify against the actual Accelerator signature; fix accumulation and checkpoint examples first, retaining save_state versus model-export distinctions. Replace broad recipes and advertising with one runnable small example.

**Trigger boundary:** Actual Accelerate distributed/precision work, excluding generic multi-GPU discussion when another backend is chosen.

**Evidence:**

- [skills-market/ai-ml/training/accelerate/SKILL.md:109](../../skills-market/ai-ml/training/accelerate/SKILL.md#L109) — `config_file="./accelerate_config.yaml"`: Launcher configuration and Accelerator constructor are conflated.
- [skills-market/ai-ml/training/accelerate/SKILL.md:160](../../skills-market/ai-ml/training/accelerate/SKILL.md#L160) — `loss = criterion(outputs, targets) / gradient_accumulation_steps`: Risks double-scaling under configured accumulation.
- [skills-market/ai-ml/training/accelerate/SKILL.md:327](../../skills-market/ai-ml/training/accelerate/SKILL.md#L327) — `accelerator.get_states()`: Debugging method needs verification against actual API.

Primary documentation checked: [Accelerator API](https://huggingface.co/docs/accelerate/package_reference/accelerator).

<a id="skill-deepspeed"></a>

### 76. deepspeed — P1

Source: [skills-market/ai-ml/training/deepspeed/SKILL.md](../../skills-market/ai-ml/training/deepspeed/SKILL.md) · version `1.0.0`.

**Retain:** Preserve scalar loss, effective batch size, ZeRO ownership, precision and distributed checkpoint semantics.

**Findings:** Linear model returns a tensor assigned directly as loss before backward. Configuration examples mix stage-specific fields, quoted numeric values and auto values whose interpretation depends on the integration. Fixed memory multipliers are not universal.

**Keep / condense / move / delete:** Correct the scalar-loss and config contracts using supported-version docs; separate native DeepSpeed from Trainer/Accelerate integration. Keep partition/checkpoint behavior, condense generic recipes, and remove unsupported guarantees/advertising.

**Trigger boundary:** Specific DeepSpeed/ZeRO work; avoid auto-selecting this backend merely from model size.

**Evidence:**

- [skills-market/ai-ml/training/deepspeed/SKILL.md:61](../../skills-market/ai-ml/training/deepspeed/SKILL.md#L61) — `loss = model_engine(batch)`: The provided Linear model produces non-scalar output, not a defined scalar objective.
- [skills-market/ai-ml/training/deepspeed/SKILL.md:145](../../skills-market/ai-ml/training/deepspeed/SKILL.md#L145) — `stage3_param_persistence_threshold": "1e5"`: Quoted numeric config needs validation against the installed schema.

<a id="skill-huggingface-hub"></a>

### 77. huggingface-hub — P1

Source: [skills-market/ai-ml/llm/huggingface-hub/SKILL.md](../../skills-market/ai-ml/llm/huggingface-hub/SKILL.md) · version `1.0.0`.

**Retain:** Target the correct repository/revision and separate retrieval from authenticated publication.

**Findings:** Includes unverified hfc_api.set_lfs_patterns, legacy Repository/local_dir_use_symlinks/CLI usage, and a model-card example with invented metrics. Damaged heading text signals copy corruption; upload/public-repo examples lack clear task boundaries.

**Keep / condense / move / delete:** Refresh against supported Hub API/CLI, keep revision pinning and safe credentials, and use placeholders explicitly for example results. Route read/download/upload modes separately; remove repeated catalogs and advertising.

**Trigger boundary:** Hub artifact/repository management rather than every model/dataset task.

**Evidence:**

- [skills-market/ai-ml/llm/huggingface-hub/SKILL.md:379](../../skills-market/ai-ml/llm/huggingface-hub/SKILL.md#L379) — `from huggingface_hub import hfc_api`: Export/API needs verification before reuse.
- [skills-market/ai-ml/llm/huggingface-hub/SKILL.md:446](../../skills-market/ai-ml/llm/huggingface-hub/SKILL.md#L446) — ``commit_message`: Commit Resources``: Visible copy/format corruption reduces reliability.

<a id="skill-datasets"></a>

### 78. datasets — P1

Source: [skills-market/ai-ml/training/datasets/SKILL.md](../../skills-market/ai-ml/training/datasets/SKILL.md) · version `1.0.0`.

**Retain:** Preserve dataset versus split types, feature/schema meanings, deterministic split units and preprocessing lineage.

**Findings:** Memory-mapping example has broken code fences and a split heading embedded in code. Examples alternate Dataset and DatasetDict but later index train indiscriminately. Generic random splitting does not address group/entity leakage; streaming is equated with no caching.

**Keep / condense / move / delete:** Repair syntax and runnable split/type example first; explicitly identify group split units when needed and distinguish streaming from cache policy. Keep batched map/feature contracts, condense basic API catalogs, remove advertising.

**Trigger boundary:** Hugging Face Datasets operations, not all dataset processing.

**Evidence:**

- [skills-market/ai-ml/training/datasets/SKILL.md:341](../../skills-market/ai-ml/training/datasets/SKILL.md#L341) — ``Memory-map to save RAM`````: Malformed fence corrupts the code example.
- [skills-market/ai-ml/training/datasets/SKILL.md:237](../../skills-market/ai-ml/training/datasets/SKILL.md#L237) — `tokenized_dataset["train"]`: Only valid when the actual object is a DatasetDict with that split.

<a id="skill-spatialdata"></a>

### 79. spatialdata — P1

Source: [skills-market/compbio/spatial-omics/analysis/spatialdata/SKILL.md](../../skills-market/compbio/spatial-omics/analysis/spatialdata/SKILL.md) · version `1.0.0`.

**Retain:** Preserve named spatial elements, linked table regions and coordinate transformations across modalities.

**Findings:** Short entrypoint relies on unverified SpatialData.read/sdata.table/to_adata calls and is largely a product summary. It never establishes table-region joins or element-coordinate contracts.

**Keep / condense / move / delete:** Replace with a supported-version minimal round-trip example, actual table access, coordinate-system inspection and ID alignment; remove generic platform catalog. Shortness is not a reason to retain unverifiable code.

**Trigger boundary:** Specific SpatialData container/transform/IO tasks rather than all multimodal integration.

**Evidence:**

- [skills-market/compbio/spatial-omics/analysis/spatialdata/SKILL.md:69](../../skills-market/compbio/spatial-omics/analysis/spatialdata/SKILL.md#L69) — `sdata.table.to_adata()`: Access/conversion contract must be verified against the real API.

<a id="skill-vitessce"></a>

### 80. vitessce — P1

Source: [skills-market/compbio/spatial-omics/visualization/vitessce/SKILL.md](../../skills-market/compbio/spatial-omics/visualization/vitessce/SKILL.md) · version `1.0.0`.

**Retain:** Create a valid viewer configuration with matching data loaders, schemas and linked views.

**Findings:** Uses unverified ViewConf, FileType.H5AD, data_type, export_plugins and CLI initialization without a supported version; example points only to a placeholder URL.

**Keep / condense / move / delete:** Rebuild one actual Python-config example from current Vitessce docs with a local toy data fixture and validated export. Keep view/data linkage and replace vague feature lists with loader constraints.

**Trigger boundary:** Explicit Vitessce configuration/viewer work, not generic visualization.

**Evidence:**

- [skills-market/compbio/spatial-omics/visualization/vitessce/SKILL.md:65](../../skills-market/compbio/spatial-omics/visualization/vitessce/SKILL.md#L65) — `vc.export_plugins()`: No source-backed API contract or bundled implementation supports the call in this skill.

<a id="skill-stereo-seq"></a>

### 81. stereo-seq — P1

Source: [skills-market/compbio/spatial-omics/platforms/stereo-seq/SKILL.md](../../skills-market/compbio/spatial-omics/platforms/stereo-seq/SKILL.md) · version `1.0.0`.

**Retain:** Preserve assay resolution/binning, gene/cell orientation and exact coordinate-to-observation alignment.

**Findings:** Python assigns coords.values by position; R overwrites coordinate row names with cell names, potentially relabeling unmatched rows. Workflow is generic CSV preprocessing, omitting actual platform-format/bin contracts.

**Keep / condense / move / delete:** Require ID-based alignment and explicit orientation, then use verified platform readers/bin units. Keep spatial-scale checks; label QC parameters as dataset-dependent and remove empty analysis headings.

**Trigger boundary:** Actual Stereo-seq data, not any high-resolution spatial dataset.

**Evidence:**

- [skills-market/compbio/spatial-omics/platforms/stereo-seq/SKILL.md:50](../../skills-market/compbio/spatial-omics/platforms/stereo-seq/SKILL.md#L50) — `adata.obsm['spatial'] = coords.values`: Positional assignment can silently misregister expression and tissue coordinates.
- [skills-market/compbio/spatial-omics/platforms/stereo-seq/SKILL.md:77](../../skills-market/compbio/spatial-omics/platforms/stereo-seq/SKILL.md#L77) — `rownames(meta) <- colnames(stereo)`: Relabels coordinates instead of proving alignment.

<a id="skill-giotto"></a>

### 82. giotto — P1

Source: [skills-market/compbio/spatial-omics/analysis/giotto/SKILL.md](../../skills-market/compbio/spatial-omics/analysis/giotto/SKILL.md) · version `1.0.0`.

**Retain:** Create a valid Giotto object with aligned expression/location/image inputs and version-compatible spatial analyses.

**Findings:** Installation/constructor paths mix Giotto and GiottoSuite; Visium example defines a questionable tissue_positions.json and passes an expression directory as raw_expr. Spatial statistics and integration sections are placeholders.

**Keep / condense / move / delete:** Choose a supported Giotto release, verify an actual reader/constructor example, and preserve coordinate units/ID alignment. Remove placeholder promises and duplicate product description.

**Trigger boundary:** Explicit Giotto R tasks rather than all spatial analysis in R.

**Evidence:**

- [skills-market/compbio/spatial-omics/analysis/giotto/SKILL.md:63](../../skills-market/compbio/spatial-omics/analysis/giotto/SKILL.md#L63) — `raw_expr = expr_path`: Constructor input semantics must match the chosen release and reader.

<a id="skill-scribble"></a>

### 83. scribble — P1

Source: [skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md](../../skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md) · version `1.0.0`.

**Retain:** An integration skill needs a verified algorithm/package identity and modality-alignment contract.

**Findings:** The only GitHub installation URL is username/scribble, documentation says merely check GitHub, and integrate(cca/mnn/wnn) has no supporting implementation or source. This is an unverified scaffold, not a reliable integration workflow.

**Keep / condense / move / delete:** Resolve intended tool and authoritative source before any installation/use; replace placeholder APIs with a demonstrated example or propose retirement separately. Do not infer a similarly named package is the intended bioinformatics tool.

**Trigger boundary:** Require verified tool identity; broad multi-omics intent is unsafe routing for this placeholder.

**Evidence:**

- [skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md:33](../../skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md#L33) — `github.com/username/scribble.git`: Explicit placeholder provenance.
- [skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md:85](../../skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md#L85) — `Check GitHub for latest information`: No actual documentation source is provided.

<a id="skill-human-cell-atlas"></a>

### 84. human-cell-atlas — P1

Source: [skills-market/compbio/databases/human-cell-atlas/SKILL.md](../../skills-market/compbio/databases/human-cell-atlas/SKILL.md) · version `1.0.0`.

**Retain:** Find HCA datasets with clear project provenance and retrieve the intended data/metadata.

**Findings:** Primary code instead opens CELLxGENE Census and supplies a tissue keyword without a verified API contract. It conflates separate data-access services and leaves marker/reference workflows empty.

**Keep / condense / move / delete:** Separate HCA portal/API access from Census; verify requested coverage and project IDs, then provide an actual source-backed query/download example. Remove unsupported feature promises.

**Trigger boundary:** HCA-specific retrieval/provenance work; route Census queries explicitly to its own skill.

**Evidence:**

- [skills-market/compbio/databases/human-cell-atlas/SKILL.md:31](../../skills-market/compbio/databases/human-cell-atlas/SKILL.md#L31) — `Using cellxgene-census (for HCA data)`: Distinct services/coverage are conflated.
- [skills-market/compbio/databases/human-cell-atlas/SKILL.md:41](../../skills-market/compbio/databases/human-cell-atlas/SKILL.md#L41) — `tissue="lung"`: Verify against the actual Census query signature.

<a id="skill-anndatar"></a>

### 85. anndatar — P1

Source: [skills-market/compbio/single-cell/analysis/anndatar/SKILL.md](../../skills-market/compbio/single-cell/analysis/anndatar/SKILL.md) · version `1.0.0`.

**Retain:** Convert H5AD/R objects while preserving orientation, IDs, assays/layers and embeddings.

**Findings:** Contains visibly corrupted R code PCsstructured metadata and broad h5ad routing that overlaps AnnData/schard. Comparison claims and mapping defaults lack a documented round-trip check.

**Keep / condense / move / delete:** Repair corrupted example; keep backed-mode and conversion choices, add a small layer/ID/embedding round-trip contract, and load detailed examples only for the selected conversion. Avoid blanket tool rankings.

**Trigger boundary:** Explicit R-native conversion intent, not every AnnData file mention.

**Evidence:**

- [skills-market/compbio/single-cell/analysis/anndatar/SKILL.md:125](../../skills-market/compbio/single-cell/analysis/anndatar/SKILL.md#L125) — `PCsstructured metadata`: Visible copy corruption inside executable-looking R code.

<a id="skill-schard"></a>

### 86. schard — P1

Source: [skills-market/compbio/single-cell/analysis/schard/SKILL.md](../../skills-market/compbio/single-cell/analysis/schard/SKILL.md) · version `1.0.0`.

**Retain:** Convert selected H5AD components while preserving exact cell/feature identity and intended assay meaning.

**Findings:** Labels /raw/X as raw counts, although a raw snapshot can hold normalized/log expression. Hardcoded downloads/slide IDs and reduction names are example-specific.

**Keep / condense / move / delete:** Require inspecting raw/layer provenance rather than assuming counts; keep component-path/orientation decisions and verify conversion results. Move specific public data recipes to optional examples and distinguish from anndataR.

**Trigger boundary:** Explicit schard conversion or an H5AD-to-R need for which this tool is chosen.

**Evidence:**

- [skills-market/compbio/single-cell/analysis/schard/SKILL.md:125](../../skills-market/compbio/single-cell/analysis/schard/SKILL.md#L125) — ```/raw/X` | Raw counts matrix``: Storage location alone does not establish count semantics.

<a id="skill-snakemake"></a>

### 87. snakemake — P1

Source: [skills-market/compbio/workflows/snakemake/SKILL.md](../../skills-market/compbio/workflows/snakemake/SKILL.md) · version `1.0.0`.

**Retain:** Build a valid dependency DAG whose declared outputs are actually produced, with pinned tools and assay-aware input contracts.

**Findings:** Basic example redirects bwa SAM output to a .bam name. Claimed complete single-cell pipeline ends rule all at QC, declares an unproduced JSON file, and omits barcode/UMI handling. Cluster/cloud flags span versions.

**Keep / condense / move / delete:** Correct one dry-run-capable workflow and its true output formats first; label bulk-RNA illustration honestly. Keep DAG/resources/environment rules and use version-supported executor profiles.

**Trigger boundary:** Explicit Snakemake workflow work, not any reproducibility request.

**Evidence:**

- [skills-market/compbio/workflows/snakemake/SKILL.md:52](../../skills-market/compbio/workflows/snakemake/SKILL.md#L52) — `bwa mem {input} > {output}`: Declared BAM does not match the command's direct SAM output.
- [skills-market/compbio/workflows/snakemake/SKILL.md:72](../../skills-market/compbio/workflows/snakemake/SKILL.md#L72) — `json="results/{sample}/qc_metrics.json"`: Shown shell commands do not produce this output.

<a id="skill-nextflow"></a>

### 88. nextflow — P1

Source: [skills-market/compbio/workflows/nextflow/SKILL.md](../../skills-market/compbio/workflows/nextflow/SKILL.md) · version `1.0.0`.

**Retain:** Preserve channel tuple shapes, declared process outputs, sample identity and selected execution profile.

**Findings:** Example uses paramsreads/paramsindex instead of proper params fields; fromFilePairs tuples are passed into path-only inputs, and GTF is undefined. A generic paired-end featureCounts workflow is called single-cell without barcode/UMI processing.

**Keep / condense / move / delete:** Replace with a valid DSL2 toy workflow or pinned nf-core example; verify channel/output contracts and distinguish workflow execution from cloud deployment. Remove broad profile assumptions and broken flag examples after checking current help.

**Trigger boundary:** Explicit Nextflow/nf-core tasks.

**Evidence:**

- [skills-market/compbio/workflows/nextflow/SKILL.md:71](../../skills-market/compbio/workflows/nextflow/SKILL.md#L71) — `paramsreads =`: Configuration variables are malformed/inconsistent with later params.gtf.
- [skills-market/compbio/workflows/nextflow/SKILL.md:119](../../skills-market/compbio/workflows/nextflow/SKILL.md#L119) — `reads = Channel.fromFilePairs(paramsreads)`: Tuple structure must match process input declarations.

<a id="skill-squidpy"></a>

### 89. squidpy — P1

Source: [skills-market/compbio/spatial-omics/analysis/squidpy/SKILL.md](../../skills-market/compbio/spatial-omics/analysis/squidpy/SKILL.md) · version `1.0.0`.

**Retain:** Construct the intended spatial graph with correct library boundaries/coordinates and valid statistical tests.

**Findings:** Installation targets squidpy_notebooks; multiple method/parameter names need verification, including spatialHeatmap/interactive/n_pcs. It claims ordinary Scanpy neighbors combines spatial and transcriptional information, which the shown call does not do, and ranks Moran I values under a significant-genes comment without testing significance.

**Keep / condense / move / delete:** Correct package/API calls and graph/statistical semantics before shortening. Keep image registration, library isolation and spatial-scale constraints; reduce generic recipes to one supported example.

**Trigger boundary:** Squidpy-specific spatial analyses; exclude generic preprocessing handled by Scanpy.

**Evidence:**

- [skills-market/compbio/spatial-omics/analysis/squidpy/SKILL.md:103](../../skills-market/compbio/spatial-omics/analysis/squidpy/SKILL.md#L103) — `using both transcriptional and spatial`: The shown sc.pp.neighbors call specifies no spatial integration.
- [skills-market/compbio/spatial-omics/analysis/squidpy/SKILL.md:180](../../skills-market/compbio/spatial-omics/analysis/squidpy/SKILL.md#L180) — `Filter significant genes`: Sorting the I statistic alone does not select by corrected significance.

<a id="skill-archr"></a>

### 90. archr — P1

Source: [skills-market/compbio/multiomics/scATAC-seq/archr/SKILL.md](../../skills-market/compbio/multiomics/scATAC-seq/archr/SKILL.md) · version `1.0.0`.

**Retain:** Preserve genome/build, Arrow/project stages, LSI/peak matrices and legitimate reference-RNA integration.

**Findings:** Calls addIterativeLSA and several other unverified APIs; peak analysis occurs before a peak matrix is established; gene integration is described as creating RNA without a reference. Installation guidance treats a genome package as a CRAN package.

**Keep / condense / move / delete:** Rebuild a verified minimal ArchR workflow with the real stage dependencies and genome annotation source; keep TSS/fragment/bias decisions, clearly separate gene scores from observed expression, and remove placeholder exports.

**Trigger boundary:** Explicit ArchR object/analysis tasks.

**Evidence:**

- [skills-market/compbio/multiomics/scATAC-seq/archr/SKILL.md:87](../../skills-market/compbio/multiomics/scATAC-seq/archr/SKILL.md#L87) — `addIterativeLSA(`: Needs correction against the actual iterative LSI API.
- [skills-market/compbio/multiomics/scATAC-seq/archr/SKILL.md:196](../../skills-market/compbio/multiomics/scATAC-seq/archr/SKILL.md#L196) — `in absence of scRNA-seq`: Reference-based integration must not be described as measured expression recovery.

<a id="skill-signac"></a>

### 91. signac — P1

Source: [skills-market/compbio/multiomics/scATAC-seq/signac/SKILL.md](../../skills-market/compbio/multiomics/scATAC-seq/signac/SKILL.md) · version `1.0.0`.

**Retain:** Preserve chromatin assay identity, genome/fragment linkage, TF-IDF/LSI and valid gene-activity/reference mapping.

**Findings:** Reassigns pbmc to GeneActivity output and then accesses it as a Seurat object; FindSVD and several integration arguments need verification. Assay annotations and matched feature spaces are not established.

**Keep / condense / move / delete:** Correct one official-version workflow, storing gene-activity matrix separately and using actual LSI and transfer methods. Preserve QC/genome and cell alignment; make cross-modality integration conditional on real matching biology.

**Trigger boundary:** Specific Signac/Seurat chromatin operations.

**Evidence:**

- [skills-market/compbio/multiomics/scATAC-seq/signac/SKILL.md:121](../../skills-market/compbio/multiomics/scATAC-seq/signac/SKILL.md#L121) — `pbmc <- GeneActivity(`: The returned matrix should not overwrite the Seurat object.
- [skills-market/compbio/multiomics/scATAC-seq/signac/SKILL.md:96](../../skills-market/compbio/multiomics/scATAC-seq/signac/SKILL.md#L96) — `FindSVD(pbmc`: Verify the supported SVD function and resulting reduction name.

<a id="skill-cellxgene"></a>

### 92. cellxgene — P1

Source: [skills-market/compbio/single-cell/visualization/cellxgene/SKILL.md](../../skills-market/compbio/single-cell/visualization/cellxgene/SKILL.md) · version `1.0.0`.

**Retain:** Prepare a valid, interpretable dataset and launch the intended local viewer without unintended exposure.

**Findings:** Gives speculative notebook/Flask APIs then claims no Python customization API. CLI examples/config formats need verification; host 0.0.0.0 is shown without distinguishing network exposure, and an h5api typo appears.

**Keep / condense / move / delete:** Keep dataset/annotation/embedding preparation and local launch. Replace invented-looking integration recipes with current supported examples; scope network binding to the requested sharing setup and remove unsupported size limits.

**Trigger boundary:** The actual CELLxGENE viewer, distinct from Census retrieval.

**Evidence:**

- [skills-market/compbio/single-cell/visualization/cellxgene/SKILL.md:143](../../skills-market/compbio/single-cell/visualization/cellxgene/SKILL.md#L143) — `cellxgene.launch.build_index()`: Unverified embedding contract conflicts with the later stated API limitation.
- [skills-market/compbio/single-cell/visualization/cellxgene/SKILL.md:181](../../skills-market/compbio/single-cell/visualization/cellxgene/SKILL.md#L181) — `data.h5api`: Filename typo undermines runnable launch guidance.

<a id="skill-scanpy"></a>

### 93. scanpy — P1

Source: [skills-market/compbio/single-cell/analysis/scanpy/SKILL.md](../../skills-market/compbio/single-cell/analysis/scanpy/SKILL.md) · version `1.0.0`.

**Retain:** Preserve count/normalized/scaled layers and valid sample-aware QC, graph, marker and condition comparisons.

**Findings:** Saves adata.raw after normalize/log yet calls it raw counts and says use_raw shows original counts. UMAP colors leiden before clustering; fixed QC/cluster-to-celltype examples risk false annotation, and condition DE ignores biological replication.

**Keep / condense / move / delete:** Correct raw/count semantics in the entrypoint and inspect duplicated templates/references. Preserve raw counts explicitly, justify QC and labels from evidence, distinguish exploratory cell markers from replicate-level condition inference, and remove advertising/repeated tutorials.

**Trigger boundary:** Scanpy analysis intent; keep AnnData-format and probabilistic-model exclusions.

**Evidence:**

- [skills-market/compbio/single-cell/analysis/scanpy/SKILL.md:111](../../skills-market/compbio/single-cell/analysis/scanpy/SKILL.md#L111) — `Save raw counts for later`: Occurs after normalization/log transformation, so count semantics are false.
- [skills-market/compbio/single-cell/analysis/scanpy/SKILL.md:306](../../skills-market/compbio/single-cell/analysis/scanpy/SKILL.md#L306) — `Shows original counts`: use_raw reads the stored snapshot, not necessarily original counts.

<a id="skill-anndata"></a>

### 94. anndata — P1

Source: [skills-market/compbio/single-cell/analysis/anndata/SKILL.md](../../skills-market/compbio/single-cell/analysis/anndata/SKILL.md) · version `1.0.0`.

**Retain:** Preserve annotated-matrix axis identity, layers, sparse/backed semantics and safe views/concatenation.

**Findings:** Calls ad.read_10x_h5 (a Scanpy reader) and passes filename strings to AnnCollection without verifying its accepted object types. A full Scanpy workflow duplicates other skills despite a format-specific description.

**Keep / condense / move / delete:** Fix namespace/object contracts; keep alignment, backed-mode and sparse/view pitfalls. Remove general analysis recipes and advertising, and load IO/concatenation references by task.

**Trigger boundary:** Annotated container/IO transformations, not all single-cell analysis.

**Evidence:**

- [skills-market/compbio/single-cell/analysis/anndata/SKILL.md:73](../../skills-market/compbio/single-cell/analysis/anndata/SKILL.md#L73) — `ad.read_10x_h5`: Reader ownership needs correction to the documented package namespace.
- [skills-market/compbio/single-cell/analysis/anndata/SKILL.md:171](../../skills-market/compbio/single-cell/analysis/anndata/SKILL.md#L171) — `['data1.h5ad', 'data2.h5ad']`: AnnCollection input object contract needs verification.

<a id="skill-seurat"></a>

### 95. seurat — P1

Source: [skills-market/compbio/single-cell/analysis/seurat/SKILL.md](../../skills-market/compbio/single-cell/analysis/seurat/SKILL.md) · version `1.0.0`.

**Retain:** Preserve assay identity, counts, cell metadata, and marker-based interpretation through Seurat analysis.

**Findings:** The generic recipe assigns fixed PBMC cluster labels and QC cutoffs to arbitrary inputs, uses an unverified LoadH5AD interface, and includes the legacy thresh.use argument and a broken code fence. These are correctness issues before context-cost issues.

**Keep / condense / move / delete:** Keep assay/count and biological validation rules; replace the example with a versioned, runnable workflow. Move optional visualization recipes to references and delete fixed labels as a general instruction.

**Trigger boundary:** Specify Seurat analysis or conversion; distinguish v5 layer/integration work from the separate seurat-v5 skill.

**Evidence:**

- [skills-market/compbio/single-cell/analysis/seurat/SKILL.md:156](../../skills-market/compbio/single-cell/analysis/seurat/SKILL.md#L156) — `new.cluster.ids <-`: Dataset-specific labels are presented inside the general workflow.
- [skills-market/compbio/single-cell/analysis/seurat/SKILL.md:168](../../skills-market/compbio/single-cell/analysis/seurat/SKILL.md#L168) — `thresh.use = 0.25`: Version-sensitive marker argument needs replacement or explicit version support.

<a id="skill-scvi-tools"></a>

### 96. scvi-tools — P2

Source: [skills-market/compbio/single-cell/analysis/scvi-tools/SKILL.md](../../skills-market/compbio/single-cell/analysis/scvi-tools/SKILL.md) · version `1.0.0`.

**Retain:** Select the model and register the correct AnnData fields before fitting and interpreting latent representations.

**Findings:** The universal API/raw-count claims flatten differences among models and modalities. Examples assume counts, batch, donor and mitochondrial fields without first establishing them. Model catalogs and broad claims of biological preservation exceed the useful execution contract.

**Keep / condense / move / delete:** Keep model-specific input/loss/registration contracts and uncertainty; condense the overview, move model variants to references, and verify examples against a declared scvi-tools version.

**Trigger boundary:** Require explicit scvi-tools modeling or a matching count-based integration task; do not route every single-cell analysis here.

**Evidence:**

- [skills-market/compbio/single-cell/analysis/scvi-tools/SKILL.md:69](../../skills-market/compbio/single-cell/analysis/scvi-tools/SKILL.md#L69) — `All scvi-tools models follow`: An overbroad API guarantee replaces model-specific contracts.
- [skills-market/compbio/single-cell/analysis/scvi-tools/SKILL.md:183](../../skills-market/compbio/single-cell/analysis/scvi-tools/SKILL.md#L183) — `Always provide unnormalized count data`: The requirement needs a named model and modality.

<a id="skill-monocle3"></a>

### 97. monocle3 — P1

Source: [skills-market/compbio/single-cell/analysis/monocle3/SKILL.md](../../skills-market/compbio/single-cell/analysis/monocle3/SKILL.md) · version `1.0.0`.

**Retain:** Infer and interpret a rooted trajectory while preserving partitions and distinguishing pseudotime from biological time or causation.

**Findings:** Monocle 2 BEAM/branched-plot methods are mixed into a Monocle 3 recipe. Other pseudotime helper calls need verification. Repeated sections and example-specific root selection conceal the actual graph/root contract.

**Keep / condense / move / delete:** Keep root justification, partition handling and interpretation limits. Replace incompatible APIs, consolidate duplicate workflows, and move optional plotting/branch variants to references.

**Trigger boundary:** Limit to Monocle 3 trajectory inference and troubleshooting; do not imply causal lineage validation.

**Evidence:**

- [skills-market/compbio/single-cell/analysis/monocle3/SKILL.md:201](../../skills-market/compbio/single-cell/analysis/monocle3/SKILL.md#L201) — `BranchP <- BEAM`: Monocle 2 method in a Monocle 3 workflow.
- [skills-market/compbio/single-cell/analysis/monocle3/SKILL.md:186](../../skills-market/compbio/single-cell/analysis/monocle3/SKILL.md#L186) — `find_genes_that_differ_with_pseudotime`: Unverified API is repeated as executable guidance.

<a id="skill-seurat-v5"></a>

### 98. seurat-v5 — P1

Source: [skills-market/compbio/single-cell/integration/seurat-v5/SKILL.md](../../skills-market/compbio/single-cell/integration/seurat-v5/SKILL.md) · version `1.0.0`.

**Retain:** Handle Seurat v5 assays/layers and multimodal integration with explicit cell alignment and graph identity.

**Findings:** WNN clustering selects group.by rather than the WNN graph; the CITE-seq loading example uses Load10X_Spatial; vdj=FALSE is offered as a ScaleData optimization. The v4/v5 comparison also attributes older WNN capabilities to v5.

**Keep / condense / move / delete:** Keep layer, assay and paired-cell invariants; replace the recipe with an official v5 workflow and named graph. Delete unsupported optimization and feature claims; reference optional recipes.

**Trigger boundary:** Require v5 layers, integration or multimodal work; coordinate with seurat rather than trigger for all single-cell tasks.

**Evidence:**

- [skills-market/compbio/single-cell/integration/seurat-v5/SKILL.md:113](../../skills-market/compbio/single-cell/integration/seurat-v5/SKILL.md#L113) — `group.by = "wnn"`: Does not explicitly select the WNN clustering graph.
- [skills-market/compbio/single-cell/integration/seurat-v5/SKILL.md:247](../../skills-market/compbio/single-cell/integration/seurat-v5/SKILL.md#L247) — `ScaleData(cbmc, vdj = FALSE)`: Unsupported optimization needs removal or API evidence.

Primary documentation checked: [Seurat FindClusters API](https://satijalab.org/seurat/reference/findclusters).

<a id="skill-harmony"></a>

### 99. harmony — P1

Source: [skills-market/compbio/single-cell/integration/harmony/SKILL.md](../../skills-market/compbio/single-cell/integration/harmony/SKILL.md) · version `1.0.0`.

**Retain:** Correct a PCA embedding for named technical batches without treating the corrected embedding as expression counts or guaranteed biology.

**Findings:** The lambda guidance says higher values cause more aggressive correction and advises decreasing lambda for overcorrection. This direction requires correction against RunHarmony documentation. Loading and metadata examples also assume uncreated batch fields.

**Keep / condense / move / delete:** Keep embedding ownership and checks for biological preservation; correct parameter directions and validate the batch metadata. Condense the tutorial and move tuning variants to references.

**Trigger boundary:** Harmony embedding integration and troubleshooting, not general differential expression or count correction.

**Evidence:**

- [skills-market/compbio/single-cell/integration/harmony/SKILL.md:98](../../skills-market/compbio/single-cell/integration/harmony/SKILL.md#L98) — `Higher values = more aggressive integration`: Regularization direction needs primary-source correction.
- [skills-market/compbio/single-cell/integration/harmony/SKILL.md:208](../../skills-market/compbio/single-cell/integration/harmony/SKILL.md#L208) — `- Decrease lambda`: Advice risks worsening overcorrection.

Primary documentation checked: [RunHarmony parameter reference](https://portals.broadinstitute.org/harmony/reference/RunHarmony.html).

<a id="skill-scanorama"></a>

### 100. scanorama — P1

Source: [skills-market/compbio/single-cell/integration/scanorama/SKILL.md](../../skills-market/compbio/single-cell/integration/scanorama/SKILL.md) · version `1.0.0`.

**Retain:** Align genes and cells across datasets and distinguish corrected matrices from integrated embeddings.

**Findings:** The neighborhood example is syntactically broken at adata_combina. Other snippets mix AnnData and matrix APIs and use Approximate=True; a citation points to a Harmony paper. Batch coloring also assumes metadata not established in the concatenation example.

**Keep / condense / move / delete:** Keep gene/cell alignment; rebuild one runnable example using the supported API and correct citation. Delete broken or duplicated examples before moving optional variants to references.

**Trigger boundary:** Scanorama integration or troubleshooting; exclude arbitrary single-cell analysis.

**Evidence:**

- [skills-market/compbio/single-cell/integration/scanorama/SKILL.md:104](../../skills-market/compbio/single-cell/integration/scanorama/SKILL.md#L104) — `adata_combina`: Truncated variable and broken syntax in executable example.
- [skills-market/compbio/single-cell/integration/scanorama/SKILL.md:128](../../skills-market/compbio/single-cell/integration/scanorama/SKILL.md#L128) — `Approximate=True`: Case-sensitive API argument needs verification.

<a id="skill-bbknn"></a>

### 101. bbknn — P1

Source: [skills-market/compbio/single-cell/integration/bbknn/SKILL.md](../../skills-market/compbio/single-cell/integration/bbknn/SKILL.md) · version `1.0.0`.

**Retain:** Construct a batch-balanced neighbor graph while retaining the original expression matrix and assessing biological structure.

**Findings:** The parameter catalog supplies k, lam and ref_batch as BBKNN arguments without a supported API contract. The text conflates graph balancing with corrected expression and makes unsupported comparative accuracy claims.

**Keep / condense / move / delete:** Keep graph-versus-expression distinction; replace the parameter list and examples from the actual signature. Condense generic Scanpy workflow and delete unsubstantiated rankings.

**Trigger boundary:** BBKNN graph construction and troubleshooting, not expression correction or all integration tasks.

**Evidence:**

- [skills-market/compbio/single-cell/integration/bbknn/SKILL.md:75](../../skills-market/compbio/single-cell/integration/bbknn/SKILL.md#L75) — `lam=1`: Unverified parameter in the main recipe.
- [skills-market/compbio/single-cell/integration/bbknn/SKILL.md:123](../../skills-market/compbio/single-cell/integration/bbknn/SKILL.md#L123) — `ref_batch='batch1'`: Reference-batch interface needs primary-source support.

Primary documentation checked: [BBKNN API](https://bbknn.readthedocs.io/en/latest/bbknn.bbknn.html).

<a id="skill-chimerax-mcp"></a>

### 102. chimerax-mcp — P3

Source: [skills-market/compbio/structural-biology/chimerax-mcp/SKILL.md](../../skills-market/compbio/structural-biology/chimerax-mcp/SKILL.md) · version `1.0.0`.

**Retain:** Use API/MCP access to the correct ChimeraX session, preserve model identity and measurement meaning, and export only when requested.

**Findings:** The skill already scopes routing, setup, session identity and export well. Incident-derived model identifiers can remain examples but should not become permanent assumptions. No mandatory cut is justified by length alone.

**Keep / condense / move / delete:** Keep session/transport, selection, measurement and requested-export invariants. Condense only repeated troubleshooting and move historical explanation to existing lessons when it does not change execution.

**Trigger boundary:** Already specific to ChimeraX API visualization/setup; preserve the exclusions and aligned UI metadata.

**Stop condition:** Stop when the requested view, measurement, setup repair or export is verified in the selected session; do not add unsolicited exports.

**Evidence:**

- [skills-market/compbio/structural-biology/chimerax-mcp/SKILL.md:12](../../skills-market/compbio/structural-biology/chimerax-mcp/SKILL.md#L12) — `An on-screen styling request does not imply export`: Useful authorization boundary.

<a id="skill-computational-biology-retrospective"></a>

### 103. computational-biology-retrospective — P3

Source: [skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md](../../skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md) · version `1.0.0`.

**Retain:** Trace project claims from the research record to code, execution evidence and result artifacts, preserving uncertainty.

**Findings:** The skill makes valuable distinctions between intent, executed behavior, numerical results and biological validity. Missing artifacts reduce coverage without blocking all progress, and optional lenses are explicitly non-mandatory. Some repeated evidence rules and historical influences could be shortened.

**Keep / condense / move / delete:** Keep provenance and scope constraints. Condense repeated explanations; retain conditional references rather than forcing all lenses or new experiments.

**Trigger boundary:** Already limited to retrospective evidence synthesis, excluding running new experiments and manuscript drafting alone.

**Stop condition:** Deliver the scoped evidence-linked report with unresolved gaps stated; do not expand into rerunning pipelines.

**Evidence:**

- [skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md:34](../../skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md#L34) — `not proof of the results`: Distinguishes index claims from result evidence.
- [skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md:61](../../skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md#L61) — `do not turn the reference into a mandatory checklist`: Prevents optional analysis lenses becoming gates.

<a id="skill-pydeseq2"></a>

### 104. pydeseq2 — P1

Source: [skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md](../../skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md) · version `1.0.0`.

**Retain:** Fit replicate-aware bulk count models with aligned sample metadata, an estimable design and an explicit contrast.

**Findings:** The confounding remedy removes batch or adds an interaction even when condition and batch cannot be separated; neither recovers an identifiable condition effect. The transpose heuristic cannot diagnose all-zero counts and risks changing sample identity. Repeated examples omit key alignment/design checks; sparse AnnData and versioned storage APIs need testing.

**Keep / condense / move / delete:** Keep count/sample/contrast and replication invariants; replace confounding advice with an estimability explanation and bounded alternatives. Remove shape-based guessing, consolidate recipes, and delete promotional routing unrelated to the task.

**Trigger boundary:** Bulk RNA-seq PyDESeq2 or replicate-level pseudobulk testing; do not imply cell-level independent replication.

**Acceptance force:** An estimable design and correct sample alignment are data-integrity prerequisites; extra plots or obtaining significance are not acceptance gates.

**Evidence:**

- [skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md:472](../../skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md#L472) — `Remove confounded variable or add interaction term`: Cannot identify an effect completely confounded with batch.
- [skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md:462](../../skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md#L462) — `if counts_df.shape[1] < counts_df.shape[0]:`: Dimensions alone do not establish matrix orientation.

<a id="skill-cellxgene-census"></a>

### 105. cellxgene-census — P1

Source: [skills-market/compbio/single-cell/visualization/cellxgene-census/SKILL.md](../../skills-market/compbio/single-cell/visualization/cellxgene-census/SKILL.md) · version `1.0.0`.

**Retain:** Query a named Census release with correct cell/gene identities, primary-data deduplication and measurement-presence handling.

**Findings:** The streaming mean divides by the number of stored sparse values, excluding implicit zeros; it therefore estimates a nonzero-entry mean rather than mean expression. A metadata example selects only cell_type and then groups by absent tissue_general. Experimental ML APIs and whole-cell random train/test splits need version and donor/dataset leakage checks.

**Keep / condense / move / delete:** Keep release pinning, is_primary_data and presence-matrix controls; correct sparse denominators and selected columns. Replace unstable ML examples with a versioned reference and donor-aware split rules; condense repeated query recipes and delete promotion.

**Trigger boundary:** Already excludes analysis of the user's own data; remove undated cell-count and largest-atlas superlatives from always-loaded metadata.

**Evidence:**

- [skills-market/compbio/single-cell/visualization/cellxgene-census/SKILL.md:189](../../skills-market/compbio/single-cell/visualization/cellxgene-census/SKILL.md#L189) — `n_observations += len(values)`: Counts stored sparse entries, not all cell-gene observations.
- [skills-market/compbio/single-cell/visualization/cellxgene-census/SKILL.md:100](../../skills-market/compbio/single-cell/visualization/cellxgene-census/SKILL.md#L100) — `cell_metadata.groupby("tissue_general")`: The preceding query selected only cell_type.

<a id="skill-metabolomics-workbench"></a>

### 106. metabolomics-workbench — P2

Source: [skills-market/compbio/multiomics/metabolomics/metabolomics-workbench/SKILL.md](../../skills-market/compbio/multiomics/metabolomics/metabolomics-workbench/SKILL.md) · version `1.0.0`.

**Retain:** Retrieve study and compound records with traceable identifiers, RefMet matching and explicit MS adduct/tolerance semantics.

**Findings:** The endpoint tour repeats a large bundled reference. Generic 0.5/0.01 Da tolerances are presented without instrument or mass dependence, and a structure download is described as confirmation even though mass matching and a structure depiction cannot establish compound identity. HTTP examples lack response checks and timeouts.

**Keep / condense / move / delete:** Keep source IDs, adduct/polarity and uncertainty rules; condense to a validated request pattern and conditional reference. Qualify mass-match candidates, make RefMet normalization task-dependent, remove undated catalog counts and unrelated promotion.

**Trigger boundary:** Metabolomics Workbench/RefMet querying, not a general guarantee of biomarker discovery or metabolite identification.

**Evidence:**

- [skills-market/compbio/multiomics/metabolomics/metabolomics-workbench/SKILL.md:199](../../skills-market/compbio/multiomics/metabolomics/metabolomics-workbench/SKILL.md#L199) — `Download structures for confirmation`: Structure retrieval does not confirm experimental identification.
- [skills-market/compbio/multiomics/metabolomics/metabolomics-workbench/SKILL.md:239](../../skills-market/compbio/multiomics/metabolomics/metabolomics-workbench/SKILL.md#L239) — `0.01 Da for high-resolution MS`: A universal absolute tolerance omits instrument and m/z context.

<a id="skill-uniprot"></a>

### 107. uniprot — P1

Source: [skills-market/compbio/multiomics/proteomics/uniprot/SKILL.md](../../skills-market/compbio/multiomics/proteomics/uniprot/SKILL.md) · version `1.0.0`.

**Retain:** Resolve protein identifiers and retrieve sequences/annotations while preserving taxonomy, isoforms, mapping multiplicity and unmapped IDs.

**Findings:** The bundled client returns only one search/mapping result page; batch_retrieve merely sets size to the input count, and map_ids polls forever without a deadline or explicit failed-job handling. Several reference paths begin /references rather than being skill-relative. The body is otherwise a useful but repetitive API index.

**Keep / condense / move / delete:** Keep ID/taxonomy/reviewed-status distinctions. Repair pagination and bounded job handling before claiming complete batch retrieval; fix relative links, condense endpoint catalogs, delete promotion and unsupported superlatives.

**Trigger boundary:** Direct UniProt REST or UniProt-specific control is already a useful boundary; avoid forcing bioservices when the requested interface differs.

**Evidence:**

- [skills-market/compbio/multiomics/proteomics/uniprot/SKILL.md:128](../../skills-market/compbio/multiomics/proteomics/uniprot/SKILL.md#L128) — `batch_retrieve(accessions, format)`: Completeness promise needs the client's pagination repair.
- [skills-market/compbio/multiomics/proteomics/uniprot/SKILL.md:87](../../skills-market/compbio/multiomics/proteomics/uniprot/SKILL.md#L87) — `/references/id_mapping_databases.md`: Leading slash conflicts with portable skill-relative resources.
- [skills-market/compbio/multiomics/proteomics/uniprot/scripts/uniprot_client.py:106](../../skills-market/compbio/multiomics/proteomics/uniprot/scripts/uniprot_client.py#L106) — `size=len(accessions)`: One-page request does not establish complete batch retrieval.
- [skills-market/compbio/multiomics/proteomics/uniprot/scripts/uniprot_client.py:180](../../skills-market/compbio/multiomics/proteomics/uniprot/scripts/uniprot_client.py#L180) — `while True:`: Mapping polling lacks a deadline and failed-job branch.

<a id="skill-kegg"></a>

### 108. kegg — P1

Source: [skills-market/compbio/databases/kegg/SKILL.md](../../skills-market/compbio/databases/kegg/SKILL.md) · version `1.0.0`.

**Retain:** Use KEGG operations with correct organism/identifier namespaces, operation-specific batch limits and provider access conditions.

**Findings:** The statement that no explicit rate limit exists conflicts with KEGG's published maximum of three API calls per second. A single ten-entry limit is also applied too broadly across different operations. Most of the body duplicates the API reference, while enrichment context omits background/mapping requirements.

**Keep / condense / move / delete:** Keep and source the provider access restriction; correct the rate limit and operation-specific limits. Condense the API tour, retain namespace and mapping-direction rules, and distinguish pathway membership retrieval from statistical enrichment.

**Trigger boundary:** Direct KEGG REST work; clinical drug-interaction decisions require a separate evidence and clinical context rather than this lookup recipe.

**Evidence:**

- [skills-market/compbio/databases/kegg/SKILL.md:351](../../skills-market/compbio/databases/kegg/SKILL.md#L351) — `No explicit limit`: Contradicts the provider's published three-calls-per-second restriction.
- [skills-market/compbio/databases/kegg/SKILL.md:348](../../skills-market/compbio/databases/kegg/SKILL.md#L348) — `Maximum 10 entries per operation`: Limits must be scoped to the actual operation.

Primary documentation checked: [KEGG API access and rate limit](https://www.kegg.jp/kegg/rest/).

<a id="skill-reactome"></a>

### 109. reactome — P2

Source: [skills-market/compbio/databases/reactome/SKILL.md](../../skills-market/compbio/databases/reactome/SKILL.md) · version `1.0.0`.

**Retain:** Query versioned pathway content or perform enrichment with explicit identifier mapping, species, background and multiple-testing interpretation.

**Findings:** The enrichment example prints only raw p-values and assumes a flat pathway response shape; service variants should be checked against a saved response. Input mapping losses, measured-gene background and redundancy are absent. Undated maintenance claims and current-statistics sections add drift without execution value.

**Keep / condense / move / delete:** Keep Content/Analysis service separation and ID/species semantics. Validate response parsing, report FDR and mapping coverage, make background selection explicit, move optional visualization/client variants to references and delete promotion/statistics catalogs.

**Trigger boundary:** Require Reactome pathway queries or analysis; do not activate solely for generic gene-expression analysis.

**Evidence:**

- [skills-market/compbio/databases/reactome/SKILL.md:143](../../skills-market/compbio/databases/reactome/SKILL.md#L143) — `pathway['stId']`: Response nesting needs a fixture or current schema check.
- [skills-market/compbio/databases/reactome/SKILL.md:143](../../skills-market/compbio/databases/reactome/SKILL.md#L143) — `p-value: {pathway['entities']['pValue']}`: Primary example omits FDR despite many pathway tests.

<a id="skill-geo"></a>

### 110. geo — P1

Source: [skills-market/compbio/databases/geo/SKILL.md](../../skills-market/compbio/databases/geo/SKILL.md) · version `1.0.0`.

**Retain:** Find and retrieve GEO records while preserving accession, platform/probe identity, processing state and sample design.

**Findings:** The manual expression assembly aligns samples by row number rather than probe ID. The Python FTP helper omits matrix/soft subdirectories that its own shell examples include. A generic t-test labels mean differences log2_fold_change without establishing log scale; the so-called meta-analysis only collects study means. Extensive repeated tutorial code distracts from provenance and design.

**Keep / condense / move / delete:** Keep GSE/GSM/GPL identity and processing-state checks. Fix feature alignment and download paths; route differential expression to an appropriate design-aware method. Relabel descriptive cross-study summaries, condense the tutorial and move validated download variants to references.

**Trigger boundary:** GEO search/retrieval and dataset interpretation, not arbitrary transcriptomics or a default statistical analysis workflow.

**Evidence:**

- [skills-market/compbio/databases/geo/SKILL.md:196](../../skills-market/compbio/databases/geo/SKILL.md#L196) — `expression_data[gsm_name] = gsm.table['VALUE']`: Positional index alignment can silently mix probes across samples.
- [skills-market/compbio/databases/geo/SKILL.md:480](../../skills-market/compbio/databases/geo/SKILL.md#L480) — `'log2_fold_change': fold_change`: The example never establishes that values are log2 expression.
- [skills-market/compbio/databases/geo/SKILL.md:380](../../skills-market/compbio/databases/geo/SKILL.md#L380) — `ftp.cwd(ftp_path)`: Helper uses series root rather than the required file-type subdirectory.

<a id="skill-ensembl"></a>

### 111. ensembl — P2

Source: [skills-market/compbio/databases/ensembl/SKILL.md](../../skills-market/compbio/databases/ensembl/SKILL.md) · version `1.0.0`.

**Retain:** Resolve genome annotation and sequence requests with explicit species, assembly, coordinate convention, strand and stable-ID version.

**Findings:** The skill lists many API categories but omits the coordinate convention and ambiguous symbol/one-to-many mapping rules that are easy to misuse. EnsemblClient/AssemblyMapper methods need checking against the named Python package; current release 115 is an undated assertion. The retry pattern has no request timeout.

**Keep / condense / move / delete:** Keep assembly/host selection and Retry-After handling. Add coordinate/strand/ID contracts, verify one direct REST example and the optional client's real API, then condense catalogs and delete stale release counts and promotion.

**Trigger boundary:** Explicit Ensembl annotation, sequence, homology or VEP work; distinguish predicted variant consequence from clinical pathogenicity.

**Evidence:**

- [skills-market/compbio/databases/ensembl/SKILL.md:15](../../skills-market/compbio/databases/ensembl/SKILL.md#L15) — `Current release is 115`: Replace drifting current-version claim with runtime release discovery.
- [skills-market/compbio/databases/ensembl/SKILL.md:178](../../skills-market/compbio/databases/ensembl/SKILL.md#L178) — `from ensembl_rest import AssemblyMapper`: Optional package API needs verification before reuse.

## Validation and remaining work

- Registry validation: passed, including required three-component version strings; eight warnings only report first-time registrations without historical paths.
- Skill documentation validation: passed, including frontmatter/registry version equality.
- Deployment/taskpack validation: passed.
- Focused version checks: malformed values, missing metadata and mismatched copies were rejected; existing versions were preserved.
- All 111 individual audit records have an active registry target and evidence locators. Non-skill files under `skills-market/` still match the pre-audit snapshot.
- A scan of Markdown relative links found no confirmed missing link: the only unresolved candidate was the illustrative literal `[text](url)` in obsidian-markdown. Plain-text references require separate inspection; PDF uppercase filenames and latex-writing's missing preamble are recorded individually.
- Marketplace plugin-root resolution: **failed for 111/111 references**, recorded above. This is distinct from registry/version validation.
- Full examples, external-service workflows, model training and all resource files were not exhaustively executed. The report does not certify runtime compatibility.

Apply repairs one skill at a time, beginning with the marketplace path calculation and persistent/unrelated write hazards. For each skill, preserve its stated behavioral core, verify the implicated API or example, make only justified cuts, update its two version fields, and run the smallest relevant checks. Keep any unresolved scientific or API question visible. Archive a skill only by an explicit retirement decision, preserving its recovery metadata.
