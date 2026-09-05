# Prompt Engineering Toolkit

Chain-of-thought, few-shot, and template-based prompting patterns for LLMs — reusable Python components with OpenAI/Anthropic integration.

## Usage

```python
from src.cot_prompter import ChainOfThoughtPrompter
prompter = ChainOfThoughtPrompter()
result = prompter.prompt(
    problem="If a train travels 120km in 2 hours, what is its speed?",
    examples=["Example: 50km in 1hr = 50km/hr"]
)
print(result)
```

```python
from src.few_shot_learning import FewShotLearner
learner = FewShotLearner(examples=[
    ("Input: Happy", "Output: Positive"),
    ("Input: Sad", "Output: Negative"),
])
result = learner.classify("Input: Excited")
```

## License

MIT
