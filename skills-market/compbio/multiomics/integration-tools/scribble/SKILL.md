---
name: scribble
domain: compbio
description: Investigate or maintain a user-identified Scribble bioinformatics package after its authoritative repository and API are supplied or found. This entry has an unverified tool identity; do not use it to select a generic multi-omics integration method.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Scribble: verify package identity first

The previous entry supplied a placeholder repository (`username/scribble`) and an unsupported `scribble.integrate` API. Those examples do not establish a real single-cell multi-omics package. This entry remains in the active catalog for explicit follow-up; it is not a validated integration recipe.

## Identification gate

1. Obtain the intended paper/DOI, authoritative repository, package source, or a project dependency lock identifying the tool.
2. Match package name, authors, purpose, installation source, supported versions, and API examples. A similarly named PyPI package is not sufficient evidence.
3. If identity remains unresolved, report that fact and stop the package-specific installation/analysis. Do not install `scribble` by name, invent CCA/MNN/WNN support, or silently substitute SCRABBLE or another method.

## After identification

Read the primary documentation and inspect the project's inputs. Establish paired versus unpaired observations, per-modality preprocessing, feature identities, supported missingness, batch labels, and expected output representation. Align modalities by stable cell IDs where pairing is required; do not assume row order implies pairing.

Validate a documented small example, finite outputs, observation coverage, batch effects, and preservation of biological structure before applying the method to real data. Record the exact source/revision and assumptions. Replace this identification-only entry with a verified workflow and advance its version when the intended tool is established.
