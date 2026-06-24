"""Utility functions for the Prompt Engineering Toolkit."""

import re
from typing import Any


def extract_json_from_response(response: str) -> dict[str, Any] | None:
    """Extract JSON from an LLM response that may contain extra text.

    Args:
        response: The raw response text.

    Returns:
        Parsed JSON dictionary or None if parsing fails.
    """
    import json

    json_patterns = [
        r'\{[^{}]*\}',
        r'```json\s*([\s\S]*?)\s*```',
        r'```\s*([\s\S]*?)\s*```',
    ]

    for pattern in json_patterns:
        match = re.search(pattern, response)
        if match:
            try:
                json_str = match.group(1) if match.lastindex else match.group(0)
                return json.loads(json_str)
            except json.JSONDecodeError:
                continue

    return None


def clean_response(response: str) -> str:
    """Clean and normalize an LLM response.

    Args:
        response: The raw response text.

    Returns:
        Cleaned response string.
    """
    response = response.strip()
    response = re.sub(r'\n{3,}', '\n\n', response)
    return response


def count_tokens_approximate(text: str) -> int:
    """Approximate token count for a text string.

    Args:
        text: Input text.

    Returns:
        Approximate number of tokens.
    """
    words = text.split()
    return int(len(words) * 1.3)


def truncate_prompt(prompt: str, max_tokens: int = 4000) -> str:
    """Truncate a prompt to fit within a maximum token limit.

    Args:
        prompt: The input prompt.
        max_tokens: Maximum allowed tokens.

    Returns:
        Truncated prompt string.
    """
    current_tokens = count_tokens_approximate(prompt)
    if current_tokens <= max_tokens:
        return prompt

    words = prompt.split()
    target_words = int(max_tokens / 1.3)
    truncated = ' '.join(words[:target_words])

    return truncated + "\n\n[Truncated due to length]"
