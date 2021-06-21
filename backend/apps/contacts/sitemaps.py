from django.contrib.sitemaps import Sitemap
from .models import Contacts


class ContactsSitemap(Sitemap):
    """Получение страницы КОНТАКТЫ"""
    changefreq = 'weekly'
    priority = 0.9
    location = '/contacts/'


    def items(self):
        return Contacts.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated

