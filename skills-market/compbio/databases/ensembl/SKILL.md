---
name: ensembl-database
domain: compbio
description: Query Ensembl REST for genes/transcripts/proteins, sequences, variants/VEP, homology, regions or assembly mappings, preserving species, release, coordinate/strand, identifier-version and evidence contracts.
license: Unknown
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# Ensembl REST

Establish species, assembly, Ensembl release/server, gene/transcript/protein ID and version, coordinate convention, strand, requested operation and output. Query available species/assembly information rather than hardcoding a current release or species count.

## Identity and coordinates

- Distinguish gene, transcript, protein, symbol, stable ID, and version suffix. Resolve ambiguous symbols and retain original identifiers and mapping evidence.
- Ensembl region coordinates are generally 1-based inclusive; BED uses 0-based half-open intervals. Convert explicitly with source/target conventions and inspect strand/orientation. Never assume chromosome aliases or assemblies are interchangeable.
- Choose the appropriate current/archived or GRCh37 endpoint for the data and operation. Record assembly/release for every genomic interval and variant.
- Sequence type (genomic/cDNA/CDS/protein), transcript selection, strand, and flanking regions must match the question. Verify returned length/header/ID; a gene's genomic sequence is not automatically its coding sequence.

## Operations

Use documented lookup, sequence, overlap, variation/VEP, homology or assembly-map REST endpoints. Check current third-party client signatures if using a wrapper; do not invent `EnsemblClient`/`AssemblyMapper` methods from API names.

For variants, validate reference allele, assembly, transcript/HGVS version and representation before consequence interpretation. VEP predicts consequences; it does not by itself establish pathogenicity or a clinical action. For homology, report orthology type/confidence and one-to-many relationships rather than treating the first hit as a unique equivalent.

Assembly mapping can split intervals, change strand, or return unmapped portions. Preserve all mappings and coverage; do not report a successful single-coordinate lift from an incomplete interval response.

## Requests and verification

Use HTTPS, encoded paths/parameters, finite request timeouts, bounded retries, rate-limit headers and `Retry-After`. Distinguish no match, invalid request, rate limit, timeout, partial batch and service failure; do not retry malformed IDs indefinitely.

The [helper](scripts/ensembl_query.py) wraps selected direct REST operations; inspect its supported formats/options. Consult [endpoint notes](references/api_endpoints.md) selectively and check signatures against [official Ensembl REST documentation](https://rest.ensembl.org/documentation).

Record request/server/release, species/assembly/coordinate system, original/resolved IDs, output format and ambiguity. Verify selected response values and interval/sequence consistency. Do not silently drop ID versions, change genome build, or extrapolate beyond the returned evidence.
