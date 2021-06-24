from django import template
from loguru import logger
from ..models import IndividualProjectRequest

register = template.Library()


@register.filter(name='count_new')
def count_new(model):
    """ Считаем количество новых """
    logger.info(model)
    logger.info(model['object_name'])
    if model['object_name'] == "IndividualProjectRequest":
        number = IndividualProjectRequest.get_new_count()
        if number:
            return f'({number})'
    return ''
