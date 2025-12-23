---
title: Benchmarking Bioconda Packages for Arm64 in Bioinformatics Pipelines
description: This self-service project benchmarks Arm64 Bioconda packages in real nf-core workflows—measuring performance, diagnosing build failures, and proposing fixes that accelerate truly native bioinformatics on the expanding fleet of Arm-powered machines.
subjects:
- Performance and Architecture
- Databases
requires-team:
- No
platform:
- Servers and Cloud Computing
- Laptops and Desktops
sw-hw:
- Software
support-level:
- Self-Service
- Arm Ambassador Support
publication-date: 2025-05-30
license:
status:
- Published
donation:
layout: article
sidebar:
  nav: projects
full_description: |-
  ### Description

  **Why this is important?**

  Bioconda is a specialized package repository for bioinformatics and genomics. Since 2020, there has been notable growth in multi-core Arm-based laptops and desktops running Linux and MacOS. In the coming years, Arm anticipates an increase in available OEM (original equipment manufacturer) devices. These machines facilitate the execution of computationally intensive bioinformatics and statistics tasks locally. Potential downstream applications include faster, more affordable diagnoses that can be conducted closer to hospital patients, exemplified by the pilot [ROBIN software](https://www.nottingham.ac.uk/news/genetic-brain-tumour-diagnosis). While many leading Bioconda packages now support Linux/Arm, there still emulated components that can be the bottleneck. 

  **Project summary**

  This project aims to benchmark specific Bioconda packages that have been built for Arm64 using the nf-core-arm-discovery repository. The participant will utilize public genomic datasets from databases such as NCBI, select appropriate datasets, and execute bioinformatics workflows on Arm-based infrastructure. The candidate will evaluate the performance, compatibility, and efficiency of these packages, document errors and failures, and investigate the reasons behind package build failures. The final deliverable will be a detailed report with performance metrics, identified issues, and recommended improvements to enhance package support on Arm64.

  The deliverables of the project are as follows:

  - Selection and justification of public genomic datasets.
  - Execution of bioinformatics workflows using Bioconda packages on Arm64.
  - Performance benchmarking and comparison with x86 architectures.
  - Documentation of failed package builds and proposed fixes.
  - Comprehensive report with results, analysis, and recommendations.


  ## Prequisites

  - Intermediate understanding of Python, Bash and nextflow
  - Basic experience with nf-core pipelines, Conda, Docker/Singularity, Snakemake
  - Access to Arm64-based cloud instances (e.g., AWS Graviton) with plenty of memory and storage
  - IP access to Public genomic databases (NCBI, ENA, etc.)

  ## Resources from Arm and our partners

  - External Documentation: [nf-core documentation](https://nf-co.re/docs/)

  - External Documentation: [AWS Graviton documentation](https://aws.amazon.com/ec2/graviton/)

  - Repository: [Arm64 nf-core pipelines](https://github.com/ewels/nf-core-arm-discovery/tree/main)

  - Repository: [Bioconda package repository](https://bioconda.github.io/)

  - Dataset: [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/)


  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).


  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

### Description

**Why this is important?**

Bioconda is a specialized package repository for bioinformatics and genomics. Since 2020, there has been notable growth in multi-core Arm-based laptops and desktops running Linux and MacOS. In the coming years, Arm anticipates an increase in available OEM (original equipment manufacturer) devices. These machines facilitate the execution of computationally intensive bioinformatics and statistics tasks locally. Potential downstream applications include faster, more affordable diagnoses that can be conducted closer to hospital patients, exemplified by the pilot [ROBIN software](https://www.nottingham.ac.uk/news/genetic-brain-tumour-diagnosis). While many leading Bioconda packages now support Linux/Arm, there still emulated components that can be the bottleneck. 

**Project summary**

This project aims to benchmark specific Bioconda packages that have been built for Arm64 using the nf-core-arm-discovery repository. The participant will utilize public genomic datasets from databases such as NCBI, select appropriate datasets, and execute bioinformatics workflows on Arm-based infrastructure. The candidate will evaluate the performance, compatibility, and efficiency of these packages, document errors and failures, and investigate the reasons behind package build failures. The final deliverable will be a detailed report with performance metrics, identified issues, and recommended improvements to enhance package support on Arm64.

The deliverables of the project are as follows:

- Selection and justification of public genomic datasets.
- Execution of bioinformatics workflows using Bioconda packages on Arm64.
- Performance benchmarking and comparison with x86 architectures.
- Documentation of failed package builds and proposed fixes.
- Comprehensive report with results, analysis, and recommendations.


## Prequisites

- Intermediate understanding of Python, Bash and nextflow
- Basic experience with nf-core pipelines, Conda, Docker/Singularity, Snakemake
- Access to Arm64-based cloud instances (e.g., AWS Graviton) with plenty of memory and storage
- IP access to Public genomic databases (NCBI, ENA, etc.)

## Resources from Arm and our partners

- External Documentation: [nf-core documentation](https://nf-co.re/docs/)

- External Documentation: [AWS Graviton documentation](https://aws.amazon.com/ec2/graviton/)

- Repository: [Arm64 nf-core pipelines](https://github.com/ewels/nf-core-arm-discovery/tree/main)

- Repository: [Bioconda package repository](https://bioconda.github.io/)

- Dataset: [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/)


## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).


## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.