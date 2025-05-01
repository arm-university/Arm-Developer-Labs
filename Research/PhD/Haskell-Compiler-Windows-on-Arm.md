# Adding Windows on Arm Support to the Glasgow Haskell Compiler (GHC)
![learn_on_arm](../../images/Learn_on_Arm_banner.png)

### Project Difficulty
Challenging

### Target Audience
PhD / Postdoctoral students in Computer Science or Electronic Engineering, with specializations in:
- Compiler construction
- Functional programming languages (especially Haskell)
- Low-level systems programming and architecture-specific optimization

## Description

The Glasgow Haskell Compiler (GHC) is the de facto standard compiler for Haskell, an advanced purely functional programming language with strong type inference and lazy evaluation. This project aims to **port GHC cto support Windows on Arm (WoA)**, a platform that is increasingly relevant with the rise of Arm-powered laptops and developer kits. Request for support has [previously been requested by the community](https://gitlab.haskell.org/ghc/ghc/-/issues/24603)

Currently, GHC lacks robust support for WoA, hindering Haskell’s reach in energy-efficient and mobile-native environments. The goal is to bridge this gap by:
- Enabling native compilation of Haskell code via GHC on WoA.
- Implementing and testing architecture-specific assembly and intrinsic functions.
- Extending the GHC build system to recognize WoA environments.
- Integrating and validating linker and runtime support on Arm-based Windows systems.

The project requires in-depth familiarity with compiler backends, calling conventions, code generation pipelines, and the use of LLVM or native code generators. Students will also gain experience in cross-compilation, Windows PE/COFF linking, and performance benchmarking on Arm CPUs.

The work has potential for real-world deployment and academic publishing, and would be of high value to the Haskell and Arm developer ecosystems.

---

## Estimated Project Duration

- 🕐 Estimated duration: **3–6 months**
- 👥 Team size: **1–3 PhD students or a small postdoctoral team**
- 📅 Suggested milestone breakdown:
  - Month 1: Toolchain and environment setup, preliminary build system adaptation
  - Month 2–3: Code generation and runtime system porting
  - Month 4–5: Testing, debugging, and upstream integration
  - Month 6: Performance tuning, documentation, and publication

---

## Hardware / Software Requirements

- **Languages & Frameworks**
  - Haskell (including Template Haskell, Core-to-STG pipeline understanding)
  - Arm64 Assembly (AArch64)

- **Tooling**
  - GHC source tree from [gitlab.haskell.org/ghc](https://gitlab.haskell.org/ghc/ghc)
  - LLVM and Clang for backend work (if using LLVM codegen)
  - MSYS2 / CMake / Ninja for Windows builds

- **Hardware**
  - Arm64 Windows device or Access to virtualized WoA platforms via [Linaro’s Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)
- **Accounts**
  - GitLab for collaboration and contribution

---

## Resources

- 🔗 [GHC Development Wiki](https://gitlab.haskell.org/ghc/ghc/-/wikis/)
- 🔧 Linaro WoA support documentation: [Linaro WoA Platforms](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)

---

## Benefits / Prizes

- Standout projects could be internally referred for relevant positions at Arm! 📃  
- If your submission is approved, you could receive a recognised badge that you can list on your CV and share on LinkedIn. A great way to stand out from the crowd! 🎓  
- It's a great way to demonstrate your initiative and commitment to your field.  
- It offers the opportunity to learn valuable skills that are highly relevant to a successful career at Arm! 🎉  
