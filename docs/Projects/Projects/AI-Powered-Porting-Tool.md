---
layout: article
license: null
platform:
- Servers and Cloud Computing
- Laptops and Desktops
- Mobile, Graphics, and Gaming
- AI
publication-date: 30-05-2025
requires-team:
- 'No'
sidebar:
  nav: projects
subjects:
- CI-CD
- ML
- Migration to Arm
support-level:
- Self-Service
- Arm Ambassador Support
sw-hw:
- Software
title: AI-Powered Package Porting Tool for the Arm Architectures
---

<img class="image image--xl" src="./images/Research_on_arm_banner.png"/>

## Description

This project challenges students to build an intelligent automation tool for porting software packages — for use in domains such as [bioinformatic pipelines with Nextflow](https://github.com/arm-university/Arm-Projects-Labs/blob/main/PhD-Level/Bioinformatic-Pipeline-Analysis-INTERMEDIATE.md) or [statistics with R](https://github.com/arm-university/Arm-Projects-Labs/blob/main/PhD-Level/R-Arm-Community-Support-INTERMEDIATE.md).

Although most top Bioconda packages now support Linux/Arm, there's still a significant gap for native macOS on Apple Silicon, where many packages default to emulated x86 environments. Similarly, for the R community, Windows-on-Arm support for community created packages is lacking with many packages unable to build due to issues such as x86-specific code. 
Given the large number of community packages, applying manual patches is not only time-consuming but also inefficient, as many involve similar, repetitive adjustments—highlighting the need for a scalable, automated solution.
The goal is to build a sophisticated system (beyond simple shell scripts) that uses dependency graph analysis, machine learning, to:

- Identify unported packages
- Trace recursive dependency issues
- Recommend or auto-generate build recipes and steps
- Evaluate build success and reattempt intelligently
- Generate pull requests when confident of a fix. 
- For complex packages, offer guidance to developers on how to port them—for example, by suggesting tools like SSE2NEON for translating x86 SSE intrinsics.
- Be extensible to work with various  packaging systems and languages

🔬 Students will gain practical experience with CI/CD systems, Python packaging with bioconda, 

This project is an ideal blend of automation, machine learning, and systems programming — built with real-world impact in mind. The outcome could directly contribute to open source ecosystems and help bring cutting-edge bioinformatics tools to wider hardware audiences.

## Hardware, Software and Skills Required

Hardware: Access to Apple Silicon either through the cloud or with Physical hardware
Languages: Familiarity with Python, Bash and Nextflow
Tooling: Experience or willing to learn nf-core pipelines, Conda, BioConda and Docker/Singularity.
Background: Familiar with genomics or interest in computational biology. 

## Resources 

[Example Porting Script for Bioconda](https://github.com/dslarm/bioconda-contrib-notes/tree/main)

[Bioconda package repository](https://bioconda.github.io/)

[nf-core documentation](https://nf-co.re/docs/)

[Bioconductor Build Reports](https://bioconductor.org/checkResults/)  
Package installation results for [CRAN](https://www.r-project.org/nosvn/winutf8/ucrt3/CRAN_aarch64/install_out/) and [Bioconductor](https://www.r-project.org/nosvn/winutf8/ucrt3/BIOC_aarch64/install_out/) packages

[Arm64 nf-core pipelines](https://github.com/ewels/nf-core-arm-discovery/tree/main)
[NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/)

### Benefits

1. Standout projects could be internally referred for relevant positions at Arm! :page_with_curl:

2. If your submission is approved, you will receive a recognised badge that you can list on your CV and shared on LinkedIn. A great way to stand out from the crowd! :mortar_board:

<img class="image image--l" src="./images/ACA_badge.jpg"/>

3. Problem-Solving Experience: Opportunity to debug and optimize bioinformatics software for emerging computing architectures.

4. Industry Relevance: Hands-on experience with Arm-based architectures, applicable to genomics research and cloud computing.  :tada: