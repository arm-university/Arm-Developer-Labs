---
title: AI-Powered Package Porting Tool for the Arm Architectures
description: This self-service project creates an AI-driven porting engine that analyzes package dependencies, auto-generates fixes, and submits pull requests—accelerating native macOS and Windows-on-Arm support for bioinformatics and R software so researchers can run demanding workflows directly on modern Arm devices.
subjects:
- CI-CD
- ML
- Migration to Arm
requires-team:
- No
platform:
- Servers and Cloud Computing
- Laptops and Desktops
- Mobile, Graphics, and Gaming
- AI
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
  ## Description

  **Why this is important?** 

  Bioconda is a specialized package repository for bioinformatics and genomics. Since 2020, there has been notable growth in multi-core Arm-based laptops and desktops, including the recent launch of Windows on Arm. In the coming years, Arm anticipates an increase in available OEM (original equipment manufacturer) devices. These machines facilitate the execution of computationally intensive bioinformatics and statistics tasks locally. Potential downstream applications include faster, more affordable diagnoses that can be conducted closer to hospital patients, exemplified by the pilot [ROBIN software](https://www.nottingham.ac.uk/news/genetic-brain-tumour-diagnosis). While many leading Bioconda packages now support Linux/Arm, there remains a gap in native macOS and Windows on Arm support, as numerous packages default to emulated x86 environments. Additionally, the R community faces challenges with Windows-on-Arm support for community-created packages, with many unable to build due to x86-specific code issues.

  **Project Summary**

  This project challenges you to build an intelligent automation tool for porting software packages — for use in domains such as [bioinformatic pipelines with Nextflow](https://github.com/arm-university/Arm-Developer-Labs/blob/main/Projects/Projects/Bioinformatic-Pipeline-Analysis.md) or [statistics with R](https://github.com/arm-university/Arm-Developer-Labs/blob/main/Projects/Projects/R-Arm-Community-Support.md).

  Given the large number of community packages, applying manual patches is not only time-consuming but also inefficient, as many involve similar, repetitive adjustments—highlighting the need for a scalable, automated solution.
  The goal is to build a sophisticated system (beyond simple shell scripts) that uses dependency graph analysis, machine learning, to:

  - Identify unported packages
  - Trace recursive dependency issues
  - Recommend or auto-generate build recipes and steps
  - Evaluate build success and reattempt intelligently
  - Generate pull requests when confident of a fix. 
  - For complex packages, offer guidance to developers on how to port them—for example, by suggesting tools like SSE2NEON for translating x86 SSE intrinsics.
  - Be extensible to work with various  packaging systems and languages

  This project is a blend of automation, machine learning, and systems programming. The outcome could directly contribute to open source ecosystems and help bring cutting-edge bioinformatics tools to wider hardware audiences.

  ## Prerequisites

  - Access to Apple Silicon or Windows on Arm machine. 
  - Familiarity with Python, Bash and Nextflow
  - Familiar with genomics/bioinformatics or statistics with the R language. 
  - Experience or willing to learn nf-core pipelines, Conda, BioConda and Docker/Singularity.


  ## Resources from Arm and our partners

  - External Resource: [Example Porting Script for Bioconda](https://github.com/dslarm/bioconda-contrib-notes/tree/main), [Arm64 nf-core pipelines](https://github.com/ewels/nf-core-arm-discovery/tree/main) and [Bioconda package repository](https://bioconda.github.io/)
  - Documentation: [nf-core documentation](https://nf-co.re/docs/)
  - External Documentation: [Bioconductor Build Reports](https://bioconductor.org/checkResults/), Package installation results for [CRAN](https://www.r-project.org/nosvn/winutf8/ucrt3/CRAN_aarch64/install_out/) and [Bioconductor](https://www.r-project.org/nosvn/winutf8/ucrt3/BIOC_aarch64/install_out/) packages
  - Dataset: Example [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/)

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

## Description

**Why this is important?** 

Bioconda is a specialized package repository for bioinformatics and genomics. Since 2020, there has been notable growth in multi-core Arm-based laptops and desktops, including the recent launch of Windows on Arm. In the coming years, Arm anticipates an increase in available OEM (original equipment manufacturer) devices. These machines facilitate the execution of computationally intensive bioinformatics and statistics tasks locally. Potential downstream applications include faster, more affordable diagnoses that can be conducted closer to hospital patients, exemplified by the pilot [ROBIN software](https://www.nottingham.ac.uk/news/genetic-brain-tumour-diagnosis). While many leading Bioconda packages now support Linux/Arm, there remains a gap in native macOS and Windows on Arm support, as numerous packages default to emulated x86 environments. Additionally, the R community faces challenges with Windows-on-Arm support for community-created packages, with many unable to build due to x86-specific code issues.

**Project Summary**

This project challenges you to build an intelligent automation tool for porting software packages — for use in domains such as [bioinformatic pipelines with Nextflow](https://github.com/arm-university/Arm-Developer-Labs/blob/main/Projects/Projects/Bioinformatic-Pipeline-Analysis.md) or [statistics with R](https://github.com/arm-university/Arm-Developer-Labs/blob/main/Projects/Projects/R-Arm-Community-Support.md).

Given the large number of community packages, applying manual patches is not only time-consuming but also inefficient, as many involve similar, repetitive adjustments—highlighting the need for a scalable, automated solution.
The goal is to build a sophisticated system (beyond simple shell scripts) that uses dependency graph analysis, machine learning, to:

- Identify unported packages
- Trace recursive dependency issues
- Recommend or auto-generate build recipes and steps
- Evaluate build success and reattempt intelligently
- Generate pull requests when confident of a fix. 
- For complex packages, offer guidance to developers on how to port them—for example, by suggesting tools like SSE2NEON for translating x86 SSE intrinsics.
- Be extensible to work with various  packaging systems and languages

This project is a blend of automation, machine learning, and systems programming. The outcome could directly contribute to open source ecosystems and help bring cutting-edge bioinformatics tools to wider hardware audiences.

## Prerequisites

- Access to Apple Silicon or Windows on Arm machine. 
- Familiarity with Python, Bash and Nextflow
- Familiar with genomics/bioinformatics or statistics with the R language. 
- Experience or willing to learn nf-core pipelines, Conda, BioConda and Docker/Singularity.


## Resources from Arm and our partners

- External Resource: [Example Porting Script for Bioconda](https://github.com/dslarm/bioconda-contrib-notes/tree/main), [Arm64 nf-core pipelines](https://github.com/ewels/nf-core-arm-discovery/tree/main) and [Bioconda package repository](https://bioconda.github.io/)
- Documentation: [nf-core documentation](https://nf-co.re/docs/)
- External Documentation: [Bioconductor Build Reports](https://bioconductor.org/checkResults/), Package installation results for [CRAN](https://www.r-project.org/nosvn/winutf8/ucrt3/CRAN_aarch64/install_out/) and [Bioconductor](https://www.r-project.org/nosvn/winutf8/ucrt3/BIOC_aarch64/install_out/) packages
- Dataset: Example [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.