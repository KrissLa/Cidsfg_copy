from django import template

from ..models import HomeDecorationCategory

register = template.Library()


@register.inclusion_tag('home_decorations/template_tags/home_decorations_menu.html')
def home_decorations_menu():
    """ Отделка и коммуникации для меню"""
    home_decorations = HomeDecorationCategory.objects.filter(hd_active=True).order_by('id')
    return {'home_decorations': home_decorations}
