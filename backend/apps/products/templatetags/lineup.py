from django import template
from loguru import logger

from ..models import Series

register = template.Library()


@register.inclusion_tag('products/template_tags/lineup.html')
def lineup():
    """ Модельный ряд """
    series = Series.objects.prefetch_related('houses',
                                             'houses__main_picture',
                                             'houses__category'
                                             ).filter(active=True,
                                                      houses__active=True
                                                      ).distinct()
    return {'series': series}
