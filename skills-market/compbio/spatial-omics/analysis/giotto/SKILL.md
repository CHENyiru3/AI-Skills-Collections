---
name: giotto
domain: compbio
description: Import, analyze, or visualize spatial genomics data in an identified Giotto/Giotto Suite R workflow, including spatial networks, statistics, and multimodal objects.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Giotto spatial analysis

Identify the actual package family, version, object class, and installation source from the project. Giotto releases and Giotto Suite can have different object and API contracts; do not combine installation or function examples from them interchangeably.

## Workflow

1. Inspect the platform output or expression matrix, stable cell/feature IDs, spatial locations, image metadata, spatial unit, and feature type.
2. Use the matching version's supported reader/converter. For custom imports, confirm matrix orientation and align location IDs explicitly; passing a matrix directory and image directory to an arbitrary object constructor is not a verified platform import.
3. Inspect available expression values, spatial units, feature types, and reductions before preprocessing. Preserve counts and document which normalized matrix each analysis uses.
4. Construct spatial networks within sample boundaries using a justified radius, kNN, or adjacency definition. Inspect edge lengths, disconnected components, density, and coordinate units before spatial statistics.
5. Select an implemented statistic with a documented null/permutation scheme and multiple-testing correction. Check cell-type abundance and sampling effects; a spatial association is not proof of signaling or causal interaction.
6. For reference mapping/deconvolution, state reference compatibility, feature overlap, normalization, and uncertainty. Do not substitute an empty placeholder block for a working integration.
7. Plot representative regions over the image and verify axes, scale, cell IDs, annotations, and selected expression values. Save the object plus configurations and version information.

Use the project's [Giotto source/documentation](https://github.com/giotto-suite/Giotto) or its matching package repository. Inspect installed help before adopting version-specific function names. Verify output IDs and dimensions after conversion; do not assume Seurat/Giotto round-trips preserve every slot.
