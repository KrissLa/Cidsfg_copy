import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from backend.apps.about.sitemaps import AboutSitemap
from backend.apps.contacts.sitemaps import ContactsSitemap
from backend.apps.home_page.sitemaps import HomePageSitemap
from backend.apps.partnership.sitemaps import PartnershipSitemap
from backend.apps.privacy.sitemaps import PrivacySitemap
from backend.apps.products.sitemaps import CatalogSitemap, SeriesSitemap, HouseSitemap

ADMIN_URL = os.environ['ADMIN_URL']


sitemaps = {'home': HomePageSitemap,
            'about': AboutSitemap,
            'contacts': ContactsSitemap,
            'partnership': PartnershipSitemap,
            'privacy': PrivacySitemap,
            'catalog': CatalogSitemap,
            'series': SeriesSitemap,
            'houses': HouseSitemap}

urlpatterns = [
    path('nobots/' + ADMIN_URL + '/', admin.site.urls),

    path('nobots/api/v1/partnership/', include('backend.api.v1.partnership.urls')),
    path('nobots/api/v1/', include('backend.api.v1.config.urls')),
    path('', include('backend.apps.config.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'CUBO'
admin.site.site_header = 'CUBO'
admin.site.verbose_name = 'Управление сайтом'
