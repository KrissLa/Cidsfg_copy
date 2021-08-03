from django import template
from loguru import logger

from ..models import Category, Series

register = template.Library()


@register.inclusion_tag('products/template_tags/series_menu.html')
def products_menu():
    """ Категории для меню """
    series = Series.objects.select_related(
        'category'
    ).only(
        'category__name',
        'category__coming_soon',
        'slug',
        'name',
        'picture',
        'active_houses_count',
    ).filter(
        active=True,
        category__active=True
    ).order_by(
        'category__sort_number'
        'sort_number'
    )

    result = []
    for s in series:
        cat_is_not_exist = True
        for i in result:
            if result:
                if s.category.id == i['category_id']:
                    i['series'].append({'series_name': s.name,
                                        'series_picture': s.picture,
                                        'series_get_absolute_url': s.get_absolute_url(),
                                        'series_houses_count': s.active_houses_count})
                    cat_is_not_exist = False
                    break
        if cat_is_not_exist:
            result.append({'category_id': s.category.id,
                           'category_name': s.category.name,
                           'category_coming_soon': s.category.coming_soon,
                           'series': [{'series_name': s.name,
                                       'series_picture': s.picture,
                                       'series_get_absolute_url': s.get_absolute_url(),
                                       'series_houses_count': s.active_houses_count}]})
    return {'data': result}
