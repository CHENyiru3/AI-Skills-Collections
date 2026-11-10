---
name: metabolomics-workbench-database
domain: compbio
description: Find and retrieve Metabolomics Workbench studies, analysis metadata, measurements, RefMet names, or candidate compounds through its documented API. Use for source-backed metabolomics data access and annotation.
license: Unknown
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# Metabolomics Workbench

Define the requested study/analysis, organism/sample context, measurement type, identifier, and output. Inspect current API documentation and response schema rather than relying on fixed study counts or endpoint guesses.

## Retrieve the evidence

- Select the appropriate study, compound, RefMet, mass-search, or other documented context. URL-encode names and special characters; use HTTPS, timeouts, HTTP-status checks, and content-type/schema checks before parsing or saving.
- Distinguish study-level metadata from analysis-level measurements, experimental factors, raw data, and processed/mwTab files. Keep study/analysis/sample identifiers and processing provenance together.
- Inspect units, scaling/normalization, missingness, platform, polarity, chromatography, sample groups, and biological replication before comparing measurements. An API table is not automatically analysis-ready.
- Use RefMet matching when name harmonization is needed. Preserve original names and mapping ambiguity, structural resolution, synonyms, and unmapped entries; do not replace uncertain identities with the first match.

## Mass searches and identification

Specify measured m/z, charge/polarity, adduct, isotope assumptions, tolerance units, and instrument/calibration evidence. Choose ppm or absolute tolerance from the real method rather than a universal high-/low-resolution cutoff.

A mass/formula match produces candidates, not confirmed metabolite identity. A downloaded structure image illustrates a candidate; it does not validate an experimental peak. Distinguish candidate matching from support based on MS/MS, retention behavior, standards, and the identification confidence actually available.

Cross-database identifiers can encode different structures, stereochemistry, salts, or resolution levels. Record those distinctions and conflicting matches explicitly. Do not infer a biomarker, mechanism, or disease effect from database association alone.

## Verify and deliver

Bound queries/downloads to the requested selection and report paging/truncation, empty responses, unavailable files, and partial results. Cache reusable reference responses with request/date/version metadata where practical.

Save an inventory of source IDs/URLs, query parameters, metadata, units, processing, annotation confidence, and excluded/unmapped records. Verify selected returned values against the source and check that files are the promised format.

Use [API notes](references/api_reference.md) selectively and verify exact endpoints against the [official Workbench tools](https://www.metabolomicsworkbench.org/tools/). Do not download an entire reference database or launch a disease analysis merely to resolve one compound.
