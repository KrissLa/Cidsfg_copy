from django import template

register = template.Library()


@register.filter(name='count_active')
def count_active(value):
    """ Считаем количество только активных """
    return value.filter(active=True).count()
