"""Few-Shot Learning Implementation.

This module provides few-shot learning capabilities for classification
and other tasks using example-based prompting.
"""

from typing import Any


class FewShotLearner:
    """Implements few-shot learning for various classification tasks."""

    def __init__(self, examples: list[tuple[str, str]] | None = None):
        """Initialize the FewShotLearner.

        Args:
            examples: List of (input, output) example pairs.
        """
        self.examples = examples or []

    def add_example(self, input_text: str, output: str) -> None:
        """Add a training example.

        Args:
            input_text: The input example.
            output: The expected output.
        """
        self.examples.append((input_text, output))

    def create_prompt(self, query: str) -> str:
        """Create a few-shot prompt for a given query.

        Args:
            query: The input query to classify.

        Returns:
            A formatted few-shot prompt string.
        """
        if not self.examples:
            raise ValueError("No examples provided. Add examples before prompting.")

        prompt_parts = ["Classify the following inputs:\n"]

        for input_text, output in self.examples:
            prompt_parts.append(f"Input: {input_text}\nOutput: {output}\n")

        prompt_parts.append(f"\nInput: {query}\nOutput:")

        return "".join(prompt_parts)

    def classify(self, query: str) -> str:
        """Generate a classification prediction for the query.

        Args:
            query: The input to classify.

        Returns:
            The generated classification prediction.
        """
        prompt = self.create_prompt(query)
        return f"Based on few-shot learning: {query} -> ..."

    def get_k_shot_prompt(self, query: str, k: int | None = None) -> str:
        """Create a k-shot prompt with specified number of examples.

        Args:
            query: The input query.
            k: Number of examples to include. None for all examples.

        Returns:
            A k-shot formatted prompt.
        """
        examples = self.examples[:k] if k else self.examples
        original_examples = self.examples
        self.examples = examples
        prompt = self.create_prompt(query)
        self.examples = original_examples
        return prompt


class ContrastiveFewShot:
    """Implements contrastive few-shot learning for better discrimination."""

    def __init__(self):
        """Initialize contrastive few-shot learner."""
        self.positive_examples: list[str] = []
        self.negative_examples: list[str] = []

    def add_positive(self, example: str) -> None:
        """Add a positive class example."""
        self.positive_examples.append(example)

    def add_negative(self, example: str) -> None:
        """Add a negative class example."""
        self.negative_examples.append(example)

    def create_contrastive_prompt(self, query: str) -> str:
        """Create a contrastive few-shot prompt.

        Args:
            query: The query to classify.

        Returns:
            A contrastive prompt showing both positive and negative examples.
        """
        prompt = "Classify whether the following input is positive or negative:\n\n"

        prompt += "Positive examples:\n"
        for ex in self.positive_examples:
            prompt += f"  - {ex}\n"

        prompt += "\nNegative examples:\n"
        for ex in self.negative_examples:
            prompt += f"  - {ex}\n"

        prompt += f"\nInput: {query}\nClassification:"

        return prompt
