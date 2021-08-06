from django import template
from loguru import logger

from ..models import Series, House
from ..services.sorting import sort_series

register = template.Library()


@register.inclusion_tag('products/template_tags/lineup.html')
def lineup():
    """ Модельный ряд """
    houses = House.objects.select_related('series', 'category', 'main_picture').filter(category__active=True,
                                                                                       series__active=True,
                                                                                       active=True).order_by(
        'series__sort_number', 'sort_number',
    ).only('series__name',
           'series__slug',
           'series__sort_number',
           'series__active_houses_count',

           'main_picture__picture',
           'main_picture__alt',

           'category__name',
           'category__slug',

           'name',
           'slug',
           'area',
           'catalog_price',

           )
    series_list = list({house.series for house in houses})
    series_list = sort_series(series_list)

    return {'series_list': series_list,
            'houses': houses}
