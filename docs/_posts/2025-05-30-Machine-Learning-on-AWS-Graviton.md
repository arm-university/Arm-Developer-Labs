---
title: Efficient Inference of text-to-video (OpenSora) on AWS Graviton Instances
description: This self-service project ports and tunes OpenSora text-to-video transformers on AWS Graviton CPUs—showcasing cost-efficient, quantized, CPU-only inference pipelines and guiding best-practice optimization for Arm-based cloud AI workloads.
subjects:
- ML
- Migration to Arm
- Performance and Architecture
requires-team:
- No
platform:
- Servers and Cloud Computing
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
layout: article
sidebar:
  nav: projects
full_description: |-
  <img class="image image--xl" src="/Arm-Developer-Labs/images/opensora.png" loading="lazy" decoding="async" />

  ## Description

  **Why is this important?**

  This project investigates the deployment and optimization of text-to-video transformer models on Arm-based instances, leveraging CPU-only execution for cost-effective and scalable inference. Vision Transformers, though typically run on GPUs, are increasingly desire to operate in resource-constrained environments for power efficiency. 


  **Project Summary**

  The aim of this project is to port, benchmark, and optimize a pre-trained ViT model (e.g., OpenSora) on Arm-based instances. This could include post-training quantization and investigation in how to speed up performance. Students will explore efficiency techniques such as  INT8 quantization, refactoring of expensive operations, and memory-efficient transformer kernels, and compare results across GPU and CPU platforms. Deliverables include a reproducable inference pipeline and a technical report outlining bottlenecks and optimization strategies.

  ## Prequisites

  - Intemediate understanding of Python.
  - Understanding of transformer architectures, vision transformer architectures and inference optimization
  - Experience using PyTorch or ONNX Runtime (CPU execution provider)
  - Experience with libraries such as Hugging Face Transformers, torchvision
  - Access to Arm-based instances such as AWS Graviton3/Graviton4 (`c7g`, `m7g`, or `r7g`)
  - Familiarity with Linux, Docker, and cloud environments


  ## Resources from Arm and our partners


  - Learning Paths: [Arm AI Learning Paths](https://learn.arm.com/tag/ml)
  - Repository: [AWS Machine Learning Guide](https://github.com/aws/aws-graviton-getting-started/tree/main/machinelearning)
  - Blog: [AWS SageMaker](https://aws.amazon.com/blogs/machine-learning/run-machine-learning-inference-workloads-on-aws-graviton-based-instances-with-amazon-sagemaker/)
  - External Documentation: [OpenSora Documentation](https://github.com/hpcaitech/Open-Sora)
  - Repository: [GGML library](https://github.com/ggml-org/ggml)


  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  ## Benefits 
  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

<img class="image image--xl" src="/Arm-Developer-Labs/images/opensora.png" loading="lazy" decoding="async" />

## Description

**Why is this important?**

This project investigates the deployment and optimization of text-to-video transformer models on Arm-based instances, leveraging CPU-only execution for cost-effective and scalable inference. Vision Transformers, though typically run on GPUs, are increasingly desire to operate in resource-constrained environments for power efficiency. 


**Project Summary**

The aim of this project is to port, benchmark, and optimize a pre-trained ViT model (e.g., OpenSora) on Arm-based instances. This could include post-training quantization and investigation in how to speed up performance. Students will explore efficiency techniques such as  INT8 quantization, refactoring of expensive operations, and memory-efficient transformer kernels, and compare results across GPU and CPU platforms. Deliverables include a reproducable inference pipeline and a technical report outlining bottlenecks and optimization strategies.

## Prequisites

- Intemediate understanding of Python.
- Understanding of transformer architectures, vision transformer architectures and inference optimization
- Experience using PyTorch or ONNX Runtime (CPU execution provider)
- Experience with libraries such as Hugging Face Transformers, torchvision
- Access to Arm-based instances such as AWS Graviton3/Graviton4 (`c7g`, `m7g`, or `r7g`)
- Familiarity with Linux, Docker, and cloud environments


## Resources from Arm and our partners


- Learning Paths: [Arm AI Learning Paths](https://learn.arm.com/tag/ml)
- Repository: [AWS Machine Learning Guide](https://github.com/aws/aws-graviton-getting-started/tree/main/machinelearning)
- Blog: [AWS SageMaker](https://aws.amazon.com/blogs/machine-learning/run-machine-learning-inference-workloads-on-aws-graviton-based-instances-with-amazon-sagemaker/)
- External Documentation: [OpenSora Documentation](https://github.com/hpcaitech/Open-Sora)
- Repository: [GGML library](https://github.com/ggml-org/ggml)


## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

## Benefits 
Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.


To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.