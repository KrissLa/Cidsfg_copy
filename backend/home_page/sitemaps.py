from django.contrib.sitemaps import Sitemap
from .models import HomePage


class HomePageSitemap(Sitemap):
    """Получение главной страницы"""
    changefreq = 'weekly'
    priority = 0.9
    location = '/'

    def items(self):
        return HomePage.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated
