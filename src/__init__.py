"""Prompt Engineering Toolkit - Core Module."""

from .cot_prompter import ChainOfThoughtPrompter
from .few_shot_learning import FewShotLearner
from .prompt_templates import (
    create_classification_template,
    create_extraction_template,
    create_summarization_template,
)

__all__ = [
    "ChainOfThoughtPrompter",
    "FewShotLearner",
    "create_classification_template",
    "create_extraction_template",
    "create_summarization_template",
]
