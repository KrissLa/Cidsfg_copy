from django import template

from ..models import Contacts

register = template.Library()


@register.inclusion_tag('contacts/template_tags/pre_footer.html')
def pre_footer():
    """ Модельный ряд """
    try:
        contacts = Contacts.objects.all()[0]
    except Exception:
        contacts = None
    return {'contacts': contacts}
