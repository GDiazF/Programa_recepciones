from django import template

register = template.Library()

@register.filter
def format_money(value):
    try:
        return "{:,.0f}".format(float(value)).replace(",", ".")
    except (ValueError, TypeError):
        return value 