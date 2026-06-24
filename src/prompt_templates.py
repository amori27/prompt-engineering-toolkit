"""Prompt Templates for Common Tasks.

This module provides reusable prompt templates for classification,
extraction, summarization, and other common LLM tasks.
"""

from typing import Any


def create_classification_template(
    categories: list[str],
    include_reasoning: bool = False,
    task_description: str = "Classify the following input"
) -> str:
    """Create a classification prompt template.

    Args:
        categories: List of valid category labels.
        include_reasoning: Whether to request reasoning in the response.
        task_description: Custom task description.

    Returns:
        A formatted classification prompt template.
    """
    categories_str = ", ".join(categories)
    reasoning_section = "\nProvide your reasoning before giving the final answer." if include_reasoning else ""

    return f"""{task_description}.

Available categories: {categories_str}.{reasoning_section}

Input: {{input}}
Category:"""


def create_extraction_template(
    fields: list[str],
    task_description: str = "Extract information"
) -> str:
    """Create an information extraction prompt template.

    Args:
        fields: List of fields to extract.
        task_description: Custom task description.

    Returns:
        A formatted extraction prompt template.
    """
    fields_list = "\n".join([f"  - {field}" for field in fields])
    fields_str = ", ".join(fields)

    return f"""{task_description}.

Extract the following fields: {fields_str}
Format your response as a structured JSON object.

{fields_list}

Input: {{input}}

Extracted Information:"""


def create_summarization_template(
    max_length: int | None = None,
    style: str = "concise",
    focus: str | None = None
) -> str:
    """Create a summarization prompt template.

    Args:
        max_length: Maximum length of summary in words/sentences.
        style: Summarization style (concise, detailed, bullet_points).
        focus: Optional focus area for the summary.

    Returns:
        A formatted summarization prompt template.
    """
    length_instruction = f"Keep the summary to no more than {max_length} sentences." if max_length else ""

    style_instructions = {
        "concise": "Provide a clear, brief summary covering only the key points.",
        "detailed": "Provide a comprehensive summary covering all important details.",
        "bullet_points": "Use bullet points to organize the key information.",
    }

    style_instruction = style_instructions.get(style, style_instructions["concise"])
    focus_instruction = f"Focus particularly on: {focus}" if focus else ""

    return f"""Summarize the following text.

{length_instruction}
{style_instruction}
{focus_instruction}

Text: {{input}}

Summary:"""


def create_translation_template(
    target_language: str,
    preserve_formatting: bool = True
) -> str:
    """Create a translation prompt template.

    Args:
        target_language: The language to translate into.
        preserve_formatting: Whether to preserve original formatting.

    Returns:
        A formatted translation prompt template.
    """
    formatting_instruction = (
        "Preserve the original formatting, including paragraphs and line breaks."
        if preserve_formatting
        else "You may restructure the text for natural flow in the target language."
    )

    return f"""Translate the following text into {target_language}.
{formatting_instruction}

Original text: {{input}}

Translation:"""


def create_code_generation_template(
    language: str,
    include_comments: bool = True,
    handle_errors: bool = True
) -> str:
    """Create a code generation prompt template.

    Args:
        language: Programming language for the code.
        include_comments: Whether to include code comments.
        handle_errors: Whether to include error handling.

    Returns:
        A formatted code generation prompt template.
    """
    comment_instruction = "Include clear comments explaining the code." if include_comments else ""
    error_instruction = "Include appropriate error handling." if handle_errors else ""

    return f"""Generate {language} code that accomplishes the following task.
{comment_instruction}
{error_instruction}

Task: {{input}}

Code:"""


def create_question_answering_template(
    context_key: str = "context",
    answer_format: str = "direct"
) -> str:
    """Create a question answering prompt template.

    Args:
        context_key: Key name for the context variable.
        answer_format: Format for answers (direct, detailed, bullet_points).

    Returns:
        A formatted question answering prompt template.
    """
    format_instructions = {
        "direct": "Give a direct, brief answer.",
        "detailed": "Provide a detailed explanation.",
        "bullet_points": "Use bullet points to organize your answer.",
    }

    format_instruction = format_instructions.get(answer_format, format_instructions["direct"])

    return f"""Answer the question based on the provided context.

{format_instruction}

{context_key}:
{{context}}

Question: {{question}}

Answer:"""
