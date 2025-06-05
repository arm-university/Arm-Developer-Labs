---
title: "Efficient Inference of Vision Transformers on AWS Graviton Instances"
subjects:
    - "ML"
    - "Migration to Arm"
    - "Performance and Architecture"
requires-team:
    - "No"
platform:
    - "Servers and Cloud Computing"
    - "AI"
sw-hw:
    - "Software"
support-level: 
    - "Self-Service"
    - "Arm Ambassador Support"
publication-date: 30-05-2025
license: 
---

## Description

This project investigates the deployment and optimization of Vision Transformer (ViT) models on Arm-based instances, leveraging CPU-only execution for cost-effective and scalable inference. Vision Transformers, though typically run on GPUs, are increasingly required to operate in resource-constrained environments or as part of serverless and CPU-bound cloud services. 

The aim of this project is to port, benchmark, and optimize a pre-trained ViT model (e.g., OpenSora) on Arm-based instances. Students will explore efficiency techniques such as  INT8 quantization, refactoring of expensive operations, and memory-efficient transformer kernels, and compare results with x86-based instances. Deliverables include a reproducable inference pipeline and a technical report outlining bottlenecks and optimization strategies.

## Hardware, Software and Skills Requirements

- **Languages**: Python, Pytorch, Bash; optionally C++ for ONNX Runtime extensions
- **Tooling**: 
  - AWS CLI, Docker, EC2
  - PyTorch or ONNX Runtime (CPU execution provider)
  - Hugging Face Transformers, torchvision
  - Arm Performance Libraries, Arm Streamline, Arm Forge
- **Hardware**: Access to Arm-based instances such as AWS Graviton3/Graviton4 (`c7g`, `m7g`, or `r7g`)
- **Skills**:
  - Understanding of transformer architectures, vision transformer architectures and inference optimization
  - Experience with deep learning frameworks (PyTorch or TensorFlow)
  - Familiarity with Linux, Docker, and cloud environments


## Resources to get started

- [AWS SageMaker](https://aws.amazon.com/blogs/machine-learning/run-machine-learning-inference-workloads-on-aws-graviton-based-instances-with-amazon-sagemaker/)
- [AWS Machine Learning Guide](https://github.com/aws/aws-graviton-getting-started/tree/main/machinelearning)
- [OpenSora Documentation](https://github.com/hpcaitech/Open-Sora)
- [GGML library](https://github.com/ggml-org/ggml)
- [Arm AI Learning Paths](https://learn.arm.com/tag/ml)

## Benefits / Prizes

- Standout projects could be internally referred for relevant positions at Arm!
- If your submission is approved, you could receive a recognised badge that you can list on your CV and shared on LinkedIn. A great way to stand out from the crowd!
- It's a great way to demonstrate your initiative and commitment to your field.
- It offers the opportunity to learn valuable skills that are highly relevant to a successful career at Arm!
