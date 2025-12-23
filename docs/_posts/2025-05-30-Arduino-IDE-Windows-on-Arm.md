---
title: Porting and Optimizing Arduino IDE for Windows on Arm
description: This self-service project ports and optimizes the Arduino IDE—patching its lzma-native dependency—to run natively and efficiently on Windows on Arm, giving developers hands-on experience with cross-platform builds, Arm64 performance tuning, and upstream open-source contributions.
subjects:
- Performance and Architecture
- Migration to Arm
- Libraries
requires-team:
- No
platform:
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
  <img class="image image--xl" src="/Arm-Developer-Labs/images/arduino_logo.png" loading="lazy" decoding="async" />


  ## Description

  **Why this is important?** 

  Since 2020, there has been notable growth in multi-core Arm-based laptops and desktops, including the recent launch of Windows on Arm (WOA). In the coming years, Arm anticipates an increase in available OEM (original equipment manufacturer) devices. As such, consumers will expect both performance and battery efficiency across all WoA applications, such as the ArduinoIDE. 

  **Project summary**

  This project focuses on **porting and optimising the Arduino IDE**—an essential open-source platform for embedded development to run natively and efficiently on Windows on Arm platforms. In addition, the project tackles a key dependency, `lzma-native`, a compression library used by the IDE, which currently [**lacks support for Windows on Arm**](https://github.com/addaleax/lzma-native/issues/132) Previous attempts to build `lzma-native` on WoA failed due to architecture-specific compilation issues and native module bindings (`node-gyp`, `liblzma`, etc.).

  ### Key Objectives:
  - Successfully build and run the [Arduino IDE](https://github.com/arduino/arduino-ide) on Windows on Arm.
  - Patch or fork [`lzma-native`](https://github.com/addaleax/lzma-native) to enable full compatibility on WoA.
  - Benchmark IDE performance and memory usage on Arm64 vs. x64 emulation.
  - Submit upstream patches and document issues to support long-term ecosystem health.

  This project aligns strongly with Arm’s mission to expand native software compatibility on Arm-based Windows devices. It provides students with a **deep dive into cross-platform development, native module compilation, and Arm architecture optimization**, making it ideal for CV building, community contribution, and real-world system-level experience.

  ## Prequisites


  - Familiarity with JavaScript (Node.js), TypeScript and C++ (lzma-native)
  - Familiarity or willing to learn `CMake`, `Ninja`, `Visual Studio with C++ Desktop Dev`, UTM
  - Basic understandig of terminal programs such as `Windows Terminal`, `PowerShell` and `WSL2` 
  - Access to a physical Windows on Arm device or a [WoA Virtual Machine running through UTM](https://mac.getutm.app/gallery/windows-11-arm). see the [Linaro Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments) for more information.


  ## Resources from Arm and our partners

  - Repository: [Arduino IDE GitHub repo](https://github.com/arduino/arduino-ide)
  - Repository: [lzma-native GitHub repo](https://github.com/addaleax/lzma-native)
  - External Documentation: [Issue #132 – lzma-native Windows Arm64 build failure](https://github.com/addaleax/lzma-native/issues/132)
  - Documentation: Arm’s official [Learn on Arm](https://learn.arm.com/) platform
  - External Documentation: [Windows on Arm Environments – Linaro wiki](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)
  - Documentation: [Node.js native addon guides](https://nodejs.org/api/addons.html)

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

<img class="image image--xl" src="/Arm-Developer-Labs/images/arduino_logo.png" loading="lazy" decoding="async" />


## Description

**Why this is important?** 

Since 2020, there has been notable growth in multi-core Arm-based laptops and desktops, including the recent launch of Windows on Arm (WOA). In the coming years, Arm anticipates an increase in available OEM (original equipment manufacturer) devices. As such, consumers will expect both performance and battery efficiency across all WoA applications, such as the ArduinoIDE. 

**Project summary**

This project focuses on **porting and optimising the Arduino IDE**—an essential open-source platform for embedded development to run natively and efficiently on Windows on Arm platforms. In addition, the project tackles a key dependency, `lzma-native`, a compression library used by the IDE, which currently [**lacks support for Windows on Arm**](https://github.com/addaleax/lzma-native/issues/132) Previous attempts to build `lzma-native` on WoA failed due to architecture-specific compilation issues and native module bindings (`node-gyp`, `liblzma`, etc.).

### Key Objectives:
- Successfully build and run the [Arduino IDE](https://github.com/arduino/arduino-ide) on Windows on Arm.
- Patch or fork [`lzma-native`](https://github.com/addaleax/lzma-native) to enable full compatibility on WoA.
- Benchmark IDE performance and memory usage on Arm64 vs. x64 emulation.
- Submit upstream patches and document issues to support long-term ecosystem health.

This project aligns strongly with Arm’s mission to expand native software compatibility on Arm-based Windows devices. It provides students with a **deep dive into cross-platform development, native module compilation, and Arm architecture optimization**, making it ideal for CV building, community contribution, and real-world system-level experience.

## Prequisites


- Familiarity with JavaScript (Node.js), TypeScript and C++ (lzma-native)
- Familiarity or willing to learn `CMake`, `Ninja`, `Visual Studio with C++ Desktop Dev`, UTM
- Basic understandig of terminal programs such as `Windows Terminal`, `PowerShell` and `WSL2` 
- Access to a physical Windows on Arm device or a [WoA Virtual Machine running through UTM](https://mac.getutm.app/gallery/windows-11-arm). see the [Linaro Windows on Arm Environments](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments) for more information.


## Resources from Arm and our partners

- Repository: [Arduino IDE GitHub repo](https://github.com/arduino/arduino-ide)
- Repository: [lzma-native GitHub repo](https://github.com/addaleax/lzma-native)
- External Documentation: [Issue #132 – lzma-native Windows Arm64 build failure](https://github.com/addaleax/lzma-native/issues/132)
- Documentation: Arm’s official [Learn on Arm](https://learn.arm.com/) platform
- External Documentation: [Windows on Arm Environments – Linaro wiki](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)
- Documentation: [Node.js native addon guides](https://nodejs.org/api/addons.html)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.