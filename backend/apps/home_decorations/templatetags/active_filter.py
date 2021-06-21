from django import template

register = template.Library()


@register.filter(name='active_filter')
def active_filter(value):
    """ Фильтрация только актывных """
    return value.filter(active=True).order_by('id')
