from django import template
from backend.services.price_to_str import price_to_str
register = template.Library()


@register.filter(name='price_to_str_filter')
def price_to_str_filter(value):
    """ Добавляем пробелы в шаблоне """
    return price_to_str(value)
