---
title: 'Ethos-U85 NPU Applications with TOSA Model Explorer: Exploring Next-Gen Edge AI Inference'
description: Push the limits of Edge AI by deploying the heaviest inference applications possible on Ethos-U85. Students will explore transformer-based and TOSA-optimized workloads that demonstrate performance levels on the next-gen of Ethos NPUs.
subjects:
- ML
- Performance and Architecture
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
badges: trending
donation:
layout: article
sidebar:
  nav: projects
full_description: |-
  <img class="image image--xl" src="/Arm-Developer-Labs/images/Educate_on_Arm_banner.png" loading="lazy" decoding="async" />

  ## Description

  **Why is this important?**

  The Arm Ethos-U85 NPU represents a major leap in bringing *heavy inference* to constrained embedded systems. With its full transformer operator support, expanded MAC throughput, and native TOSA compatibility, the Ethos-U85 enables developers to deploy models and workloads that were previously too intensive for MCU-class devices.

  This project challenges you to explore the boundaries of what’s possible on Ethos-U85. The goal is to demonstrate inference performance and model complexity that is now achievable due to the architectural improvements and transformer acceleration capabilities of the Ethos-U85.

  [Ethos-U85 Launch](https://newsroom.arm.com/blog/ethos-u85)  

  **Project Summary**

  Using hardware such as the Alif Ensemble E4/E6/E8 DevKits (all include Ethos-U85) or a comparable platform or Arm Fixed Virtual Platform Corstone-320, your task is to design and benchmark an advanced edge inference application that exploits the Ethos-U85’s compute and transformer capabilities.

  Your project should include:

  1. Model Deployment and Optimization  
     Select a computationally intensive model — ideally transformer-based or multi-branch convolutional — and deploy it on the Ethos-U85 using:
     - The TOSA Model Explorer extension to inspect and adapt unsupported or experimental models for TOSA compliance.  
     - The Vela compiler for optimization.  

     These tools can be used to:
     - Convert and visualize model graphs in TOSA format.  
     - Identify unsupported operators.  
     - Modify or substitute layers for compatibility using the Flatbuffers schema before re-exporting.  
     - Run Vela for optimized compilation targeting Ethos-U85.

  2. Application Demonstration 
     Implement a working example that highlights the Ethos-U85’s strengths in real-world inference. Possible categories include:  
     - Transformers on Edge: lightweight BERT, ViT, or audio transformers (e.g. speech or sound event classification).  
     - High-resolution Vision: semantic segmentation, object detection on large input sizes, or multi-head perception networks.  
     - Multi-modal Fusion: combining audio, image, or sensor streams for contextual understanding.  

  3. Analysis and Benchmarking 
     Report quantitative results on:
     - Inference latency, throughput (FPS or tokens/s), and memory footprint.  
     - Power efficiency under load (optional).  
     - Comparative performance versus Ethos-U55/U65 (use available benchmarks for reference or utilise the other Ethos-U NPUs provided in the Alif DevKits).  
     - The effect of TOSA optimization — demonstrate measurable improvements from graph conversion and operator fusion.

  ---

  ## What kind of projects should you target?

  To clearly demonstrate the leap from Ethos-U55/U65 to U85, choose projects that meet at least one of the following criteria:

  - Transformer-heavy architectures: e.g. attention blocks, transformer encoders, ViTs, or hybrid CNN+transformer models.  
    - *Example:* an audio event detection transformer that must process longer sequences or higher-resolution spectrograms.  
  - High-resolution or multi-branch networks: models with high input dimensionality or multiple processing paths that saturate NPU throughput.  
    - *Example:* 512×512 semantic segmentation or multi-object detection.  
  - Dense post-processing or large fully connected layers: cases where U55/U65 memory limits or MAC bandwidth previously restricted performance.  
    - *Example:* large MLP heads or transformer token mixers.  
  - Multi-modal pipelines: combining multiple sensor inputs (e.g. image + IMU + audio) where the NPU must maintain concurrency or shared intermediate representations.  

  The Ethos-U85 is ideal for projects where model performance is constrained by attention layers, large activations, or operator types that previously required fallback to the CPU. Use the Ethos-U85 to eliminate those fallbacks and achieve full-NPU execution of advanced topologies.

  ---

  ## What will you use?
  You should be familiar with, or willing to learn about:
  - Programming: Python, C/C++  
  - ExecuTorch or TensorFlow Lite (Micro/LiteRT)
  - Techniques for optimising AI models for the edge (quantization, pruning, etc.)
  - Optimization Tools: 
    - TOSA Model Explorer
    - .tflite to .tosa converter (if using Tensorflow rather than ExecuTorch)
    - Vela compiler for Ethos-U  
  - Bare-metal or RTOS (e.g., Zephyr)  

  ---

  ## Resources from Arm and our partners
  - Arm Developer: [Edge AI](https://developer.arm.com/edge-ai)
  - Learning Path: [Navigating Machine Learning with Ethos-U processors](https://learn.arm.com/learning-paths/microcontrollers/nav-mlek/)    
  - Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)  
  - Example Board: [Alif Ensemble DevKit E8](https://www.keil.arm.com/boards/alif-semiconductor-devkit-e8-gen-1-2558a7b/features/)  
  - Documentation: [TOSA Specification](https://www.mlplatform.org/tosa/), [TOSA Model Explorer](https://github.com/arm/tosa-adapter-model-explorer), and [TOSA Reference Model](https://gitlab.arm.com/tosa/tosa-reference-model)
  - PyTorch Blog: [ExecuTorch support for Ethos-U85](https://pytorch.org/blog/pt-executorch-ethos-u85/)
  ---

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

<img class="image image--xl" src="/Arm-Developer-Labs/images/Educate_on_Arm_banner.png" loading="lazy" decoding="async" />

## Description

**Why is this important?**

The Arm Ethos-U85 NPU represents a major leap in bringing *heavy inference* to constrained embedded systems. With its full transformer operator support, expanded MAC throughput, and native TOSA compatibility, the Ethos-U85 enables developers to deploy models and workloads that were previously too intensive for MCU-class devices.

This project challenges you to explore the boundaries of what’s possible on Ethos-U85. The goal is to demonstrate inference performance and model complexity that is now achievable due to the architectural improvements and transformer acceleration capabilities of the Ethos-U85.

[Ethos-U85 Launch](https://newsroom.arm.com/blog/ethos-u85)  

**Project Summary**

Using hardware such as the Alif Ensemble E4/E6/E8 DevKits (all include Ethos-U85) or a comparable platform or Arm Fixed Virtual Platform Corstone-320, your task is to design and benchmark an advanced edge inference application that exploits the Ethos-U85’s compute and transformer capabilities.

Your project should include:

1. Model Deployment and Optimization  
   Select a computationally intensive model — ideally transformer-based or multi-branch convolutional — and deploy it on the Ethos-U85 using:
   - The TOSA Model Explorer extension to inspect and adapt unsupported or experimental models for TOSA compliance.  
   - The Vela compiler for optimization.  

   These tools can be used to:
   - Convert and visualize model graphs in TOSA format.  
   - Identify unsupported operators.  
   - Modify or substitute layers for compatibility using the Flatbuffers schema before re-exporting.  
   - Run Vela for optimized compilation targeting Ethos-U85.

2. Application Demonstration 
   Implement a working example that highlights the Ethos-U85’s strengths in real-world inference. Possible categories include:  
   - Transformers on Edge: lightweight BERT, ViT, or audio transformers (e.g. speech or sound event classification).  
   - High-resolution Vision: semantic segmentation, object detection on large input sizes, or multi-head perception networks.  
   - Multi-modal Fusion: combining audio, image, or sensor streams for contextual understanding.  

3. Analysis and Benchmarking 
   Report quantitative results on:
   - Inference latency, throughput (FPS or tokens/s), and memory footprint.  
   - Power efficiency under load (optional).  
   - Comparative performance versus Ethos-U55/U65 (use available benchmarks for reference or utilise the other Ethos-U NPUs provided in the Alif DevKits).  
   - The effect of TOSA optimization — demonstrate measurable improvements from graph conversion and operator fusion.

---

## What kind of projects should you target?

To clearly demonstrate the leap from Ethos-U55/U65 to U85, choose projects that meet at least one of the following criteria:

- Transformer-heavy architectures: e.g. attention blocks, transformer encoders, ViTs, or hybrid CNN+transformer models.  
  - *Example:* an audio event detection transformer that must process longer sequences or higher-resolution spectrograms.  
- High-resolution or multi-branch networks: models with high input dimensionality or multiple processing paths that saturate NPU throughput.  
  - *Example:* 512×512 semantic segmentation or multi-object detection.  
- Dense post-processing or large fully connected layers: cases where U55/U65 memory limits or MAC bandwidth previously restricted performance.  
  - *Example:* large MLP heads or transformer token mixers.  
- Multi-modal pipelines: combining multiple sensor inputs (e.g. image + IMU + audio) where the NPU must maintain concurrency or shared intermediate representations.  

The Ethos-U85 is ideal for projects where model performance is constrained by attention layers, large activations, or operator types that previously required fallback to the CPU. Use the Ethos-U85 to eliminate those fallbacks and achieve full-NPU execution of advanced topologies.

---

## What will you use?
You should be familiar with, or willing to learn about:
- Programming: Python, C/C++  
- ExecuTorch or TensorFlow Lite (Micro/LiteRT)
- Techniques for optimising AI models for the edge (quantization, pruning, etc.)
- Optimization Tools: 
  - TOSA Model Explorer
  - .tflite to .tosa converter (if using Tensorflow rather than ExecuTorch)
  - Vela compiler for Ethos-U  
- Bare-metal or RTOS (e.g., Zephyr)  

---

## Resources from Arm and our partners
- Arm Developer: [Edge AI](https://developer.arm.com/edge-ai)
- Learning Path: [Navigating Machine Learning with Ethos-U processors](https://learn.arm.com/learning-paths/microcontrollers/nav-mlek/)    
- Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)  
- Example Board: [Alif Ensemble DevKit E8](https://www.keil.arm.com/boards/alif-semiconductor-devkit-e8-gen-1-2558a7b/features/)  
- Documentation: [TOSA Specification](https://www.mlplatform.org/tosa/), [TOSA Model Explorer](https://github.com/arm/tosa-adapter-model-explorer), and [TOSA Reference Model](https://gitlab.arm.com/tosa/tosa-reference-model)
- PyTorch Blog: [ExecuTorch support for Ethos-U85](https://pytorch.org/blog/pt-executorch-ethos-u85/)
---

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.