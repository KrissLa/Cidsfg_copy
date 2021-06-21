from django import template

from ..models import Series

register = template.Library()


@register.inclusion_tag('products/template_tags/lineup.html')
def lineup():
    """ Модельный ряд """
    series = Series.objects.filter(active=True).exclude(houses=None).order_by('sort_number')
    return {'series': series}
