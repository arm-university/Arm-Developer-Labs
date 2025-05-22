---
layout: article
sidebar:
  nav: projects
subjects:
- Migration to Arm
- Libraries
title: Porting and Optimizing Arduino IDE for Windows on Arm
---

<img class="image image--xl" src="./images/Learn_on_Arm_banner.png"/>


## Description

This project focuses on **porting the Arduino IDE**—an essential open-source platform for embedded development—to run natively and efficiently on **Windows on Arm (WoA)** platforms. In addition, the project tackles a key dependency, `lzma-native`, a compression library used by the IDE, which currently [**lacks support for Windows on Arm**](https://github.com/addaleax/lzma-native/issues/132) Previous attempts to build `lzma-native` on WoA failed due to architecture-specific compilation issues and native module bindings (`node-gyp`, `liblzma`, etc.).

### Key Objectives:
- Successfully build and run the [Arduino IDE](https://github.com/arduino/arduino-ide) on Windows on Arm.
- Patch or fork [`lzma-native`](https://github.com/addaleax/lzma-native) to enable full compatibility on WoA.
- Benchmark IDE performance and memory usage on Arm64 vs. x64 emulation.
- Submit upstream patches and document issues to support long-term ecosystem health.

This project aligns strongly with Arm’s mission to expand native software compatibility on Arm-based Windows devices. It provides students with a **deep dive into cross-platform development, native module compilation, and Arm architecture optimization**, making it ideal for CV building, community contribution, and real-world system-level experience.


## Hardware, Software and Skills Required


- **Languages**: Familiarity with JavaScript (Node.js), TypeScript and C++ (lzma-native)
- **Tooling**: Familiarity or willing to learn
  - `CMake`, `Ninja`, `Visual Studio with C++ Desktop Dev`, UTM
  - `Windows Terminal`, `PowerShell`, `WSL2` (optional for cross-compilation)
- **Hardware**: Access to a physical Windows on Arm device or a [WoA Virtual Machine running through UTM](https://mac.getutm.app/gallery/windows-11-arm)
  - [Linaro Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments) available to students
- **Accounts**:
  - GitHub for forks/PRs
  - Arduino developer forums

## Resources

- [Arduino IDE GitHub repo](https://github.com/arduino/arduino-ide)
- [lzma-native GitHub repo](https://github.com/addaleax/lzma-native)
- [Issue #132 – lzma-native Windows Arm64 build failure](https://github.com/addaleax/lzma-native/issues/132)
- Arm’s official [Learn on Arm](https://learn.arm.com/) platform
- [Windows on Arm Environments – Linaro wiki](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)
- Optional: [Node.js native addon guides](https://nodejs.org/api/addons.html)

## Benefits / Prizes

- Standout projects could be internally referred for relevant positions at Arm! 📃  
- If your submission is approved, you could receive a recognised badge that you can list on your CV and shared on LinkedIn. A great way to stand out from the crowd! 🎓  
- It's a great way to demonstrate your initiative and commitment to your field.  
- It offers the opportunity to learn valuable skills that are highly relevant to a successful career at Arm! 🎉