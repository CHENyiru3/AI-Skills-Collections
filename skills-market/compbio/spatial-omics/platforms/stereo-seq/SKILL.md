---
name: stereo-seq
domain: compbio
description: Analyze or convert Stereo-seq GEM/GEF, square-bin, or cell-bin spatial transcriptomics data while preserving bin/cell identity, coordinates, and count semantics.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Stereo-seq

Inspect the upstream processing version, organism/reference, file format, sample identity, bin mode/size, coordinate units, and segmentation/image metadata. Select the analysis path from the actual data rather than treating every export as a generic CSV.

## Import and alignment

- For native formats use a supported reader from the installed Stereopy or platform workflow. Confirm whether rows represent DNBs, square bins, segmented cells, or aggregated regions.
- Preserve original counts and feature IDs. AnnData convention is observations by features; Seurat count matrices are features by cells. Check orientation from identifiers and metadata, not dimensions alone.
- Join coordinates and metadata by stable bin/cell identifiers, assert uniqueness and coverage, then reorder to the expression observations. Never assign coordinates by `.values` or overwrite row names to disguise a mismatch.
- Preserve x/y order, origin, axis direction, physical scale, binning offset, and sample-specific frame. Do not convert a bin number to microns without the platform's scale metadata.

## Analyze at the selected resolution

Choose bin size or cell segmentation for the biological question and count depth. Record aggregation rules, edge bins, empty regions, tissue masking, and segmentation uncertainty. Changing bin size changes observation identity and must propagate to coordinates, counts, and metadata.

Assess depth, detected features, background, mitochondrial metrics, segmentation quality, and tissue coverage per sample before selecting thresholds. Preserve a count layer before normalization. Apply expression normalization/HVG/PCA/graph methods with explicit assumptions; UMAP is not a tissue coordinate map.

Build spatial neighborhoods within sample boundaries using a documented distance or adjacency rule. Evaluate spatial statistics with appropriate nulls, multiple-testing control, and biological replication; adjacent bins are not independent biological replicates.

## Verify and save

Inspect expression-coordinate ID alignment and plot counts/annotations over the tissue image. Preserve sparse structures when possible and estimate memory before materializing high-resolution matrices. Save count/processed-layer meanings, bin mode/size, IDs, transforms, reference, sample metadata, and software versions with the output.

Use [Stereopy documentation](https://stereopy.readthedocs.io/en/latest/) for current GEM/GEF readers, square-bin/cell-bin workflows, and format conversion.
