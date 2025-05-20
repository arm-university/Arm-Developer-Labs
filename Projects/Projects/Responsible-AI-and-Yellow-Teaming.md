---
title: "DRAFT - Building Better Products on Arm with the Responsible AI methodology, Yellow Teaming"

subjects:
    - ML
    - Security
    - CI-CD
    - Performance and Architecture 
---

## Description

AI products are becoming more capable by the day. But unless we think carefully about how we build AI systems, we risk amplifying harm as fast as we’re scaling performance. Even AI products that seem successful in narrow metrics like `number of users` and `engagement` can lead to a degradation of user trust in your company, reputational risk, and drive negative societal outcomes. A more systematic product development approach is necessary for this next generation of tech to ensure we get the benefits of AI without the downsides.

This project introduces "Yellow Teaming", a structured methodology for stress-testing AI products by exploring the full spectrum of consequences when products succeed, not just fail. Students will create a YellowTeamGPT to analyze their Arm-based product concept and apply the learnings to make their product better. This exercise is an excellent way for software developers, product managers, and designers to elevate their products through thoughtful design choices above a crowded competitive landscape.

The assistant will be integrated into your product development workflow (e.g. product brainstorming, feature planning reviews, coding sessions) to aid software teams in surfacing unintended effects of new product features on your company, your users, and society. Participants can implement their YellowTeamGPT using any LLM, from a private Llama3.1-8B model on an AWS instance (tutorial linked below) to a public ChatGPT/Claude/other chatbot. Participants can also Yellow Team without an LLM by applying the methodology themselves and documenting their analysis. Analysis can be documented as product design documents, sprint retrospectives, Git-based code reviews...anything that shows the results of their thoughtful design practices.

Key Objectives of Your Project
- Collect Real-World Applications: Gather detailed accounts of AI projects developed using Yellow Teaming principles on Arm-based systems.
- Showcase Responsible AI Practices: Highlight how developers anticipate and address potential societal and ethical impacts of their AI solutions.
- Promote Arm-Based AI Development: Demonstrate the capabilities and advantages of deploying AI applications on Arm architectures, such as AWS Graviton processors or smartphones.
- Yellow Teaming Implementation: A detailed account of how Yellow Teaming was applied, including the tools/prompts used to facilitate analysis, identification of unintended consequences, strategies to mitigate negative product impacts, and/or new net-positive features ideated.


## Hardware, Software and Skills Required

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

## Resources 

- [Development In Progress essay by the Consilience Project](https://consilienceproject.org/development-in-progress/)
- [Mitigating Harmful Consequences course module by the Center for Humane Technology](https://www.humanetech.com/course) 
- Blog on Yellow Teaming - COMING SOON
- [Arm AI Learning Paths](https://learn.arm.com/tag/ml)

### Benefits

1. Standout projects could be internally referred for relevant positions at Arm! :page_with_curl:

2. If your submission is approved, you may receive a recognised badge that you can list on your CV and shared on LinkedIn. A great way to stand out from the crowd! :mortar_board:

3. Co-promotion opportunities of your product with Arm.
  
4. Problem-Solving Experience: Opportunity to gain experience with new methodologies that make your company, product, and society better. 

6. Industry Relevance: Hands-on experience with Arm-based architectures, applicable to genomics research and cloud computing.  
