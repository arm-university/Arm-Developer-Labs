# Improving R Support for the Windows on Arm Community 
![learn_on_arm](../images/Learn_on_Arm_banner.png)

### Project Difficulty  
Challenging

### Target Audience  
Computer Science, Electronic Engineering, or Computer Engineering students with an interest in programming languages, operating systems, and community-driven open-source software.

## Description  

This project aims to significantly enhance the support for running **R and Rtools on Windows 11 for Arm64 (WoA)** by contributing to the **R Core**, **Rtools** or the **CRAN/Bioconductor ecosystems**. Building on the groundwork laid out in [this blog post on R for 64-bit Arm Windows](https://blog.r-project.org/2024/04/23/r-on-64-bit-arm-windows/), the project’s goals include:

- **Analyzing and fixing upstream compatibility issues** in base R and Rtools for the Windows/Arm64 environment.
- **Reviewing the R Bugzilla tracker** (https://bugs.r-project.org/) for unresolved WoA-related issues and either fixing or updating them.
- **Identifying CRAN and Bioconductor packages** lacking Windows/Arm64 support.
- **Proposing and testing patches upstream** for R packages that fail to build or run on WoA.
- **Engaging with the R development community** via the [R Contributors Slack](https://contributor.r-project.org/slack) and following the [R Contribution Guide](https://github.com/r-devel/rdevguide?tab=readme-ov-file) to submit high-quality patches.
- **Reporting new issues**, requesting comments on proposed patches, and documenting process via Bugzilla.
- **Tracking CI availability** for Windows/Arm64 runners and potentially proposing GitHub Actions or GitLab CI templates to automate WoA builds.

This project encourages the use of native tooling and Rtools under WoA, while exposing students to low-level platform support, compiler toolchains (LLVM/MinGW), and ecosystem-scale problem solving.

**Deliverables**:
- Patches, request for comments and bug reports the highest impact R base, tools and packages
- A curated list of packages with proposed WoA support status
- A short technical write-up describing the contributions and challenges
- (Optional) GitHub Actions workflows for building/testing R packages on Windows/Arm64

## Estimated Project Duration  

- Estimated Time: Variable  
- Ideal Team Size: 1–2 students  
- Suitable for individual research projects, summer internships, or final-year theses

## Hardware / Software Requirements  

- **Languages**: R  
- **Tooling**: Rtools, Git, Bugzilla, Windows 11 on Arm device (Surface Pro X or similar), GitHub CI/CD, optional Docker for cross-compilation  
- Arm64 Windows device or Access to virtualized WoA platforms via [Linaro’s Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments).

## Resources  

- [R on Windows-on-Arm blog post](https://blog.r-project.org/2024/04/23/r-on-64-bit-arm-windows/)  
- [R Contribution Guide](https://github.com/r-devel/rdevguide?tab=readme-ov-file)  
- [R Bugzilla](https://bugs.r-project.org/)  
- [Rtools for Windows](https://cran.r-project.org/bin/windows/Rtools/)  
- [CRAN Package Check Results](https://cran.r-project.org/web/checks/check_results.html)  
- [Bioconductor Build Reports](https://bioconductor.org/checkResults/)  
- [GitHub R Development Discussions](https://github.com/r-devel/r-source/discussions)  
- [Example R CI Setup for Arm](https://github.com/actions/setup-r)  

## Benefits / Prizes  

- Standout projects could be internally referred for relevant positions at Arm! 📃  
- If your submission is approved, you could receive a recognised badge that you can list on your CV and share on LinkedIn. A great way to stand out from the crowd! 🎓  
- It's a great way to demonstrate your initiative and commitment to your field.  
- It offers the opportunity to learn valuable skills that are highly relevant to a successful career at Arm! 🎉  
