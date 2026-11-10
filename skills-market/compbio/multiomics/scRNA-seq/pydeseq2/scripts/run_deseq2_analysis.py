#!/usr/bin/env python3
"""
PyDESeq2 Analysis Script

This script performs a complete differential expression analysis using PyDESeq2.
It can be used as a template for standard RNA-seq DEA workflows.

Usage:
    python run_deseq2_analysis.py --counts counts.csv --metadata metadata.csv \
           --design "~condition" --contrast condition treated control \
           --output results/

Requirements:
    - pydeseq2
    - pandas
    - matplotlib (optional, for plots)
"""

import argparse
import os
import pickle
import sys
from pathlib import Path



def load_and_validate_data(counts_path, metadata_path, transpose_counts=True):
    """Load count matrix and metadata, perform basic validation."""
    import csv
    import numpy as np
    import pandas as pd

    with open(counts_path, newline="") as handle:
        labels = next(csv.reader(handle))[1:]
    if not labels or len(labels) != len(set(labels)):
        raise ValueError("Count column identifiers must be present and unique")
    print(f"Loading count data from {counts_path}...")
    counts_df = pd.read_csv(counts_path, converters={0: str})
    counts_df = counts_df.set_index(counts_df.columns[0])

    if transpose_counts:
        print("Transposing count matrix to samples × genes format...")
        counts_df = counts_df.T

    print(f"Loading metadata from {metadata_path}...")
    metadata = pd.read_csv(metadata_path, converters={0: str})
    metadata = metadata.set_index(metadata.columns[0])

    print(f"\nData loaded:")
    print(f"  Counts shape: {counts_df.shape} (samples × genes)")
    print(f"  Metadata shape: {metadata.shape} (samples × variables)")

    if any(not str(value).strip() for value in counts_df.index) or any(not str(value).strip() for value in metadata.index):
        raise ValueError("Sample identifiers must not be empty")
    if counts_df.empty or metadata.empty:
        raise ValueError("Counts and metadata must be nonempty")
    if not counts_df.index.is_unique or not metadata.index.is_unique:
        raise ValueError("Sample identifiers must be unique")
    if not counts_df.columns.is_unique:
        raise ValueError("Gene identifiers must be unique")
    if set(counts_df.index) != set(metadata.index):
        raise ValueError("Count sample IDs must match metadata exactly; check --no-transpose and sample inclusion")
    metadata = metadata.loc[counts_df.index].copy()
    counts_df = counts_df.apply(pd.to_numeric, errors="raise")
    values = counts_df.to_numpy()
    if not np.isfinite(values).all() or (values < 0).any() or (values % 1 != 0).any():
        raise ValueError("Counts must be finite non-negative integers; normalized expression is not count input")
    if (values >= 2**63).any():
        raise ValueError("Counts exceed supported int64 range")
    counts_df = counts_df.astype("int64")

    return counts_df, metadata


def filter_data(counts_df, metadata, min_counts=10, condition_col=None):
    """Filter low-count genes and samples with missing data."""
    print(f"\nFiltering data...")

    initial_genes = counts_df.shape[1]
    initial_samples = counts_df.shape[0]

    # Filter genes
    genes_to_keep = counts_df.columns[counts_df.sum(axis=0) >= min_counts]
    counts_df = counts_df[genes_to_keep]
    genes_removed = initial_genes - counts_df.shape[1]
    print(f"  Removed {genes_removed} genes with < {min_counts} total counts")

    if condition_col:
        if condition_col not in metadata:
            raise ValueError(f"Missing contrast variable: {condition_col}")
        if metadata[condition_col].isna().any():
            raise ValueError("Missing contrast metadata; resolve and document sample exclusions before fitting")
    if counts_df.empty:
        raise ValueError("No genes remain after filtering")

    print(f"  Final data shape: {counts_df.shape[0]} samples × {counts_df.shape[1]} genes")

    return counts_df, metadata


def run_deseq2(counts_df, metadata, design, n_cpus=1):
    """Run DESeq2 normalization and fitting."""
    print(f"\nInitializing DeseqDataSet with design: {design}")

    from pydeseq2.dds import DeseqDataSet
    from pydeseq2.default_inference import DefaultInference

    dds = DeseqDataSet(
        counts=counts_df,
        metadata=metadata,
        design=design,
        refit_cooks=True,
        inference=DefaultInference(n_cpus=n_cpus),
        quiet=False
    )

    print("\nRunning DESeq2 pipeline...")
    print("  Step 1/7: Computing size factors...")
    print("  Step 2/7: Fitting genewise dispersions...")
    print("  Step 3/7: Fitting dispersion trend curve...")
    print("  Step 4/7: Computing dispersion priors...")
    print("  Step 5/7: Fitting MAP dispersions...")
    print("  Step 6/7: Fitting log fold changes...")
    print("  Step 7/7: Calculating Cook's distances...")

    dds.deseq2()

    print("\n✓ DESeq2 fitting complete")

    return dds


def run_statistical_tests(dds, contrast, alpha=0.05, shrink_lfc=False, shrink_coeff=None):
    """Perform Wald tests and compute p-values."""
    print(f"\nPerforming statistical tests...")
    print(f"  Contrast: {contrast}")
    print(f"  Significance threshold: {alpha}")

    from pydeseq2.ds import DeseqStats

    ds = DeseqStats(
        dds,
        contrast=contrast,
        alpha=alpha,
        cooks_filter=True,
        independent_filter=True,
        quiet=False
    )

    print("\n  Running Wald tests...")
    print("  Filtering outliers based on Cook's distance...")
    print("  Applying independent filtering...")
    print("  Adjusting p-values (Benjamini-Hochberg)...")

    ds.summary()

    print("\n✓ Statistical testing complete")

    # Optional LFC shrinkage
    if shrink_lfc:
        print("\nApplying LFC shrinkage for visualization...")
        if not shrink_coeff:
            raise ValueError("LFC shrinkage requires an explicit supported coefficient matching the contrast")
        ds.unshrunk_results = ds.results_df.copy()
        ds.lfc_shrink(coeff=shrink_coeff)
        print("✓ LFC shrinkage complete")

    return ds


def save_results(ds, dds, output_dir, shrink_lfc=False, alpha=0.05):
    """Save results and intermediate objects."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nSaving results to {output_dir}/")

    # Save statistical results
    results_path = output_dir / "deseq2_results.csv"
    ds.results_df.to_csv(results_path)
    print(f"  Saved: {results_path}")

    if shrink_lfc and hasattr(ds, "unshrunk_results"):
        ds.unshrunk_results.to_csv(output_dir / "deseq2_results_unshrunk.csv")

    # Save significant genes
    significant = ds.results_df[ds.results_df.padj < alpha]
    sig_path = output_dir / "significant_genes.csv"
    significant.to_csv(sig_path)
    print(f"  Saved: {sig_path} ({len(significant)} significant genes)")

    # Save sorted results
    sorted_results = ds.results_df.sort_values("padj")
    sorted_path = output_dir / "results_sorted_by_padj.csv"
    sorted_results.to_csv(sorted_path)
    print(f"  Saved: {sorted_path}")

    # Save DeseqDataSet as pickle
    dds_path = output_dir / "deseq_dataset.pkl"
    with open(dds_path, "wb") as f:
        pickle.dump(dds.to_picklable_anndata(), f)
    print(f"  Saved: {dds_path}")

    # Print summary
    print(f"\n{'='*60}")
    print("ANALYSIS SUMMARY")
    print(f"{'='*60}")
    print(f"Total genes tested: {len(ds.results_df)}")
    print(f"Significant genes (padj < {alpha:g}): {len(significant)}")
    print(f"Upregulated: {len(significant[significant.log2FoldChange > 0])}")
    print(f"Downregulated: {len(significant[significant.log2FoldChange < 0])}")
    print(f"{'='*60}")

    # Show top genes
    print("\nTop 10 most significant genes:")
    print(sorted_results.head(10)[["baseMean", "log2FoldChange", "pvalue", "padj"]])

    return results_path


def create_plots(ds, output_dir, alpha=0.05):
    """Create basic visualization plots."""
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("\nNote: matplotlib not installed. Skipping plot generation.")
        return

    output_dir = Path(output_dir)
    results = ds.results_df.copy()

    print("\nGenerating plots...")

    # Volcano plot
    results["-log10(padj)"] = -np.log10(results.padj.clip(lower=np.finfo(float).tiny))

    plt.figure(figsize=(10, 6))
    significant = results.padj < alpha
    plt.scatter(
        results.loc[~significant, "log2FoldChange"],
        results.loc[~significant, "-log10(padj)"],
        alpha=0.3, s=10, c='gray', label='Not significant'
    )
    plt.scatter(
        results.loc[significant, "log2FoldChange"],
        results.loc[significant, "-log10(padj)"],
        alpha=0.6, s=10, c='red', label=f'Significant (padj < {alpha:g})'
    )
    plt.axhline(-np.log10(alpha), color='blue', linestyle='--', linewidth=1, alpha=0.5)
    plt.axvline(1, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    plt.axvline(-1, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    plt.xlabel("Log2 Fold Change", fontsize=12)
    plt.ylabel("-Log10(Adjusted P-value)", fontsize=12)
    plt.title("Volcano Plot", fontsize=14, fontweight='bold')
    plt.legend()
    plt.tight_layout()
    volcano_path = output_dir / "volcano_plot.png"
    plt.savefig(volcano_path, dpi=300)
    plt.close()
    print(f"  Saved: {volcano_path}")

    # MA plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        np.log10(results.loc[~significant, "baseMean"] + 1),
        results.loc[~significant, "log2FoldChange"],
        alpha=0.3, s=10, c='gray', label='Not significant'
    )
    plt.scatter(
        np.log10(results.loc[significant, "baseMean"] + 1),
        results.loc[significant, "log2FoldChange"],
        alpha=0.6, s=10, c='red', label=f'Significant (padj < {alpha:g})'
    )
    plt.axhline(0, color='blue', linestyle='--', linewidth=1, alpha=0.5)
    plt.xlabel("Log10(Base Mean + 1)", fontsize=12)
    plt.ylabel("Log2 Fold Change", fontsize=12)
    plt.title("MA Plot", fontsize=14, fontweight='bold')
    plt.legend()
    plt.tight_layout()
    ma_path = output_dir / "ma_plot.png"
    plt.savefig(ma_path, dpi=300)
    plt.close()
    print(f"  Saved: {ma_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Run PyDESeq2 differential expression analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic analysis
  python run_deseq2_analysis.py \\
    --counts counts.csv \\
    --metadata metadata.csv \\
    --design "~condition" \\
    --contrast condition treated control \\
    --output results/

  # Multi-factor analysis
  python run_deseq2_analysis.py \\
    --counts counts.csv \\
    --metadata metadata.csv \\
    --design "~batch + condition" \\
    --contrast condition treated control \\
    --output results/ \\
    --n-cpus 4
        """
    )

    parser.add_argument("--counts", required=True, help="Path to count matrix CSV file")
    parser.add_argument("--metadata", required=True, help="Path to metadata CSV file")
    parser.add_argument("--design", required=True, help="Design formula (e.g., '~condition')")
    parser.add_argument("--contrast", nargs=3, required=True,
                       metavar=("VARIABLE", "TEST", "REFERENCE"),
                       help="Contrast specification: variable test_level reference_level")
    parser.add_argument("--output", default="results", help="Output directory (default: results)")
    parser.add_argument("--min-counts", type=int, default=10,
                       help="Minimum total counts for gene filtering (default: 10)")
    parser.add_argument("--alpha", type=float, default=0.05,
                       help="Significance threshold (default: 0.05)")
    parser.add_argument("--no-transpose", action="store_true",
                       help="Don't transpose count matrix (use if already samples × genes)")
    parser.add_argument("--no-shrink", action="store_true",
                       help="Skip LFC shrinkage")
    parser.add_argument("--n-cpus", type=int, default=1,
                       help="Number of CPUs for parallel processing (default: 1)")
    parser.add_argument("--plots", action="store_true",
                       help="Generate volcano and MA plots")

    parser.add_argument("--shrink-coeff", help="Opt in to LFC shrinkage for this exact supported coefficient; verify it matches the contrast")

    args = parser.parse_args()
    if not 0 < args.alpha < 1:
        parser.error("--alpha must be between 0 and 1")
    if args.min_counts < 0 or args.n_cpus < 1:
        parser.error("--min-counts must be nonnegative and --n-cpus positive")
    if args.no_shrink and args.shrink_coeff:
        parser.error("--no-shrink and --shrink-coeff cannot be combined")

    # Load data
    counts_df, metadata = load_and_validate_data(
        args.counts,
        args.metadata,
        transpose_counts=not args.no_transpose
    )

    # Filter data
    condition_col = args.contrast[0]
    counts_df, metadata = filter_data(
        counts_df,
        metadata,
        min_counts=args.min_counts,
        condition_col=condition_col
    )

    # Run DESeq2
    dds = run_deseq2(counts_df, metadata, args.design, n_cpus=args.n_cpus)

    # Statistical testing
    ds = run_statistical_tests(
        dds,
        contrast=args.contrast,
        alpha=args.alpha,
        shrink_lfc=bool(args.shrink_coeff),
        shrink_coeff=args.shrink_coeff
    )

    # Save results
    save_results(ds, dds, args.output, shrink_lfc=bool(args.shrink_coeff), alpha=args.alpha)

    # Create plots if requested
    if args.plots:
        create_plots(ds, args.output, alpha=args.alpha)

    print(f"\n✓ Analysis complete! Results saved to {args.output}/")


if __name__ == "__main__":
    main()
