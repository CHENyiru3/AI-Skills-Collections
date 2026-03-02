---
name: explain-bio-dl-model
description: Translates complex deep learning architectures (VQ-VAE, Transformers, Neural ODEs) into standard biological manuscript text, focusing on the biological rationale for the architecture.
---

# Deep Learning Architecture Explainer

Translate the model architecture details provided in $ARGUMENTS into a manuscript-ready text block suitable for a journal like *Nature Computational Science* or *Bioinformatics*.

Follow this specific mapping framework:
1. **The Biological Problem:** Start by defining the biological constraint the model overcomes (e.g., noisy single-cell dropout, missing spatial z-axis resolution, high-dimensional perturbation spaces).
2. **The Architecture Rationale:** Explain *why* the specific architecture was chosen for this biological data.
   * *Example:* "A Vector Quantized-Variational Autoencoder (VQ-VAE) was implemented to force the highly variable gene expression profiles into a discrete latent space, effectively isolating distinct cellular states from continuous technical noise."
3. **Data Flow:** Describe the journey of the data from the input biological matrix, through the embedding layers, to the final biological prediction (e.g., predicting spatial perturbation responses).
4. **Validation:** End by stating how the model's embeddings are biologically validated (e.g., comparing generated gene embeddings against established Hallmark pathways).
