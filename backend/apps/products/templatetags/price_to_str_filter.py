from django import template

register = template.Library()


@register.filter(name='price_to_str_filter')
def price_to_str_filter(value):
    """ Добавляем пробелы в шаблоне """
    list_value = list(str(value))
    list_value.reverse()
    if len(list_value) > 3:
        list_value.insert(3, ' ')
    if len(list_value) > 6:
        list_value.insert(7, ' ')
    list_value.reverse()
    return ''.join(list_value)
