---
name: geo-database
domain: compbio
description: Search, select, download, or curate NCBI GEO series/sample/platform data and metadata, including SOFT/series matrices/supplementary files, probe alignment, and study-design provenance.
license: Unknown
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# NCBI GEO data access

Define organism, assay/platform, biological question, sample/replicate criteria, raw versus processed requirement, and download scope. Distinguish GSE series, GSM samples, GPL platforms, curated GDS records, and linked sequencing archives; a GSM is not always one independent biological replicate.

## Discover and select

Use the portal or documented E-utilities/GEOparse route. Preserve exact query, accessions, publication/design, processing metadata, retrieval date, and inclusion/exclusion decisions. Handle search pagination; a limited `IdList` is not the total matching inventory.

Inspect actual sample characteristics and donor/pairing/batch variables rather than assigning groups by title substrings alone. Multi-platform series and superseries can contain overlapping or incomparable samples.

## Retrieve and align

- Choose the actual file listing: series matrix, SOFT, MINiML, supplementary data, or linked raw reads. Files live in type-specific subdirectories; series matrices can have platform-specific filenames or be absent.
- Use source-provided URLs/manifest, bounded timeouts/retries, download-size checks and atomic/verified writes where appropriate. Do not recursively retrieve an entire archive for one study.
- For expression extraction, join sample values by probe/feature ID, not row number. Check duplicates, platform annotations, missing features and one-to-many gene mappings before creating a matrix.
- Determine whether values are counts, raw intensities, normalized or log-transformed from processing provenance and diagnostic values. A simple maximum-value heuristic cannot prove the scale.
- Keep metadata/sample IDs aligned and record transformations. Do not call the difference of means `log2FoldChange` unless the modeled scale and contrast support that interpretation.

## Analysis boundaries

Choose assay-appropriate statistics and independent biological replicates, including paired/covariate structure and multiple testing. Use counts for count models and appropriate intensity/log-expression models for arrays. Descriptive study/probe means are not a formal meta-analysis; combine comparable effect estimates and uncertainty only under an explicit design.

Follow current [NCBI programmatic-access guidance](https://www.ncbi.nlm.nih.gov/books/NBK25501/) and per-request pacing, including searches plus summaries. Public download access does not imply unlimited request rate. Keep credentials out of logs and cache requested data deliberately.

## Verify and deliver

Check file integrity/format, source accession/platform, probe/sample mapping, selected values, missingness, processing and design. Report actual downloaded/inspected files, metadata gaps, exclusions and partial failures; do not claim reanalysis from a download or summary alone.

Use [GEO download documentation](https://www.ncbi.nlm.nih.gov/geo/info/download.html), [GEOparse documentation](https://geoparse.readthedocs.io/), and [local reference](references/geo_reference.md) for the selected operation. Avoid stale inventory counts and generic complete-analysis claims.
