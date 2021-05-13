from django import template

from ..models import Contacts

register = template.Library()


@register.inclusion_tag('contacts/template_tags/pre_footer.html')
def pre_footer():
    """ Модельный ряд """
    contacts = Contacts.objects.all()[0]
    return {'contacts': contacts}
