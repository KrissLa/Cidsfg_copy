from django.contrib.sitemaps import Sitemap
from .models import Privacy


class PrivacySitemap(Sitemap):
    """ Получение страницы ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ """
    changefreq = 'weekly'
    priority = 0.9
    location = '/privacy/'


    def items(self):
        return Privacy.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated

