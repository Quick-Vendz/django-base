import markdown as mdp

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def markdown(value):
    md = mdp.Markdown(extensions=["fenced_code"])
    html = md.convert(value)
    wrapped = f'<div class="markdown">{html}</div>'
    return mark_safe(wrapped)