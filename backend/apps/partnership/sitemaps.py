from django.contrib.sitemaps import Sitemap
from .models import Partnership


class PartnershipSitemap(Sitemap):
    """Получение страницы СОТРУДНИЧЕСТВО"""
    changefreq = 'weekly'
    priority = 0.9
    location = '/partnership/'


    def items(self):
        return Partnership.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated

