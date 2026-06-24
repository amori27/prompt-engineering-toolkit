"""Chain-of-Thought Prompting Implementation.

This module provides utilities for implementing chain-of-thought prompting
techniques to improve LLM reasoning capabilities.
"""

from typing import Any


class ChainOfThoughtPrompter:
    """Handles chain-of-thought prompting for complex reasoning tasks."""

    def __init__(self, include_intermediate_steps: bool = True):
        """Initialize the ChainOfThoughtPrompter.

        Args:
            include_intermediate_steps: Whether to include intermediate reasoning steps.
        """
        self.include_intermediate_steps = include_intermediate_steps

    def create_reasoning_prompt(self, problem: str, context: list[str] | None = None) -> str:
        """Create a chain-of-thought prompt for a given problem.

        Args:
            problem: The problem statement to reason about.
            context: Optional list of context information.

        Returns:
            A formatted prompt string with chain-of-thought instructions.
        """
        context_section = ""
        if context:
            context_section = "\n".join([f"Context: {ctx}" for ctx in context])
            context_section = f"\n{context_section}\n"

        reasoning_template = f"""Let's solve this step by step.

{context_section}Problem: {problem}

Please follow these steps:
1. Break down the problem into smaller parts
2. Show your reasoning for each step
3. Calculate intermediate results
4. Provide the final answer

Reasoning:"""

        return reasoning_template

    def prompt(self, problem: str, examples: list[str] | None = None) -> str:
        """Generate a chain-of-thought prompt with optional examples.

        Args:
            problem: The main problem to solve.
            examples: Optional list of example problems with solutions.

        Returns:
            A complete prompt string ready for LLM input.
        """
        prompt_parts = []

        if examples:
            prompt_parts.append("Here are some examples of step-by-step reasoning:\n")
            for i, example in enumerate(examples, 1):
                prompt_parts.append(f"Example {i}: {example}\n")

        prompt_parts.append(self.create_reasoning_prompt(problem))

        return "\n".join(prompt_parts)

    def extract_answer(self, response: str) -> str:
        """Extract the final answer from a chain-of-thought response.

        Args:
            response: The LLM response containing reasoning.

        Returns:
            The extracted final answer.
        """
        lines = response.strip().split("\n")
        for line in reversed(lines):
            if "final answer:" in line.lower() or "answer:" in line.lower():
                return line.split(":", 1)[-1].strip()
        return lines[-1] if lines else ""


def create_cot_prompt(problem: str, steps: list[str] | None = None) -> str:
    """Create a chain-of-thought prompt with custom steps.

    Args:
        problem: The problem to solve.
        steps: Optional custom steps to include in the reasoning.

    Returns:
        A formatted chain-of-thought prompt.
    """
    default_steps = [
        "Identify what is being asked",
        "Determine relevant information",
        "Apply appropriate reasoning or calculations",
        "Verify the solution",
    ]
    steps = steps or default_steps

    steps_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)])

    return f"""Problem: {problem}

Follow these reasoning steps:
{steps_text}

Work through each step systematically and show your thinking.

Solution:"""
