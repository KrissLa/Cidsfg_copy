from django import template

from config.settings import SITE_DOMAIN

register = template.Library()


@register.inclusion_tag('template_tags/domain.html')
def domain():
    """ domain """
    return {'domain': SITE_DOMAIN}
