from django import template
from loguru import logger

from ..models import Series, Category

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
    ).exclude(active_houses_count=0).order_by(
        'category__sort_number',
        'sort_number'
    )
    coming_soon_categories = Category.objects.filter(coming_soon=True).only('id', 'name', 'coming_soon')


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
    for cat in coming_soon_categories:
        if cat.id not in [i['category_id'] for i in result]:
            result.append({'category_id': cat.id,
                           'category_name': cat.name,
                           'category_coming_soon': cat.coming_soon,
                           'series': []})
    logger.info(result)

    return {'data': result}
