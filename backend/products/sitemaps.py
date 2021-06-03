from django.contrib.sitemaps import Sitemap
from .models import House, Series


class CatalogSitemap(Sitemap):
    """ Получение страницы КАТАЛОГ """
    changefreq = 'weekly'
    priority = 0.9
    location = '/catalog/'

    def items(self):
        return House.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated


class SeriesSitemap(Sitemap):
    """ Получение страниц с сериями домов"""
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Series.objects.filter(active=True).order_by('sort_number')

    def lastmod(self, obj):
        return obj.updated


class HouseSitemap(Sitemap):
    """ Получение страниц детальной информацией о доме"""
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return House.objects.filter(active=True).order_by('sort_number')

    def lastmod(self, obj):
        return obj.updated
