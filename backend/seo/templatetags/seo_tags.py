from django import template
from ..models import CounterForSite, SearchSystem

register = template.Library()

@register.inclusion_tag('template_tags/seo_tags.html')
def all_counters():
    counters = CounterForSite.objects.filter(active=True)
    return {'counters':counters}


@register.inclusion_tag('template_tags/seo_tags.html')
def all_ss():
    ss = SearchSystem.objects.filter(active=True)
    return {'ss':ss}
