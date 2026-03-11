# Understanding AI: A Practical Workshop for Humanities and Social Science Researchers

<img align="right" width="300" src="https://raw.githubusercontent.com/gpizzorno/understanding-ai/ad2d7b134a276c93c59a6a1e3a956c7613fc6021/assets/understanding_ai_thumb.png?token=GHSAT0AAAAAADW3EG66227TUSNL6BRZW26S2NQGESQ">

Artificial intelligence (AI), large language models (LLMs), and machine learning (ML) are reshaping research across disciplines. This two-day workshop offers humanities and social science researchers a clear, accessible introduction to contemporary AI systems: what they are, how they differ from traditional computing, what they can—and cannot—do, and how to critically assess their outputs. Through guided demonstrations and hands-on exercises participants will gain a grounded understanding of the concepts behind today’s AI tools.

[Day 1](#day-1-key-concepts-and-off-the-shelf-tools) focuses on conceptual foundations and hands-on exploration with off-the-shelf tools. Participants will see how training data, model limitations, and evaluation methods shape AI behavior, and will practice identifying common failure modes. Day 1 also introduces practical ways to use LLMs to support programming and technical work as a bridge to the more hands-on workflows of Day 2.

[Day 2](#day-2-programmatic-approaches) shifts toward programming and applied workflows using open-source Python tools and pre-trained models, with an emphasis on choosing appropriate tasks, understanding what a model is doing, and evaluating results.

A self-paced online introduction to Python will be available for participants who want to learn or brush up on programming basics [between the two workshop days](#between-workshops). 

## Workshop learning goals

By the end of the workshop, participants will be equipped with both a deeper theoretical understanding of AI systems and practical skills for integrating them thoughtfully into their own research. Specific learning goals include:

- distinguish key categories of systems (traditional software vs. ML, generative AI as a subset of AI)
- explain, at a high level, how models are trained and why training data matters
- recognize common limitations and failure modes (brittleness, overfitting, hallucination-like behavior, and evaluation pitfalls)
- apply basic evaluation concepts (training/testing split, accuracy and related metrics, precision/recall) in a research-appropriate way
- use LLMs more effectively and safely for research and technical support (prompt structuring, asking for explanations, iterative refinement)
- run and adapt simple Python-based pipelines using pre-trained models for common research tasks
- document and communicate model choices, assumptions, and limitations in a way that supports responsible use

## Tools

The workshop uses a mix of browser-based tools and Python.

- Browser-based: [Teachable Machine](https://teachablemachine.withgoogle.com), [Gandalf](https://gandalf.lakera.ai/gandalf), and [NotebookLM](https://notebooklm.google.com)
- Python-based (Day 2): [Jupyter](https://jupyter.org), and libraries/tools for working with pre-trained models such as [Hugging Face](https://huggingface.co).

## Plan

### Day 1: Key concepts and off-the-shelf tools

#### Learning Objectives

By the end of Day 1, participants will be able to:

- Distinguish key categories of AI systems: traditional software vs. machine learning, generative AI as a subset of AI
- Explain, at a high level, how models are trained, what training data is, and why it matters
- Describe the basic architecture of neural networks and language models (tokens, weights, attention, transformers)
- Recognize the difference between supervised, unsupervised, and reinforcement learning—and identify which applies in a given context
- Apply basic evaluation concepts, training/testing split, accuracy, precision, recall, F1, in a research-appropriate way
- Identify and name common LLM failure modes: hallucination, reasoning failure, instruction-following errors, bias, inconsistency, and adversarial susceptibility
- Explain why LLM guardrails are brittle, and what prompt injection demonstrates about model behavior
- Articulate what a conversational LLM interface (like NotebookLM) can and cannot do for systematic research tasks

#### Prework

Participants should plan on modest prework in advance of Day 1:

- Bring a laptop with a modern web browser
- Have a Google account (for NotebookLM, a g.harvard account is fine)
- Optional but recommended: a GitHub account (useful for accessing shared materials)

#### Schedule

| Time               | Activity |
|--------------------|----------|
| 9:00 – 9:30 | Introduction |
| 9:30 – 10:05 | Activity: Teachable Machine |
| 10:05 – 10:25 | Discussion: Training and Bias |
| 10:25 – 10:35 | *Break* |
| 10:35 – 11:10 | Activity: Gandalf  |
| 11:10 – 11:35 | Discussion: LLM Limitations |
| 11:35 – 12:05 | *Lunch* |
| 12:05 – 1:00 | Activity: NotebookLM  |
| 1:00 – 1:25 | Discussion: Failure Modes and Assessment  |
| 1:25 – 1:35 | *Break* |
| 1:35 – 1:50 | Coding with LLMs |
| 1:50 – 2:00 | Closing  |


### Between workshops

A [self-paced online introduction to Python]() is available for participants who want to learn or brush up on programming basics between the two workshop days. Follow the [setup instructions](documents/python_setup.md) to get started.

We recommend going over Units 1 and 2 of the Python introduction before Day 2.

### Day 2: Programmatic approaches

#### Learning Objectives

By the end of Day 2, participants will be able to:

- Load and run a pre-trained NER model using Hugging Face Transformers
- Process a corpus of text files programmatically using a Python loop
- Transform model output into structured tabular data and export it as CSV
- Evaluate model performance against self-produced ground-truth annotations, calculating precision, recall, and F1
- Interpret evaluation results and identify systematic error patterns in model predictions
- Read, adapt, and debug existing Python code with LLM assistance
- Document model name, version, and parameters in a way that supports reproducible research

#### Prework

Before Day 2, participants should:

- [Set up a Python/Jupyter environment](documents/python_setup.md)
- Download the workshop materials and confirm the `data/` directory is accessible from the notebook

#### Schedule

| Time | Activity |
|------|----------|
| 9:00 – 9:30 | Introduction and Review |
| 9:30 – 10:00 | Coding with LLMs |
| 10:00 – 10:10 | *Break* |
| 10:10 – 10:55 | Case Study: Setup and NER Model |
| 10:55 – 11:15 | Case Study: Full Corpus processing |
| 11:15 – 11:45 | Case Study: Explore Results and Visualize |
| 11:45 – 12:15 | *Lunch* |
| 12:15 – 12:45 | Activity: Ground-Truth Annotation |
| 12:45 – 1:10 | Evaluation |
| 1:10 – 1:20 | *Break* |
| 1:20 – 1:35 | Model Comparison |
| 1:35 – 2:00 | Closing Discussion |

