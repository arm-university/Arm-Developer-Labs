---
title: 'SpecINT2017 Benchmarking on Arm64: Evaluating Compiler and Workload Performance'
description: This self-service project profiles SPEC CPU2017 on Arm64 servers—using GCC, Clang, and Arm Compiler with top-down analysis—to reveal how compiler choices and Arm micro-architectural features impact execution time, energy efficiency, and performance bottlenecks.
subjects:
- Performance and Architecture
- Migration to Arm
requires-team:
- No
platform:
- Servers and Cloud Computing
- Laptops and Desktops
- AI
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
  ### Description

  **Why this is important?**

  SPEC is an industry standard for assessing the performance of both single-threaded and multi-threaded applications across various data types and compilers. This synthetic workload accurately represents real-world tasks and serves as a common metric for evaluating platform choices. Therefore, it is essential to comprehend the inner workings of these benchmarks to identify which microarchitectural features can enhance end-user applications.

  **Project Summary**

  This project aims to replicate the characterisation study from "SPEC CPU2017: Performance, Event, and Energy Characterization on the Core i7-8700K" on an Arm64 platform (e.g., Ampere Altra, AWS Graviton) using different compilers and performance profiling tools. The study will analyze how compiler optimizations and architectural features affect execution time, energy efficiency, and instruction throughput on Arm-based server processors. Deliverables include a comprehensive performance analysis report, reproducible benchmarking scripts, and a dataset comparing performance across different configurations. The report should locate microarchitectural bottlenecks using the [top-down methodology](https://developer.arm.com/documentation/109542/0100/Arm-Topdown-methodology), compiler performance and recommendations on how to improve performance.

  ## Prequisites

  Hardware: Access to Arm64-based server (Ampere Altra, AWS Graviton, Raspberry Pi for preliminary tests)

  Software: Familiarity with performance engineering and a OOP with a language such as C++. 

  Compilers: GCC, LLVM/Clang, Arm Compiler for Linux

  Profiling Tools: perf, Arm Performance Libraries

  Workloads: SPEC CPU2017 (academic license required), custom workloads

  ## Resources from Arm and our partners

  - Research Article: [Characterisation Paper on x86](https://research.spec.org/icpe_proceedings/2019/proceedings/p111.pdf)

  - Whitepaper: [Arm Top-down methodology](https://developer.arm.com/documentation/109542/0100/Arm-Topdown-methodology)

  - Install Guide:[Install Perf for Linux on Arm](https://learn.arm.com/install-guides/perf/)

  - Documentation: [Arm Performance Counters](https://developer.arm.com/documentation/ddi0379/a/Introduction/Performance-counters)

  - Documentation: [SPEC CPU2017 ](https://www.spec.org/cpu2017/results/)

  - Documentation: [GNU compilers](https://gcc.gnu.org/)

  - Software Download: [Arm compiler for Linux](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux)

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).


  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

### Description

**Why this is important?**

SPEC is an industry standard for assessing the performance of both single-threaded and multi-threaded applications across various data types and compilers. This synthetic workload accurately represents real-world tasks and serves as a common metric for evaluating platform choices. Therefore, it is essential to comprehend the inner workings of these benchmarks to identify which microarchitectural features can enhance end-user applications.

**Project Summary**

This project aims to replicate the characterisation study from "SPEC CPU2017: Performance, Event, and Energy Characterization on the Core i7-8700K" on an Arm64 platform (e.g., Ampere Altra, AWS Graviton) using different compilers and performance profiling tools. The study will analyze how compiler optimizations and architectural features affect execution time, energy efficiency, and instruction throughput on Arm-based server processors. Deliverables include a comprehensive performance analysis report, reproducible benchmarking scripts, and a dataset comparing performance across different configurations. The report should locate microarchitectural bottlenecks using the [top-down methodology](https://developer.arm.com/documentation/109542/0100/Arm-Topdown-methodology), compiler performance and recommendations on how to improve performance.

## Prequisites

Hardware: Access to Arm64-based server (Ampere Altra, AWS Graviton, Raspberry Pi for preliminary tests)

Software: Familiarity with performance engineering and a OOP with a language such as C++. 

Compilers: GCC, LLVM/Clang, Arm Compiler for Linux

Profiling Tools: perf, Arm Performance Libraries

Workloads: SPEC CPU2017 (academic license required), custom workloads

## Resources from Arm and our partners

- Research Article: [Characterisation Paper on x86](https://research.spec.org/icpe_proceedings/2019/proceedings/p111.pdf)

- Whitepaper: [Arm Top-down methodology](https://developer.arm.com/documentation/109542/0100/Arm-Topdown-methodology)

- Install Guide:[Install Perf for Linux on Arm](https://learn.arm.com/install-guides/perf/)

- Documentation: [Arm Performance Counters](https://developer.arm.com/documentation/ddi0379/a/Introduction/Performance-counters)

- Documentation: [SPEC CPU2017 ](https://www.spec.org/cpu2017/results/)

- Documentation: [GNU compilers](https://gcc.gnu.org/)

- Software Download: [Arm compiler for Linux](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).


## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.