from django import template

from ..models import Contacts

register = template.Library()


@register.inclusion_tag('contacts/template_tags/pre_footer.html')
def pre_footer():
    """ Модельный ряд """
    try:
        contacts = Contacts.objects.all().only('address_office',
                                               'phone_number_office',
                                               'email_office',
                                               'working_hours_office',
                                               'address',
                                               'phone_number',
                                               'email',
                                               'working_hours',
                                               'map_picture',
                                               'map_link',
                                               'map_picture_footer',
                                               'alt_picture_footer')[0]
    except Exception:
        contacts = None
    return {'contacts': contacts}
