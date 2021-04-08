import os
from django.contrib import admin
from django.urls import path, include

ADMIN_URL = os.environ['ADMIN_URL']

urlpatterns = [
    path(ADMIN_URL + '/', admin.site.urls),
    path('', include('backend.home_page.urls')),
    path('advantages/', include('backend.advantages.urls')),
    path('privacy/', include('backend.privacy.urls')),
    path('catalog/', include('backend.products.urls')),
    path('home_decorations/', include('backend.home_decorations.urls')),
    path('about/', include('backend.about.urls')),

    path('api/v1/orders/', include('backend.api.v1.orders.urls')),
]
