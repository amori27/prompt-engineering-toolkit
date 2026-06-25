# Prompt Engineering Toolkit
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


A comprehensive toolkit for advanced prompt engineering techniques including chain-of-thought reasoning, few-shot learning, and template-based prompt generation.

## Description

This toolkit provides reusable components and templates for building sophisticated AI prompts. It implements industry-best practices for maximizing LLM performance across various tasks including reasoning, classification, and content generation.

## Skills & Technologies

- Python 3.9+
- Chain-of-Thought (CoT) Prompting
- Few-Shot Learning
- Template-based Prompt Engineering
- OpenAI/Anthropic API Integration
- LangChain

## Installation

```bash
git clone https://github.com/amori27/prompt-engineering-toolkit.git
cd prompt-engineering-toolkit
pip install -r requirements.txt
```

## Usage

### Chain of Thought Prompting

```python
from src.cot_prompter import ChainOfThoughtPrompter

prompter = ChainOfThoughtPrompter()
result = prompter.prompt(
    problem="If a train travels 120km in 2 hours, what is its speed?",
    examples=["Example: 50km in 1hr = 50km/hr"]
)
print(result)
```

### Few-Shot Learning

```python
from src.few_shot_learning import FewShotLearner

learner = FewShotLearner(examples=[
    ("Input: Happy", "Output: Positive"),
    ("Input: Sad", "Output: Negative"),
])
result = learner.classify("Input: Excited")
```

### Template-Based Prompts

```python
from src.prompt_templates import create_classification_template

template = create_classification_template(
    categories=["positive", "negative", "neutral"],
    include_reasoning=True
)
```

## Project Structure

```
prompt-engineering-toolkit/
├── src/
│   ├── __init__.py
│   ├── cot_prompter.py       # Chain-of-thought implementation
│   ├── few_shot_learning.py  # Few-shot learning patterns
│   ├── prompt_templates.py   # Reusable prompt templates
│   └── utils.py              # Utility functions
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## References

- [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903)
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## License

MIT License
