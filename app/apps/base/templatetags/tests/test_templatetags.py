from datetime import date

import pytest

from django.template import Context, Template


def test_markdown_template_tag():
    context = Context({"title": "# Title"})
    template_to_render = Template(
        "{% load markdown_extras %}" "{{ title|markdown|safe }}"
    )
    rendered_template = template_to_render.render(context)
    assert rendered_template == "<h1>Title</h1>"


def test_markdown_add_header():
    context = Context({"title": "# Title"})
    template_to_render = Template(
        "{% load markdown_extras %}" "{{ title|add_heading|markdown|safe }}"
    )
    rendered_template = template_to_render.render(context)
    assert rendered_template == "<h3>Title</h3>"


def test_ymd_date():
    context = Context({"date": date(2000, 1, 1)})
    template_to_render = Template(
        "{% load format_data %}" "{{ date|ymd_remove_07_01 }}"
    )
    rendered_template = template_to_render.render(context)
    assert rendered_template == "2000-01-01"


def test_ymd_date_remove():
    context = Context({"date": date(2000, 7, 1)})
    template_to_render = Template(
        "{% load format_data %}" "{{ date|ymd_remove_07_01 }}"
    )
    rendered_template = template_to_render.render(context)

    assert rendered_template != "2000-07-01"
    assert rendered_template == "2000"


@pytest.mark.parametrize(
    "number, rounded",
    [
        [-190, -200],
        [26.6, 0],
        [80.1, 100],
        [1730, 1700],
    ],
)
def test_round_100_tag(number, rounded):
    context = Context({"number": number})
    template_to_render = Template("{% load format_data %}" "{{ number|round_100 }}")
    rendered_template = template_to_render.render(context)
    assert rendered_template == f"{rounded}"


def test_wikipedia_title_tag():
    context = Context({"wikipedia": "https://en.wikipedia.org/wiki/ANO_2011"})
    template_to_render = Template(
        "{% load format_data %}" "{{ wikipedia|wikipedia_title }}"
    )
    rendered_template = template_to_render.render(context)
    assert rendered_template == "ANO 2011"
