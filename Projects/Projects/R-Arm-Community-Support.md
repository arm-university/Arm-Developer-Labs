---
title: "Improving R Support for the Windows on Arm Community"
description: "This self-service project boosts the R ecosystem on Windows on Arm by identifying unsupported packages, upstreaming fixes, and automating builds—so data scientists can run their workflows natively on fast, efficient Arm64 laptops and desktops."
subjects:
    - "Performance and Architecture"
    - "Migration to Arm"
    - "Libraries"
requires-team:
    - "No"
platform:
    - "Laptops and Desktops"
sw-hw:
    - "Software"
support-level: 
    - "Self-Service"
    - "Arm Ambassador Support"
publication-date: 2025-05-30
license:
status:
    - "Published" 
donation: 
---

![learn_on_arm](../../images/Learn_on_Arm_banner.png)


## Description  

**Why this is important?**

Since 2020, there has been notable growth in multi-core Arm-based laptops and desktops, including the recent launch of Windows on Arm (WOA). In the coming years, Arm anticipates an increase in available OEM (original equipment manufacturer) devices. As such, developers will expect packages to be available for WoA so that downstream applications can more easily build for WoA platforms.

**Project summary**


This project aims to significantly enhance the support for running **R packages on Windows 11 for Arm64 (WoA)** by identifying and contributing bug fixes / improvements to the relevant parts of the R community (e.g.,  CRAN/Bioconductor packages or even R Core / Rtools etc.). The project’s goals include:


- **Identifying CRAN and Bioconductor packages** lacking Windows/Arm64 support.
- **Proposing and testing patches upstream** for R packages that fail to build or run on WoA.
- **Engaging with the R development community** via the Windows Special interest group, [R-SIG-windows](https://stat.ethz.ch/mailman/listinfo/r-sig-windows), [R-Package-Devel](https://stat.ethz.ch/mailman/listinfo/r-package-devel) mailing list or the informal [R Contributors Slack](https://contributor.r-project.org/slack) and following the [R Contribution Guide](https://github.com/r-devel/rdevguide?tab=readme-ov-file) to submit high-quality patches.
- **Reporting new issues**, requesting comments on proposed patches, documenting process via Bugzilla and reviewing existing issues through the [bug tracker](https://bugs.r-project.org/)
- **Tracking CI coverage** for recently announced public preview of [Windows11-Arm64 GitHub-hosted runners](https://github.blog/changelog/2025-04-14-windows-arm64-hosted-runners-now-available-in-public-preview/) and potentially proposing GitHub Actions or GitLab CI templates to automate WoA builds.

Stretch Objectives:

- **Identifying, Analyzing and fixing compatibility issues** in base R and Rtools for the Windows/Arm64 environment. This may involve waiting for improved upstream support from GCC for Windows-AArch64. A summary and progress is [available here](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/28802842658/MinGW+GNU+Toolchain).

The deliverables include:

- Patches, request for comments and bug reports the highest impact packages
- A curated list of packages with proposed WoA support status
- A short technical write-up describing the contributions and challenges

## Prequisites 

- Intermediate understanding of the R language  
- Intermediate understanding of Rtools, Git and Docker for cross-compilation.
- Basic understanding or willingness to learn Bugzilla, Windows 11 operating system and GitHub CI/CD. 
- Arm64 Windows device or Access to virtualized WoA platforms via [Linaro’s Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments).

## Resources from Arm and our partners
  
- Documentation: [R Contribution Guide](https://github.com/r-devel/rdevguide?tab=readme-ov-file)  
- Documentation: [R Bugzilla](https://bugs.r-project.org/)  
- Documentation: [Rtools for Windows](https://cran.r-project.org/bin/windows/Rtools/)   
- Documentation: [Bioconductor Build Reports](https://bioconductor.org/checkResults/)  
- Documentation: Package installation results for [CRAN](https://www.r-project.org/nosvn/winutf8/ucrt3/CRAN_aarch64/install_out/) and [Bioconductor](https://www.r-project.org/nosvn/winutf8/ucrt3/BIOC_aarch64/install_out/) packages

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors , who are part of the Arm Developer program and the R community. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).


## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
