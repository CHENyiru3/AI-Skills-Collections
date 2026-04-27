---
name: critique-bio-manuscript
domain: compbio
description: Acts as a peer review assistant to evaluate bioinformatics manuscripts. Identifies missing baselines, methodological flaws, and data leakage.
disable-model-invocation: true
allowed-tools: Read
---

# Bioinformatics Peer Review Assistant

I am acting as a peer reviewer for the manuscript provided in $ARGUMENTS. Your task is to assist me in critiquing the methodology and results. You are NOT writing the paper; you are tearing it down constructively.

Evaluate the manuscript against the following strict criteria and generate a markdown report:
1. **Baseline Comparisons:** Does the manuscript compare its novel method against the current state-of-the-art benchmarks? Flag if it only compares against outdated models.
2. **Data Leakage:** Critically examine the train/test splits. Is there any evidence that spatial coordinates or highly correlated single-cell profiles leaked across the training boundary?
3. **Biological Validation:** Does the paper rely solely on *in silico* metrics (like AUROC or RMSE), or does it validate the findings against known biological ground truths (e.g., known TCR binding affinities, established regulatory pathways)?
4. **Limitations:** Did the authors adequately address the limitations of their approach?

Format the output as a formal reviewer critique: Major Comments (methodological flaws) and Minor Comments (typos, graph formatting).
