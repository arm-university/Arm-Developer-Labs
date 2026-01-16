---
title: "HLS4ML - AI SoC Design"
description: "Explore using HLS4ML, an open-source project developed at organisations including CERN, Fermilab, and MIT, to create hardware for AI, compatible with Arm IP to form an SoC capable of tape-out."
subjects:
  - "ML"
  - "Performance and Architecture"
requires-team:
  - "No"
platform:
  - "AI"
sw-hw:
  - "Software"
  - "Hardware"
support-level:
  - "Self-Service"
  - "Arm Ambassador Support"
publication-date: 2026-01-16
license:
status:
  - "Hidden"
---

![learn_on_arm](../../images/Learn_on_Arm_banner.png)

# SoC Labs Logo

## Description

### Why is this important?

Tools such as HLS4ML have proven extremely successful for rapid FPGA-based AI acceleration, particularly in research and edge-AI contexts. However, there is currently a significant gap between FPGA-targeted HLS workflows and reproducible, tape-out-ready ASIC design flows.

Many AI accelerator projects focus on a single model, dataset, or hardware target. This project instead focuses on defining a repeatable and auditable methodology for translating AI models into hardware IP suitable for integration into an Arm-based SoC and potential fabrication.

We are looking for a clear, well-documented path from AI model → HLS → RTL → Arm-based SoC → tape-out. This reduces the cost, risk, and expertise barrier for startups, academics, and independent developers to innovate on silicon.

### Project Summary

This project explores the use of HLS4ML (and comparable HLS-based AI tools) to develop a repeatable, tape-out-capable workflow for creating AI accelerator IP that can be integrated with Arm IP into a full SoC design.

The focus is not on a single accelerator or model, but on defining a methodology that includes:

AI and software layer
- Selection of AI models (e.g. CNNs, transformers, or classical ML models).
- Quantisation, pruning, and model optimisation strategies compatible with hardware implementation.
- Clear mapping between software frameworks (e.g. TensorFlow / PyTorch) and hardware-friendly representations.

Hardware generation layer
- Use of HLS4ML (or alternatives where appropriate) to generate synthesizable RTL.
- Identification of constraints and modifications required to move from FPGA-oriented HLS outputs to ASIC-suitable RTL.
- Definition of design rules, interfaces, and verification steps that ensure reproducibility.

SoC Design
- Integration of the generated accelerator as an IP block within an Arm-based SoC.
- Documentation of the additional steps required beyond FPGA validation: synthesis targets, timing closure considerations, verification, and power/area trade-offs.
- Clear identification of what changes are needed to move from “works on FPGA” to “ready for fabrication”.

The output of this project is a reference flow, example designs, and documentation that others can follow to reproducibly generate AI accelerator IP suitable for integration into real Arm-based silicon.

## What will you use?
You should be familiar with, or willing to learn about:
- High-level Synthesis (HLS), including HLS4ML or similar tools
- Machine learning frameworks (e.g. TensorFlow, PyTorch)
- AI model optimisation for hardware (quantisation, pruning)
- RTL and digital design basics
- Arm-based SoC and accelerator integration concepts
- Software–hardware co-design
- Reproducible design workflows

## Resources from Arm and our partners

# TODO

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

This project can also be supported by SoC Labs in Southampton. 
# TODO

## Benefits 

Standout project contributions will result in digital badges for CV building, recognised by Arm Talent Acquisition. We are currently discussing with national agencies the potential for funding streams for Arm Developer Labs projects, which would flow to you, not us.


To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.

