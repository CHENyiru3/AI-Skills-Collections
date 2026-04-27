---
name: nextflow
domain: compbio
description: Workflow management for computational biology. Use for creating portable and reproducible pipelines with excellent support for cloud and HPC environments.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Nextflow: Workflow Management

## Overview

Nextflow is a powerful workflow management system designed for computational biology and bioinformatics. It enables the creation of portable, reproducible pipelines that can run on local machines, HPC clusters, and cloud platforms.

## When to Use This Skill

This skill should be used when:
- Creating scalable bioinformatics pipelines
- Running workflows on HPC or cloud
- Building nf-core pipelines
- Ensuring reproducibility
- Managing containerized workflows

## Quick Start

### Installation

```bash
# Using conda
conda install -c bioconda nextflow

# Direct download
curl -s https://get.nextflow.io | bash

# Or using sdkman
sdk install nextflow
```

### Basic Pipeline

```groovy
// main.nf
process SAYHELLO {
    input:
        val x

    output:
        stdout

    script:
    """
    echo "Hello $x!"
    """
}

workflow {
    Channel.from('World', 'Nextflow', 'Pipeline') \
        | SAYHELLO \
        | view
}
```

## Single-Cell Example

### Basic scRNA-seq Pipeline

```groovy
// main.nf
paramsreads = "data/reads/*_{1,2}.fastq.gz"
paramsgenome = "genome.fa"
paramsindex = "genome.index"

process FASTQC {
    input:
    path reads

    output:
    path "fastqc_reports"

    script:
    """
    mkdir -p fastqc_reports
    fastqc $reads -o fastqc_reports
    """
}

process ALIGN {
    input:
    path reads
    path index

    output:
    path "aligned.bam"

    script:
    """
    hisat2 -x $index -1 ${reads[0]} -2 ${reads[1]} -S aligned.sam
    samtools view -b aligned.sam > aligned.bam
    """
}

process COUNT {
    input:
    path bam
    path gtf

    output:
    path "counts.txt"

    script:
    """
    featureCounts -a $gtf -o counts.txt $bam
    """
}

workflow {
    reads = Channel.fromFilePairs(paramsreads)
    FASTQC(reads)
    ALIGN(reads, paramsindex)
    COUNT(ALIGN.out, params.gtf)
}
```

## Running Nextflow

### Execution Modes

```bash
# Local
nextflow run main.nf

# Docker
nextflow run main.nf -dockerize

# Singularity
nextflow run main.nf -with-singularity

# Conda
nextflow run main.nf -with-conda
```

### HPC Configuration

```bash
# SLURM
nextflow run main.nf -profile slurm

# PBS/Torque
nextflow run main.nf -profile pbs

# LSF
nextflow run main.nf -profile lsf
```

### Cloud

```bash
# AWS Batch
nextflow run main.nf -profile awsbatch

# Google Cloud
nextflow run main.nf -profile google
```

## Key Concepts

### Processes

```groovy
process PROCESS_NAME {
    input:
        type input_data
        val value_data

    output:
        type output_data

    script:
        """
        your_command $input_data $value_data > output_data
        """
}
```

### Channels

```groovy
// From files
Channel.fromFilePairs('data/*_{1,2}.fastq.gz')

// From list
Channel.from('a', 'b', 'c')

// From path
Channel.fromPath('data/*.txt')
```

### Operators

```groovy
// Map
Channel.from(1,2,3) | map { it * 2 }

// Filter
Channel.from(1,2,3,4,5) | filter { it > 2 }

// FlatMap
Channel.from([1,2], [3,4]) | flatMap { it }

// Combine
ch1 = Channel.from(1,2)
ch2 = Channel.from('a','b')
ch1 | combine(ch2) | view
```

### Config Files

```groovy
// nextflow.config
process {
    executor = 'slurm'
    queue = 'general'
    time = '1h'
    memory = '4 GB'
}

docker {
    enabled = true
}
```

## nf-core

### Using nf-core Pipelines

```bash
# List available pipelines
nextflow pull nf-core/rnaseq

# Run pipeline
nextflow run nf-core/rnaseq -profile docker --reads '*_{1,2}.fastq.gz'
```

### Key nf-core Pipelines

- **rnaseq**: RNA-seq analysis
- **atacseq**: ATAC-seq analysis
- **scrnaseq**: Single-cell RNA-seq
- **methylseq**: Bisulfite sequencing

## Best Practices

1. **Use nf-core**: Leverage community pipelines
2. **Containerize**: Use Docker/Singularity
3. **Version control**: Keep in git
4. **Test**: Use CI/CD for testing

## Additional Resources

- **Documentation**: https://www.nextflow.io/docs/latest/
- **nf-core**: https://nf-co.re/
- **Tutorial**: https://www.nextflow.io/docs/latest/getstarted.html
