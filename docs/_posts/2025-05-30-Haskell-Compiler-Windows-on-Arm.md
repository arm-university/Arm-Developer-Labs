---
title: Adding Windows on Arm Support to the Glasgow Haskell Compiler (GHC)
description: This self-service project brings native Glasgow Haskell Compiler support to Windows on Arm—unlocking efficient Arm-laptop builds, extending Haskell’s reach, and giving contributors hands-on experience with Arm64 code generation and runtime integration.
subjects:
- Migration to Arm
- Performance and Architecture
requires-team:
- No
platform:
- Servers and Cloud Computing
- Laptops and Desktops
sw-hw:
- Software
- Hardware
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
  <img class="image image--xl" src="/Arm-Developer-Labs/images/Learn_on_Arm_banner.png" loading="lazy" decoding="async" />


  ## Description

  **Why this is important?**

  The Glasgow Haskell Compiler (GHC) is the de facto standard compiler for Haskell, an advanced purely functional programming language with strong type inference and lazy evaluation. This project aims to **port GHC to support Windows on Arm (WoA)**, a platform that is increasingly relevant with the rise of Arm-powered laptops and developer kits. Arm anticipates more original equipment manufacturers (OEMs) to be available in the coming years.


  **Project summary**

  Currently, GHC lacks robust support for WoA, hindering Haskell’s reach in energy-efficient and mobile-native environments (Request for support has [previously been requested by the community](https://gitlab.haskell.org/ghc/ghc/-/issues/24603)). The goal is to bridge this gap by:
  - Enabling native compilation of Haskell code via GHC on WoA.
  - Implementing and testing architecture-specific assembly and intrinsic functions.
  - Extending the GHC build system to recognize WoA environments.
  - Integrating and validating linker and runtime support on Arm-based Windows systems.

  The project requires in-depth familiarity with compiler backends, calling conventions, code generation pipelines, and the use of LLVM or native code generators. Students will also gain experience in cross-compilation, Windows PE/COFF linking, and performance benchmarking on Arm CPUs.

  The work has potential for real-world deployment and academic publishing, and would be of high value to the Haskell and Arm developer ecosystems.

  ---

  ## Prequisites

  - Advanced understanding of Haskell (including Template Haskell, Core-to-STG pipeline understanding)
  - Arm64 Windows device or Access to virtualized WoA platforms via [Linaro’s Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)
  - Intemediate understanding of Arm64 Assembly (AArch64)
  - Comfortable using compilers such as LLVM and Clang for backend work (if using LLVM codegen)
  - Access to MSYS2 / CMake / Ninja for Windows builds


  ## Resources from Arm and our partners

  - External Documentation: [GHC Development Wiki](https://gitlab.haskell.org/ghc/ghc/-/wikis/)
  - Repository: [GHC source tree](https://gitlab.haskell.org/ghc/ghc)
  - External Documentation: [Linaro WoA Support Documentation](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)


  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

<img class="image image--xl" src="/Arm-Developer-Labs/images/Learn_on_Arm_banner.png" loading="lazy" decoding="async" />


## Description

**Why this is important?**

The Glasgow Haskell Compiler (GHC) is the de facto standard compiler for Haskell, an advanced purely functional programming language with strong type inference and lazy evaluation. This project aims to **port GHC to support Windows on Arm (WoA)**, a platform that is increasingly relevant with the rise of Arm-powered laptops and developer kits. Arm anticipates more original equipment manufacturers (OEMs) to be available in the coming years.


**Project summary**

Currently, GHC lacks robust support for WoA, hindering Haskell’s reach in energy-efficient and mobile-native environments (Request for support has [previously been requested by the community](https://gitlab.haskell.org/ghc/ghc/-/issues/24603)). The goal is to bridge this gap by:
- Enabling native compilation of Haskell code via GHC on WoA.
- Implementing and testing architecture-specific assembly and intrinsic functions.
- Extending the GHC build system to recognize WoA environments.
- Integrating and validating linker and runtime support on Arm-based Windows systems.

The project requires in-depth familiarity with compiler backends, calling conventions, code generation pipelines, and the use of LLVM or native code generators. Students will also gain experience in cross-compilation, Windows PE/COFF linking, and performance benchmarking on Arm CPUs.

The work has potential for real-world deployment and academic publishing, and would be of high value to the Haskell and Arm developer ecosystems.

---

## Prequisites

- Advanced understanding of Haskell (including Template Haskell, Core-to-STG pipeline understanding)
- Arm64 Windows device or Access to virtualized WoA platforms via [Linaro’s Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)
- Intemediate understanding of Arm64 Assembly (AArch64)
- Comfortable using compilers such as LLVM and Clang for backend work (if using LLVM codegen)
- Access to MSYS2 / CMake / Ninja for Windows builds


## Resources from Arm and our partners

- External Documentation: [GHC Development Wiki](https://gitlab.haskell.org/ghc/ghc/-/wikis/)
- Repository: [GHC source tree](https://gitlab.haskell.org/ghc/ghc)
- External Documentation: [Linaro WoA Support Documentation](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)


## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.