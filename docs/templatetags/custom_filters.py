from django import template

register = template.Library()

@register.filter
def format_money(value):
    try:
        return "{:,.0f}".format(float(value)).replace(",", ".")
    except (ValueError, TypeError):
        return value

@register.filter
def has_permission(user, permission):
    """
    Verifica si el usuario tiene un permiso específico
    Uso en template: {% if user|has_permission:'docs.Acceso_a_reportes' %}
    """
    if user and user.is_authenticated:
        return user.has_perm(permission)
    return False 