---
title: Python Package Porting Challenge
description: This challenge focuses on enabling Python support for Windows on Arm (WoA) to improve developer experience. While Python is widely used in research and industry, many popular packages—such as Pandas—still lack pre-built WoA binaries (win_arm64 wheels). The goal is to validate and optimise third-party packages, fix compatibility issues, and collaborate with maintainers to upstream WoA support.
subjects:
- Libraries
requires-team:
- No
platform:
- Laptops and Desktops
sw-hw:
- Software
support-level:
- Self-Service
- Arm Ambassador Support
publication-date: 2025-11-03
license:
status:
- Published
donation:
layout: article
sidebar:
  nav: projects
full_description: |-
  <img class="image image--xl" src="/Arm-Developer-Labs/images/Educate_on_Arm_banner.png" loading="lazy" decoding="async" />

  ### *We are open to supporting participants through hardware donations, such as gift cards to help procure Windows on Arm laptops for development and research purposes. Please reach out to us at Arm-Developer-Labs@arm.com for more details on eligibility*

  ## Description

  Windows on Arm brings the power of Arm architecture to Windows users, delivering energy efficiency and performance for a wide range of devices. As adoption grows, ensuring a seamless developer experience is critical, especially for Python, one of the most widely used languages in research, education, and industry.

  This challenge is on advancing the Arm ecosystem by addressing critical gaps in software enablement. A key objective is enabling Windows on Arm (WoA) across the WoA Python package ecosystem, which involves validating and optimising 3rd party packages to ensure seamless functionality across diverse environments.

  Despite Python’s widespread adoption, many popular packages such as Pandas still lack pre-built Windows on Arm binaries (`win_arm64` wheels), creating a barrier for developers and researchers who rely on these tools for data analysis and scientific computing. If a Windows on Arm Python developer wanted to use Pandas, they would have to recompile from source, which required the correct toolchain and is not guaranteed to compile or run successfully.

  Key Objectives:

  - Python Ecosystem Enablement: Turn at least 5 amber projects green on [Windows Arm64 Wheels](https://tonybaloney.github.io/windows-arm64-wheels/).
  - Identify packages that do not have readily available `win_arm64` wheels. Identify any bugs or regressions when porting to application (for example, `x86` instrinsics) and create a patch that resolves issues and enables the packages to correctly build and run performantly. 
  - Community Collaboration: Engage with global developer communities, such as Python package maintainers, to get WoA package support upstreamed and integrated. 


  ## Prequisites

  - Intermediate to advance understanding of the Python language
  - Some experience on creating python packages and continuous integration testing. 
  - If you decide to tackle non pure-python packages that are written in other languages, you will need an intermediate understanding of the language the program was written in (e.g., Rust, Java, C++ etc.).

  ## Resources from Arm and our partners

  - External Documentation: [Methods to run Windows on Arm64](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)
  - External Documentation: [Python Packages without Windows-on-Arm Wheels](https://tonybaloney.github.io/windows-arm64-wheels/)
  - External Documentation: [Python Packages without Windows-on-Arm Wheels additional resource](http://www.winarm64wheels.com/)
  - Learning Path: [Sampling CPython with WindowsPerf](https://learn.arm.com/learning-paths/laptops-and-desktops/windowsperf_sampling_cpython/)
  - Community Post: [Python on Windows Arm64](https://discuss.python.org/t/python-on-windows-arm64/104524)
  - External Documentation: [Status of Python versions](https://devguide.python.org/versions/)
  - GitHub Repository: [Source code and documentation to build Python Wheels](https://github.com/pypa/cibuildwheel)


  ## Support Level

  If you would like to request a small donation to help procure Windows on Arm hardware, please reach out to us at Arm-Developer-Lab@arm.com. 

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

  To receive the benefits, you must share your contribution through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

<img class="image image--xl" src="/Arm-Developer-Labs/images/Educate_on_Arm_banner.png" loading="lazy" decoding="async" />

### *We are open to supporting participants through hardware donations, such as gift cards to help procure Windows on Arm laptops for development and research purposes. Please reach out to us at Arm-Developer-Labs@arm.com for more details on eligibility*

## Description

Windows on Arm brings the power of Arm architecture to Windows users, delivering energy efficiency and performance for a wide range of devices. As adoption grows, ensuring a seamless developer experience is critical, especially for Python, one of the most widely used languages in research, education, and industry.

This challenge is on advancing the Arm ecosystem by addressing critical gaps in software enablement. A key objective is enabling Windows on Arm (WoA) across the WoA Python package ecosystem, which involves validating and optimising 3rd party packages to ensure seamless functionality across diverse environments.

Despite Python’s widespread adoption, many popular packages such as Pandas still lack pre-built Windows on Arm binaries (`win_arm64` wheels), creating a barrier for developers and researchers who rely on these tools for data analysis and scientific computing. If a Windows on Arm Python developer wanted to use Pandas, they would have to recompile from source, which required the correct toolchain and is not guaranteed to compile or run successfully.

Key Objectives:

- Python Ecosystem Enablement: Turn at least 5 amber projects green on [Windows Arm64 Wheels](https://tonybaloney.github.io/windows-arm64-wheels/).
- Identify packages that do not have readily available `win_arm64` wheels. Identify any bugs or regressions when porting to application (for example, `x86` instrinsics) and create a patch that resolves issues and enables the packages to correctly build and run performantly. 
- Community Collaboration: Engage with global developer communities, such as Python package maintainers, to get WoA package support upstreamed and integrated. 


## Prequisites

- Intermediate to advance understanding of the Python language
- Some experience on creating python packages and continuous integration testing. 
- If you decide to tackle non pure-python packages that are written in other languages, you will need an intermediate understanding of the language the program was written in (e.g., Rust, Java, C++ etc.).

## Resources from Arm and our partners

- External Documentation: [Methods to run Windows on Arm64](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)
- External Documentation: [Python Packages without Windows-on-Arm Wheels](https://tonybaloney.github.io/windows-arm64-wheels/)
- External Documentation: [Python Packages without Windows-on-Arm Wheels additional resource](http://www.winarm64wheels.com/)
- Learning Path: [Sampling CPython with WindowsPerf](https://learn.arm.com/learning-paths/laptops-and-desktops/windowsperf_sampling_cpython/)
- Community Post: [Python on Windows Arm64](https://discuss.python.org/t/python-on-windows-arm64/104524)
- External Documentation: [Status of Python versions](https://devguide.python.org/versions/)
- GitHub Repository: [Source code and documentation to build Python Wheels](https://github.com/pypa/cibuildwheel)


## Support Level

If you would like to request a small donation to help procure Windows on Arm hardware, please reach out to us at Arm-Developer-Lab@arm.com. 

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must share your contribution through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.