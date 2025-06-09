---
layout: article
license: null
platform:
- Servers and Cloud Computing
- AI
publication-date: 2025-05-30
requires-team:
- 'No'
sidebar:
  nav: projects
status:
- Draft
subjects:
- ML
- Migration to Arm
- Performance and Architecture
support-level:
- Self-Service
- Arm Ambassador Support
sw-hw:
- Software
title: Efficient Inference of Vision Transformers on AWS Graviton Instances
---

## Description

This project investigates the deployment and optimization of text-to-video transformer models on Arm-based instances, leveraging CPU-only execution for cost-effective and scalable inference. Vision Transformers, though typically run on GPUs, are increasingly required to operate in resource-constrained environments or as part of serverless and CPU-bound cloud services. 

The aim of this project is to port, benchmark, and optimize a pre-trained ViT model (e.g., OpenSora) on Arm-based instances. Students will explore efficiency techniques such as  INT8 quantization, refactoring of expensive operations, and memory-efficient transformer kernels, and compare results with x86-based instances. Deliverables include a reproducable inference pipeline and a technical report outlining bottlenecks and optimization strategies.

## Prequisites

- Intemediate understanding of Python; 

- Expeience using PyTorch or ONNX Runtime (CPU execution provider)
- Experience with libraries such as Hugging Face Transformers, torchvision
- Access to Arm-based instances such as AWS Graviton3/Graviton4 (`c7g`, `m7g`, or `r7g`)
- Understanding of transformer architectures, vision transformer architectures and inference optimization
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

Standout project contributions will result in preferential internal referrals to Arm Talent Acquisition (with digital badges for CV building).  And we are currently discussing with national agencies the potential for funding streams for Arm Developer Labs projects, which would flow to you, not us.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.