---
title: Responsible AI and Yellow Teaming
description: This self-service project equips teams with a YellowTeamGPT workflow that probes Arm-based AI products for unintended impacts—turning responsible-AI stress-testing into a core step of the development cycle.
subjects:
- ML
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
layout: article
sidebar:
  nav: projects
full_description: |-
  ## Description


  **Why this is important?** 

  AI products are becoming more capable by the day. But unless we think carefully about how we build AI systems, we risk amplifying harm as fast as we’re scaling performance. Even AI products that seem successful in narrow metrics like `number of users` and `engagement` can lead to a degradation of user trust in your company, reputational risk, and drive negative societal outcomes. A more systematic product development approach is necessary for this next generation of tech to ensure we get the benefits of AI without the downsides.

  **Project summary**

  This project introduces "Yellow Teaming", a structured methodology for stress-testing AI products by exploring the full spectrum of consequences when products succeed, not just fail. Students will create a YellowTeamGPT to analyze their Arm-based product concept and apply the learnings to make their product better. This exercise is an excellent way for software developers, product managers, and designers to elevate their products through thoughtful design choices above a crowded competitive landscape.

  The assistant will be integrated into your product development workflow (e.g. product brainstorming, feature planning reviews, coding sessions) to aid software teams in surfacing unintended effects of new product features on your company, your users, and society. Participants can implement their YellowTeamGPT using any LLM, from a private Llama3.1-8B model on an AWS instance (tutorial linked below) to a public ChatGPT/Claude/other chatbot. Participants can also Yellow Team without an LLM by applying the methodology themselves and documenting their analysis. Analysis can be documented as product design documents, sprint retrospectives, Git-based code reviews...anything that shows the results of their thoughtful design practices.

  Key Objectives of Your Project
  - Collect Real-World Applications: Gather detailed accounts of AI projects developed using Yellow Teaming principles on Arm-based systems.
  - Showcase Responsible AI Practices: Highlight how developers anticipate and address potential societal and ethical impacts of their AI solutions.
  - Promote Arm-Based AI Development: Demonstrate the capabilities and advantages of deploying AI applications on Arm architectures, such as AWS Graviton processors or smartphones.
  - Yellow Teaming Implementation: A detailed account of how Yellow Teaming was applied, including the tools/prompts used to facilitate analysis, identification of unintended consequences, strategies to mitigate negative product impacts, and/or new net-positive features ideated.


  ## Prequisites

  If deploying a private Llama model -> 
  - **Hardware**:
    - Access to an Arm-based cloud instance, for example Arm-based Graviton4 processors.
  - **Software**:
    - PyTorch and Hugging Face account
    - `torchchat` repo and dependencies
    - Hugging Face CLI for LLM download
    - Git, Python 3.10+, and various common build essentials (e.g., `make`, `g++`)
  - **Skills**:
    - Proficiency in Python and PyTorch
    - [Hugging Face account](https://huggingface.co/)
    - Understanding of LLMs and prompting techniques

  If using a public LLM ->
  - **Hardware**:
    - None needed
  - **Software**:
    - Access to a public LLM
  - **Skills**:
    - Understanding of LLMs and prompting techniques

  ## Resources from Arm and our partners

  - External Course: [Mitigating Harmful Consequences course module by the Center for Humane Technology](https://www.humanetech.com/course) 
  - Blog: [Build Responsible AI products with your own Yellow Teaming LLM](https://pytorch.org/blog/build-responsible-ai-products-with-your-own-yellow-teaming-llm/)
  - Learning Paths: [AI Learning Paths](https://learn.arm.com/tag/ml)

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).


  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

## Description


**Why this is important?** 

AI products are becoming more capable by the day. But unless we think carefully about how we build AI systems, we risk amplifying harm as fast as we’re scaling performance. Even AI products that seem successful in narrow metrics like `number of users` and `engagement` can lead to a degradation of user trust in your company, reputational risk, and drive negative societal outcomes. A more systematic product development approach is necessary for this next generation of tech to ensure we get the benefits of AI without the downsides.

**Project summary**

This project introduces "Yellow Teaming", a structured methodology for stress-testing AI products by exploring the full spectrum of consequences when products succeed, not just fail. Students will create a YellowTeamGPT to analyze their Arm-based product concept and apply the learnings to make their product better. This exercise is an excellent way for software developers, product managers, and designers to elevate their products through thoughtful design choices above a crowded competitive landscape.

The assistant will be integrated into your product development workflow (e.g. product brainstorming, feature planning reviews, coding sessions) to aid software teams in surfacing unintended effects of new product features on your company, your users, and society. Participants can implement their YellowTeamGPT using any LLM, from a private Llama3.1-8B model on an AWS instance (tutorial linked below) to a public ChatGPT/Claude/other chatbot. Participants can also Yellow Team without an LLM by applying the methodology themselves and documenting their analysis. Analysis can be documented as product design documents, sprint retrospectives, Git-based code reviews...anything that shows the results of their thoughtful design practices.

Key Objectives of Your Project
- Collect Real-World Applications: Gather detailed accounts of AI projects developed using Yellow Teaming principles on Arm-based systems.
- Showcase Responsible AI Practices: Highlight how developers anticipate and address potential societal and ethical impacts of their AI solutions.
- Promote Arm-Based AI Development: Demonstrate the capabilities and advantages of deploying AI applications on Arm architectures, such as AWS Graviton processors or smartphones.
- Yellow Teaming Implementation: A detailed account of how Yellow Teaming was applied, including the tools/prompts used to facilitate analysis, identification of unintended consequences, strategies to mitigate negative product impacts, and/or new net-positive features ideated.


## Prequisites

If deploying a private Llama model -> 
- **Hardware**:
  - Access to an Arm-based cloud instance, for example Arm-based Graviton4 processors.
- **Software**:
  - PyTorch and Hugging Face account
  - `torchchat` repo and dependencies
  - Hugging Face CLI for LLM download
  - Git, Python 3.10+, and various common build essentials (e.g., `make`, `g++`)
- **Skills**:
  - Proficiency in Python and PyTorch
  - [Hugging Face account](https://huggingface.co/)
  - Understanding of LLMs and prompting techniques

If using a public LLM ->
- **Hardware**:
  - None needed
- **Software**:
  - Access to a public LLM
- **Skills**:
  - Understanding of LLMs and prompting techniques

## Resources from Arm and our partners

- External Course: [Mitigating Harmful Consequences course module by the Center for Humane Technology](https://www.humanetech.com/course) 
- Blog: [Build Responsible AI products with your own Yellow Teaming LLM](https://pytorch.org/blog/build-responsible-ai-products-with-your-own-yellow-teaming-llm/)
- Learning Paths: [AI Learning Paths](https://learn.arm.com/tag/ml)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).


## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.