from django.contrib.sitemaps import Sitemap
from .models import About


class AboutSitemap(Sitemap):
    """Получение страницы ЗАВОД"""
    changefreq = 'weekly'
    priority = 0.9
    location = '/about/'

    def items(self):
        return About.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated
