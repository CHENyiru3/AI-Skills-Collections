---
name: snakemake
domain: compbio
description: Workflow management system for bioinformatics. Use for creating reproducible and scalable computational biology pipelines.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Snakemake: Workflow Management

## Overview

Snakemake is a workflow management system that allows you to create reproducible and scalable data analysis pipelines. It is widely used in bioinformatics for automating computational biology workflows.

## When to Use This Skill

This skill should be used when:
- Creating automated analysis pipelines
- Ensuring reproducibility
- Scaling workflows to clusters/cloud
- Managing complex dependencies
- Building single-cell analysis pipelines

## Quick Start

### Installation

```bash
# Using conda
conda install -c conda-forge snakemake

# Using pip
pip install snakemake
```

### Basic Workflow

```python
# snakefile
rule all:
    input:
        "results/aligned.bam"

rule align:
    input:
        "data/sample.fastq"
    output:
        "results/aligned.bam"
    shell:
        "bwa mem {input} > {output}"
```

## Single-Cell Example

### Complete scRNA-seq Pipeline

```python
# snakefile
configfile: "config.yaml"

rule all:
    input:
        expand("results/{sample}/qc_report.html", sample=config["samples"])

rule qc:
    input:
        "data/{sample}.fastq.gz"
    output:
        html="results/{sample}/qc_report.html",
        json="results/{sample}/qc_metrics.json"
    shell:
        """
        fastqc {input} -o results/{wildcards.sample}/
        multiqc results/{wildcards.sample}/ -o {output.html}
        """

rule trimming:
    input:
        "data/{sample}.fastq.gz"
    output:
        "results/{sample}/trimmed.fastq.gz"
    shell:
        "trim_galore {input} -o results/{wildcards.sample}/"

rule alignment:
    input:
        "results/{sample}/trimmed.fastq.gz"
    output:
        "results/{sample}/aligned.bam"
    shell:
        "star --genomeDir {config[genome]} --readFilesIn {input} --outFileNamePrefix results/{wildcards.sample}/"

rule count:
    input:
        "results/{sample}/aligned.bam"
    output:
        "results/{sample}/counts.txt"
    shell:
        "featureCounts -a {config[gtf]} -o {output} {input}"
```

## Running Snakemake

### Local Execution

```bash
# Dry run
snakemake -n

# Run with visualization
snakemake --dag | dot -Tpdf dag.pdf
```

### Cluster Execution

```bash
# SLURM
snakemake --profile slurm

# PBS
snakemake --profile pbs

# SGE
snakemake --profile sge
```

### Cloud Execution

```bash
# Google Life Sciences
snakemake --google-lifesciences

# AWS
snakemake --default-remote-provider S3 --default-remote-prefix my-bucket
```

## Key Concepts

### Rules

```python
rule my_rule:
    input:
        file1="data/input1.txt",
        file2="data/input2.txt"
    output:
        "results/output.txt"
    params:
        extra="--option value"
    shell:
        "command {input.file1} {input.file2} {params.extra} > {output}"
```

### Wildcards

```python
# Using wildcards
rule everything:
    input:
        "data/{sample}.txt"
    output:
        "results/{sample}_processed.txt"
    shell:
        "process {input} > {output}"
```

### Resources

```python
rule:
    input: ...
    output: ...
    resources:
        mem_mb=8000,
        runtime=120
```

### Containers

```python
rule:
    input: ...
    output: ...
    container:
        "docker://myimage:latest"
    shell: ...
```

## Advanced Features

### Grouping

```python
rule align:
    group: "alignment"
    ...

rule sort:
    group: "alignment"
    ...
```

### Subworkflows

```python
subworkflow other_workflow:
    workdir: "../other-project"
    snakefile: "Snakefile"
```

## Best Practices

1. **Use config files**: Separate configuration from logic
2. **Version control**: Keep workflows in git
3. **Test locally**: Verify before cluster execution
4. **Use containers**: Ensure reproducibility
5. **Document**: Add comments and README

## Additional Resources

- **Documentation**: https://snakemake.readthedocs.io/
- **Tutorial**: https://snakemake-tutorial.readthedocs.io/
- **GitHub**: https://github.com/snakemake/snakemake
