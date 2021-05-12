from django import template

from ..models import Series, Category

register = template.Library()


@register.inclusion_tag('products/template_tags/series_menu.html')
def products_menu():
    """ Категории для меню """
    category = Category.objects.filter(active=True).order_by('sort_number')
    return {'category': category}

