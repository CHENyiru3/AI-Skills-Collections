---
name: signac
domain: compbio
description: Implement or debug Signac ChromatinAssay workflows for scATAC-seq QC, TF-IDF/LSI, accessibility, gene activity, fragments, genomic annotations, and Seurat multimodal integration.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Signac chromatin analysis

Inspect Signac/Seurat versions, peak-by-cell counts, fragment file/index, barcode mapping, genome assembly and annotations. Preserve the selected assay and coordinate conventions.

## Build and preprocess

- Construct a supported `ChromatinAssay` with peaks/counts, fragment mapping, and compatible genomic ranges, then place it in a Seurat object.
- Match annotation assembly, chromosome names, coordinate conventions, and gene identifiers to fragments/peaks. Check fragment barcode coverage and selected cells explicitly.
- Assess TSS enrichment, nucleosome signal, fragments/reads in peaks, blacklist metrics, and doublets per sample. Choose thresholds from data and assay context.
- Use supported TF-IDF, feature-selection, and `RunSVD` operations for LSI. Inspect component/depth correlation before choosing dimensions; do not always discard component 1 without evidence. Use that named reduction for neighbors, clustering and UMAP.

## Gene activity and integration

`GeneActivity` returns a matrix, not a replacement Seurat object. For an existing compatible object, a typical pattern is:

```r
activity <- GeneActivity(pbmc)
pbmc[["ACTIVITY"]] <- CreateAssayObject(counts = activity)
pbmc <- NormalizeData(pbmc, assay = "ACTIVITY")
```

Check barcode/feature alignment before assignment. Gene activity is an accessibility-derived proxy and should retain that meaning rather than being labeled measured RNA.

For paired multiome data, verify shared cell IDs and use an appropriate multimodal/WNN workflow with separately processed RNA and ATAC representations. For an unpaired RNA reference, use supported transfer/mapping procedures and assess uncertainty. Do not integrate unlike RNA-gene and ATAC-peak matrices as if their features were equivalent.

## Testing and interpretation

For differential accessibility, account for depth and biological replication with a design appropriate to the claim. Cell-level cluster markers are exploratory; condition inference needs donor/sample-aware analysis. Use matched backgrounds for motif/enrichment questions.

Inspect coverage tracks and genomic ranges on the intended genome, selected reduction/assay, cell labels, and metadata. Save the Seurat object with versions and keep fragment/index dependencies accessible. Verify reopen and selected signal values; a saved object may still reference external files.

Use the [official Signac vignette](https://stuartlab.org/signac/articles/pbmc_vignette) and installed function help for exact APIs and Seurat-version compatibility.
