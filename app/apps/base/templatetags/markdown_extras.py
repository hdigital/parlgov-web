"""Template tag to render markdown."""

import markdown as md

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def markdown(value: str) -> str:
    """Render markdown text as html."""
    return md.markdown(value, extensions=["markdown.extensions.fenced_code"])


@register.filter()
@stringfilter
def add_heading(text: str, add_level: str = "##") -> str:
    """Add heading level to Markdown headings."""
    modified_lines = []

    for line in text.split("\n"):
        if line.startswith("#"):
            line = add_level + line
        modified_lines.append(line)

    return "\n".join(modified_lines)
