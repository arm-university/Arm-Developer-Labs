---
title: Optimise Performance of an Algorithm Used in High-Performance Compute Using Scalable Vector Extensions (SVE / SVE2)
description: This self-service project is around finding a HPC algorithm and accelerating it with Arm’s SVE/SVE2 vectorization—demonstrating how next-generation Arm hardware can deliver significant, scalable performance gains.
subjects:
- Performance and Architecture
requires-team:
- No
platform:
- Servers and Cloud Computing
- Laptops and Desktops
- AI
sw-hw:
- Software
support-level:
- Self-Service
- Arm Ambassador Support
publication-date: 2025-05-30
license:
status:
- Published
donation:
badges: trending
layout: article
sidebar:
  nav: projects
full_description: |-
  ## Description

  **Why this is important?**

  Scalable Vector Extension (SVE) is a vector extension the A64 instruction set of the Armv8-A architecture. Armv9-A builds on SVE with the SVE2 extension. Unlike other single-instruction multiple data (SIMD) architectures, SVE and SVE2 do not define the size of the vector registers, but constrains it to a range of possible values, from a minimum of 128 bits up to a maximum of 2048 in 128-bit wide units. Therefore, any CPU vendor can implement the extension by choosing the vector register size that better suits the workloads the CPU is targeting. As of J there is growing availablity of SVE-enabled hardware, such as through cloud service providers. However, not all software has taken advantage of this feature. As such there is potential performance improvements available to software libraries and applications that add support for SVE/SVE2. 

  **Project summary**

  This project aims to identify and optimize the performance of an algorithm used in high-performance computing (HPC) by leveraging Scalable Vector Extensions (SVE) instructions. The main deliverable is an optimized version of the chosen algorithm that demonstrates a performance improvements using SVE. This project will provide practical experience in HPC, vectorization, and performance optimization. The final output will be a detailed report and a functional implementation of the optimized algorithm. 

  ## Prequisites

  - Intermediate undestanding of C, C++ or Fortran.
  - Experience with high performance compute (HPC).
  - Basic understanding of compilers such as Arm Compiler for HPC, or autovectorising compiler such as GCC.
  - Access to Arm-based servers or SVE-enabled hardware

  ## Resources from Arm and our partners

  - Learning path: [Port Code to SVE](https://learn.arm.com/learning-paths/servers-and-cloud-computing/sve/)
  - Learning path: [Migrate applications that use performance libraries](https://learn.arm.com/learning-paths/servers-and-cloud-computing/using-and-porting-performance-libs/)
  - Documentation: [SVE Programmers Guide](https://developer.arm.com/documentation/102476/0101/Programming-with-SVE)


  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

## Description

**Why this is important?**

Scalable Vector Extension (SVE) is a vector extension the A64 instruction set of the Armv8-A architecture. Armv9-A builds on SVE with the SVE2 extension. Unlike other single-instruction multiple data (SIMD) architectures, SVE and SVE2 do not define the size of the vector registers, but constrains it to a range of possible values, from a minimum of 128 bits up to a maximum of 2048 in 128-bit wide units. Therefore, any CPU vendor can implement the extension by choosing the vector register size that better suits the workloads the CPU is targeting. As of J there is growing availablity of SVE-enabled hardware, such as through cloud service providers. However, not all software has taken advantage of this feature. As such there is potential performance improvements available to software libraries and applications that add support for SVE/SVE2. 

**Project summary**

This project aims to identify and optimize the performance of an algorithm used in high-performance computing (HPC) by leveraging Scalable Vector Extensions (SVE) instructions. The main deliverable is an optimized version of the chosen algorithm that demonstrates a performance improvements using SVE. This project will provide practical experience in HPC, vectorization, and performance optimization. The final output will be a detailed report and a functional implementation of the optimized algorithm. 

## Prequisites

- Intermediate undestanding of C, C++ or Fortran.
- Experience with high performance compute (HPC).
- Basic understanding of compilers such as Arm Compiler for HPC, or autovectorising compiler such as GCC.
- Access to Arm-based servers or SVE-enabled hardware

## Resources from Arm and our partners

- Learning path: [Port Code to SVE](https://learn.arm.com/learning-paths/servers-and-cloud-computing/sve/)
- Learning path: [Migrate applications that use performance libraries](https://learn.arm.com/learning-paths/servers-and-cloud-computing/using-and-porting-performance-libs/)
- Documentation: [SVE Programmers Guide](https://developer.arm.com/documentation/102476/0101/Programming-with-SVE)


## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.