import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

ADMIN_URL = os.environ['ADMIN_URL']

urlpatterns = [
    path(ADMIN_URL + '/', admin.site.urls),
    path('', include('backend.home_page.urls')),
    path('privacy/', include('backend.privacy.urls')),
    path('catalog/', include('backend.products.urls')),
    # path('home_decorations/', include('backend.home_decorations.urls')),
    path('about/', include('backend.about.urls')),
    path('partnership/', include('backend.partnership.urls')),
    path('contacts/', include('backend.contacts.urls')),

    path('api/v1/contacts/', include('backend.api.v1.contacts.urls')),
    # path('api/v1/home_decorations/', include('backend.api.v1.home_decorations.urls')),
    path('api/v1/houses/', include('backend.api.v1.products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = 'CUBO'
admin.site.site_header = 'CUBO'
admin.site.verbose_name = 'Управление сайтом'
