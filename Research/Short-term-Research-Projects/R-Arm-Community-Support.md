---
title: "Improving R Support for the Windows on Arm Community"
subjects:
    - "Migration to Arm"
    - "Libraries"
---

![learn_on_arm](../../images/Learn_on_Arm_banner.png)


### Target Audience  
Computer Science, Electronic Engineering, or Computer Engineering students with an interest in programming languages, operating systems, and community-driven open-source software.

## Description  

This project aims to significantly enhance the support for running **R packages on Windows 11 for Arm64 (WoA)** by identifying and contributing bug fixes / improvements to the relevant parts of the R community (e.g.,  CRAN/Bioconductor packages or even R Core / Rtools etc.). The project’s goals include:


- **Identifying CRAN and Bioconductor packages** lacking Windows/Arm64 support.
- **Proposing and testing patches upstream** for R packages that fail to build or run on WoA.
- **Engaging with the R development community** via the Windows Special interest group, [R-SIG-windows](https://stat.ethz.ch/mailman/listinfo/r-sig-windows), [R-Package-Devel](https://stat.ethz.ch/mailman/listinfo/r-package-devel) mailing list or the informal [R Contributors Slack](https://contributor.r-project.org/slack) and following the [R Contribution Guide](https://github.com/r-devel/rdevguide?tab=readme-ov-file) to submit high-quality patches.
- **Reporting new issues**, requesting comments on proposed patches, documenting process via Bugzilla and reviewing existing issues through the [bug tracker](https://bugs.r-project.org/)
- **Tracking CI coverage** for recently announced public preview of [Windows11-Arm64 GitHub-hosted runners](https://github.blog/changelog/2025-04-14-windows-arm64-hosted-runners-now-available-in-public-preview/) and potentially proposing GitHub Actions or GitLab CI templates to automate WoA builds.

Stretch Objectives:

- **Identifying, Analyzing and fixing compatibility issues** in base R and Rtools for the Windows/Arm64 environment. This may involve waiting for improved upstream support from GCC for Windows-AArch64. A summary and progress is [available here](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/28802842658/MinGW+GNU+Toolchain).


**Deliverables**:
- Patches, request for comments and bug reports the highest impact packages
- A curated list of packages with proposed WoA support status
- A short technical write-up describing the contributions and challenges

## Hardware / Software Requirements  

- **Languages**: R  
- **Tooling**: Rtools, Git, Bugzilla, Windows 11 on Arm device, GitHub CI/CD, optional Docker for cross-compilation  
- Arm64 Windows device or Access to virtualized WoA platforms via [Linaro’s Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments).

## Resources  
  
- [R Contribution Guide](https://github.com/r-devel/rdevguide?tab=readme-ov-file)  
- [R Bugzilla](https://bugs.r-project.org/)  
- [Rtools for Windows](https://cran.r-project.org/bin/windows/Rtools/)   
- [Bioconductor Build Reports](https://bioconductor.org/checkResults/)  
- Package installation results for [CRAN](https://www.r-project.org/nosvn/winutf8/ucrt3/CRAN_aarch64/install_out/) and [Bioconductor](https://www.r-project.org/nosvn/winutf8/ucrt3/BIOC_aarch64/install_out/) packages


## Benefits / Prizes  

- Standout projects could be internally referred for relevant positions at Arm! 📃  
- If your submission is approved, you could receive a recognised badge that you can list on your CV and share on LinkedIn. A great way to stand out from the crowd! 🎓  
- It's a great way to demonstrate your initiative and commitment to your field.  
- It offers the opportunity to learn valuable skills that are highly relevant to a successful career at Arm! 🎉  
