---
title: 'Edge AI with NPU: always-on-AI with ExecuTorch on Cortex-M55 + Ethos-U85 → Cortex-A'
description: The vision of Edge AI compute is to embed low-power intelligent sensing, perception, and decision systems everywhere. A low-power always-on-AI island continuously monitors sensory inputs to detect triggers. When a trigger is detected, it wakes up a more capable processor to carry out high-value inference, interaction, or control tasks.
subjects:
- ML
- Performance and Architecture
- Embedded Linux
- RTOS Fundamentals
requires-team:
- No
platform:
- IoT
- Embedded and Microcontrollers
- AI
sw-hw:
- Software
- Hardware
support-level:
- Self-Service
- Arm Ambassador Support
publication-date: 2025-11-27
license:
status:
- Published
donation:
layout: article
sidebar:
  nav: projects
full_description: |-
  <img class="image image--xl" src="/Arm-Developer-Labs/images/Educate_on_Arm_banner.png" loading="lazy" decoding="async" />


  ## Description

  **Why is this important?**

  The vision of Edge AI compute is to embed intelligent low-power sensing, perception, and decision systems everywhere (in homes, wearables, infrastructure) so devices can react to subtle cues, adapt to context, and wake higher-power systems only when needed. Rather than sending everything to the cloud or running full-scale models continuously, this Edge AI system operates as a layered hierarchy:  
  - A low-power always-on-AI model continuously monitors sensory inputs (audio, motion, video) to detect triggers or anomalies.  
  - When a trigger is detected, it wakes up a more capable processor (e.g. Cortex-A running a rich OS such as Linux) to carry out further tasks. This could be high-value inference, interaction, or control tasks. It could also involve connecting to other IoT devices or to a Neoverse cloud instance.

  This architecture is key to bridging the gap between battery-constrained devices and rich AI services, making systems smarter, more efficient, and responsive without draining resources.

  **Project Summary**

  Using equipment such as the Alif Ensemble development kit (e.g. E6/E8, which includes Cortex-A, Cortex-M55, and Ethos-U85 cores - or E4 (M55+U85) + Raspberry Pi for Cortex-A), and the ExecuTorch framework, build an Edge AI prototype that implements:  

  1. A “wake-up” path: deploy a TOSA-compliant optimized model on the Cortex-M55 + Ethos-U85 pair to continuously monitor sensory signals (audio, motion, video) for wake-word, anomalies, or triggers.  
  2. A subsequent workload path: when a trigger is detected, activate a Cortex-A core to perform more complex tasks, e.g. use an LLM optimised for CPU inference, connect to and manage other IoT devices, or connect to a Neoverse cloud instance for heavier inference.  
  3. Evaluation and documentation: measure accuracy, latency, power consumption, robustness, and compare trade-offs between modalities (audio, video, motion). Demonstrate an end-to-end use case of your choice (e.g. smart assistant, anomaly alert system, gesture control, environment monitoring).  

  *Note that the Cortex-A32 included on the Alif DevKits will not be suitable for LLM inference. If using the onboard core for the project, target cloud/IoT connectivity. For LLM inference, consider connecting a Raspberry Pi 5 or similar.*

  Example: Use a microphone input to detect “Hey Arm”. After wake-up, launch an optimised LLM on Raspberry Pi Cortex-A to answer questions or control local devices.

  You are free to mix and match sensors, modalities, and tasks — as long as the core architecture (wake-on M55/U85, main task on A) is preserved.

  Many of these DevKits come with additional Ethos-U55 NPUs onboard - feel free to be creative and distribute different tasks across the different NPUs - what use-cases and applications can you achieve?

  ## What will you use?
  You should either be familiar with, or willing to learn about, the following:
  -	Programming: Python, C++, Embedded C
  -	ExecuTorch, plus knowledge of model quantization, pruning, conversion. Use of the Vela compiler and TOSA.
  -	Edge/Embedded development: bare-metal or RTOS (e.g. Zephyr), and embedded Linux (e.g. Yocto) or Raspberry Pi OS


  ## Resources from Arm and our partners
  - Arm Developer: [Edge AI](https://developer.arm.com/edge-ai)
  - Learning Path: [Navigating Machine Learning with Ethos-U processors](https://learn.arm.com/learning-paths/microcontrollers/nav-mlek/)    
  - Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)  
  - Example Board: [Alif Ensemble DevKit E8](https://www.keil.arm.com/boards/alif-semiconductor-devkit-e8-gen-1-2558a7b/features/)  
  - PyTorch Blog: [ExecuTorch support for Ethos-U85](https://pytorch.org/blog/pt-executorch-ethos-u85/)

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

<img class="image image--xl" src="/Arm-Developer-Labs/images/Educate_on_Arm_banner.png" loading="lazy" decoding="async" />


## Description

**Why is this important?**

The vision of Edge AI compute is to embed intelligent low-power sensing, perception, and decision systems everywhere (in homes, wearables, infrastructure) so devices can react to subtle cues, adapt to context, and wake higher-power systems only when needed. Rather than sending everything to the cloud or running full-scale models continuously, this Edge AI system operates as a layered hierarchy:  
- A low-power always-on-AI model continuously monitors sensory inputs (audio, motion, video) to detect triggers or anomalies.  
- When a trigger is detected, it wakes up a more capable processor (e.g. Cortex-A running a rich OS such as Linux) to carry out further tasks. This could be high-value inference, interaction, or control tasks. It could also involve connecting to other IoT devices or to a Neoverse cloud instance.

This architecture is key to bridging the gap between battery-constrained devices and rich AI services, making systems smarter, more efficient, and responsive without draining resources.

**Project Summary**

Using equipment such as the Alif Ensemble development kit (e.g. E6/E8, which includes Cortex-A, Cortex-M55, and Ethos-U85 cores - or E4 (M55+U85) + Raspberry Pi for Cortex-A), and the ExecuTorch framework, build an Edge AI prototype that implements:  

1. A “wake-up” path: deploy a TOSA-compliant optimized model on the Cortex-M55 + Ethos-U85 pair to continuously monitor sensory signals (audio, motion, video) for wake-word, anomalies, or triggers.  
2. A subsequent workload path: when a trigger is detected, activate a Cortex-A core to perform more complex tasks, e.g. use an LLM optimised for CPU inference, connect to and manage other IoT devices, or connect to a Neoverse cloud instance for heavier inference.  
3. Evaluation and documentation: measure accuracy, latency, power consumption, robustness, and compare trade-offs between modalities (audio, video, motion). Demonstrate an end-to-end use case of your choice (e.g. smart assistant, anomaly alert system, gesture control, environment monitoring).  

*Note that the Cortex-A32 included on the Alif DevKits will not be suitable for LLM inference. If using the onboard core for the project, target cloud/IoT connectivity. For LLM inference, consider connecting a Raspberry Pi 5 or similar.*

Example: Use a microphone input to detect “Hey Arm”. After wake-up, launch an optimised LLM on Raspberry Pi Cortex-A to answer questions or control local devices.

You are free to mix and match sensors, modalities, and tasks — as long as the core architecture (wake-on M55/U85, main task on A) is preserved.

Many of these DevKits come with additional Ethos-U55 NPUs onboard - feel free to be creative and distribute different tasks across the different NPUs - what use-cases and applications can you achieve?

## What will you use?
You should either be familiar with, or willing to learn about, the following:
-	Programming: Python, C++, Embedded C
-	ExecuTorch, plus knowledge of model quantization, pruning, conversion. Use of the Vela compiler and TOSA.
-	Edge/Embedded development: bare-metal or RTOS (e.g. Zephyr), and embedded Linux (e.g. Yocto) or Raspberry Pi OS


## Resources from Arm and our partners
- Arm Developer: [Edge AI](https://developer.arm.com/edge-ai)
- Learning Path: [Navigating Machine Learning with Ethos-U processors](https://learn.arm.com/learning-paths/microcontrollers/nav-mlek/)    
- Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)  
- Example Board: [Alif Ensemble DevKit E8](https://www.keil.arm.com/boards/alif-semiconductor-devkit-e8-gen-1-2558a7b/features/)  
- PyTorch Blog: [ExecuTorch support for Ethos-U85](https://pytorch.org/blog/pt-executorch-ethos-u85/)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.