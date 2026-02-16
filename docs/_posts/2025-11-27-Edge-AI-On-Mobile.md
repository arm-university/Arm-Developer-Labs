---
title: 'SME2 on vivo X300 and other devices: Mobile Edge AI Projects for multi-modal inference.'
description: Leverage the latest SME2 (Scalable Matrix Extension 2) available on the newest vivo X300 smartphones (built on Arm Lumex CSS) or other SME2-enabled devices for advanced image/video, audio and text processing edge AI. Explore how SME2, via KleidiAI, enables larger matrix workloads, higher throughput, and novel applications on device without cloud connectivity required.
subjects:
- ML
- Performance and Architecture
- Libraries
- Edge AI
requires-team:
- No
platform:
- Mobile, Graphics, and Gaming
- AI
- IoT
sw-hw:
- Software
support-level:
- Self-Service
- Arm Ambassador Support
publication-date: 2025-11-27
license:
status:
- Published
badges:
- trending
- recently_added
donation:
layout: article
sidebar:
  nav: projects
full_description: |-
  ## Description

  ### Why is this important?

  SME2 (Scalable Matrix Extension 2) is the latest CPU extension on Arm Lumex CSS. Designed to accelerate matrix-oriented compute workloads directly on device, SME2 improves AI/ML performance. This is by accelerating models that rely on operations like matrix multiplication, common in transformers, convolutional neural networks (CNNs), and large language models (LLMs). Via KleidiAI, SME2 is seamlessly integrated into frameworks such as ExecuTorch, LiteRT, ONNX Runtime so it is automatically leveraged for applications depending on whether SME2 is present on the host device.

  [SME2](https://www.arm.com/technologies/sme2)

  The vivo X300 is built on Arm Lumex. SME2 now enables AI compute that previously was too heavy or inaccessible on mobile. Developers can now utilise these advancements to deliver advanced applications on-device, reducing latency, increasing data privacy, and unlocking novel use-cases.

  [vivo X300, built on Arm Lumex](https://www.arm.com/company/success-library/vivo-x300-smartphones)

  Other devices also support SME2, including both Apple and Android - [see the full list here](https://learn.arm.com/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started#devices)

  ### Project Summary

  Select a **mobile edge AI application** that benefits from large matrix operations, multi-modal fusion, or transformer-based processing accelerated by SME2, with real-time speech-to-speech translation, profanity filtering or filler-word removal, and on-device Small Language Models (SLMs) as key example use cases.

  Example project areas:  
  - Real-time speech-to-speech translation
  - On-device SLM for contextual understanding, rewriting, or assistant tasks
  - Profanity detection and filtering (masking, rewriting, audio bleeping)
  - Filler-word removal / speech clean-up (e.g., removing “um”, “uh”, false starts)
  - Real-time video semantic segmentation (e.g., AR captions + background removal)
  - Live object detection with natural-language description
  - Multi-sensor fusion (camera + IMU + microphone) for gesture + voice interaction

  Identify a model architecture that maps to wide matrix operations (e.g., ViT, MLP-Mixer, multi-branch CNN with large FC layers). Utilise a mobile-friendly framework (e.g., ExecuTorch, LiteRT, ONNX Runtime, MediaPipe) to leverage SME2 optimizations. Optimize quantization, memory layout, and verify that the large matrix multiplications get scheduled efficiently on the SME2-enabled CPU. Build a mobile app (Android or iOS) that executes the model and utilises it for a compelling use-case.

  Utilise the resources and learning paths below and create an exciting and challenging application. As a bonus, you could compare performance vs a reference phone without SME2.

  ## Resources from Arm and our partners

  - Arm Developer: [Launchpad - Mobile AI](https://developer.arm.com/mobile-graphics-and-gaming/ai-mobile)
  - Learning Path: [Mobile AI/ML Performance Profiling](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/profiling-ml-on-arm/)
  - Learning Path: [Build an Android chat app with Llama, KleidiAI, ExecuTorch, and XNNPACK](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-llama3-chat-android-app-using-executorch-and-xnnpack/)
  - Learning Path: [Vision LLM Inference on Android with KleidiAI](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/vision-llm-inference-on-android-with-kleidiai-and-mnn/)
  - Learning Path: [Build a Hands-Free Selfie Android Application with MediaPipe](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-android-selfie-app-using-mediapipe-multimodality/)
  - Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)
  - Arm / Cambridge University edX course: [AI at the Edge on Arm (Mobile)](https://www.edx.org/learn/computer-science/arm-education-ai-at-the-edge-on-arm)

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.

  ## Example Reference Project

  [This project, submitted to Arm Developer Labs and also created as part of the Arm AI Developer Challenge, is an example of Edge inference on mobile using the ExecuTorch runtime and XNNPACK](https://github.com/abhitorch81/PocketQSAR/) 

  ---
---

## Description

### Why is this important?

SME2 (Scalable Matrix Extension 2) is the latest CPU extension on Arm Lumex CSS. Designed to accelerate matrix-oriented compute workloads directly on device, SME2 improves AI/ML performance. This is by accelerating models that rely on operations like matrix multiplication, common in transformers, convolutional neural networks (CNNs), and large language models (LLMs). Via KleidiAI, SME2 is seamlessly integrated into frameworks such as ExecuTorch, LiteRT, ONNX Runtime so it is automatically leveraged for applications depending on whether SME2 is present on the host device.

[SME2](https://www.arm.com/technologies/sme2)

The vivo X300 is built on Arm Lumex. SME2 now enables AI compute that previously was too heavy or inaccessible on mobile. Developers can now utilise these advancements to deliver advanced applications on-device, reducing latency, increasing data privacy, and unlocking novel use-cases.

[vivo X300, built on Arm Lumex](https://www.arm.com/company/success-library/vivo-x300-smartphones)

Other devices also support SME2, including both Apple and Android - [see the full list here](https://learn.arm.com/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started#devices)

### Project Summary

Select a **mobile edge AI application** that benefits from large matrix operations, multi-modal fusion, or transformer-based processing accelerated by SME2, with real-time speech-to-speech translation, profanity filtering or filler-word removal, and on-device Small Language Models (SLMs) as key example use cases.

Example project areas:  
- Real-time speech-to-speech translation
- On-device SLM for contextual understanding, rewriting, or assistant tasks
- Profanity detection and filtering (masking, rewriting, audio bleeping)
- Filler-word removal / speech clean-up (e.g., removing “um”, “uh”, false starts)
- Real-time video semantic segmentation (e.g., AR captions + background removal)
- Live object detection with natural-language description
- Multi-sensor fusion (camera + IMU + microphone) for gesture + voice interaction

Identify a model architecture that maps to wide matrix operations (e.g., ViT, MLP-Mixer, multi-branch CNN with large FC layers). Utilise a mobile-friendly framework (e.g., ExecuTorch, LiteRT, ONNX Runtime, MediaPipe) to leverage SME2 optimizations. Optimize quantization, memory layout, and verify that the large matrix multiplications get scheduled efficiently on the SME2-enabled CPU. Build a mobile app (Android or iOS) that executes the model and utilises it for a compelling use-case.

Utilise the resources and learning paths below and create an exciting and challenging application. As a bonus, you could compare performance vs a reference phone without SME2.

## Resources from Arm and our partners

- Arm Developer: [Launchpad - Mobile AI](https://developer.arm.com/mobile-graphics-and-gaming/ai-mobile)
- Learning Path: [Mobile AI/ML Performance Profiling](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/profiling-ml-on-arm/)
- Learning Path: [Build an Android chat app with Llama, KleidiAI, ExecuTorch, and XNNPACK](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-llama3-chat-android-app-using-executorch-and-xnnpack/)
- Learning Path: [Vision LLM Inference on Android with KleidiAI](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/vision-llm-inference-on-android-with-kleidiai-and-mnn/)
- Learning Path: [Build a Hands-Free Selfie Android Application with MediaPipe](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-android-selfie-app-using-mediapipe-multimodality/)
- Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)
- Arm / Cambridge University edX course: [AI at the Edge on Arm (Mobile)](https://www.edx.org/learn/computer-science/arm-education-ai-at-the-edge-on-arm)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.

## Example Reference Project

[This project, submitted to Arm Developer Labs and also created as part of the Arm AI Developer Challenge, is an example of Edge inference on mobile using the ExecuTorch runtime and XNNPACK](https://github.com/abhitorch81/PocketQSAR/) 

---