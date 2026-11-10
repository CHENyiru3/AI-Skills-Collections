---
name: harmony
domain: compbio
description: Configure, tune, or assess Harmony correction of single-cell low-dimensional representations, including supported Seurat or Python integrations and preservation of biological structure.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Harmony integration

Inspect the actual implementation/version, input reduction, cell IDs, batch/covariate metadata, and biological comparison. R Harmony and Python integrations have distinct wrappers/signatures; use matching documentation.

## Input and output contract

- Start from a justified normalized feature space and PCA or supported representation. Verify batch metadata exists and is aligned; merge prefixes do not automatically create a `batch` column.
- Select technical variables deliberately. Do not correct away condition, cell type, donor, or other biological structure merely because a column is available. Complete batch-condition confounding cannot be solved by integration.
- Run the supported Harmony interface and preserve a named corrected reduction. Use it explicitly for neighbors/UMAP/clustering; Harmony ordinarily corrects embeddings, not the original RNA count matrix.
- Use the appropriate original expression/count representation and replicate-aware design for markers/condition DE. An integrated reduction does not create batch-corrected expression measurements.

## Tune with evidence

`theta` controls the diversity penalty; stronger penalties favor greater batch diversity in clusters. For the documented ridge parameter `lambda`, smaller values make correction more aggressive; larger regularization can reduce overcorrection. Do not recommend decreasing lambda to restore lost biological structure. Some releases support automatic lambda selection; inspect that version's behavior before overriding it.

Inspect convergence, neighborhood/cluster composition, unmatched populations, and representative markers. Compare with unintegrated data and assess both technical mixing and biological preservation. More mixing or more iterations is not automatically better, especially with unequal cell-type composition.

Use real supported reference options only when needed; do not invent `reference="batch1"` or combine independent integration methods without explaining the input/output contract and testing the result.

## Verify and save

Check corrected embedding shape, finite values, observation order, selected dimensions, and downstream graph ownership. Save parameters, variables corrected, original/corrected reductions, versions, and assessment results. Report unresolved confounding and missing population overlap.

Consult [RunHarmony reference](https://portals.broadinstitute.org/harmony/reference/RunHarmony.html) and the [authoritative repository](https://github.com/immunogenomics/harmony) for version-specific wrappers and parameter semantics.
