from django import template
from ..models import IndividualProjectRequest, ConsultationRequest, CooperationApplication, Message

register = template.Library()


@register.filter(name='count_new')
def count_new(model):
    """ Считаем количество новых """
    if model['object_name'] == "IndividualProjectRequest":
        number = IndividualProjectRequest.get_new_count()
        if number:
            return f'({number})'
    elif model['object_name'] == "ConsultationRequest":
        number = ConsultationRequest.get_new_count()
        if number:
            return f'({number})'
    elif model['object_name'] == "CooperationApplication":
        number = CooperationApplication.get_new_count()
        if number:
            return f'({number})'
    elif model['object_name'] == "Message":
        number = Message.get_new_count()
        if number:
            return f'({number})'
    return ''
