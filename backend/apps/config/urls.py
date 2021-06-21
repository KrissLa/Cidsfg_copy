from django.urls import path, include

urlpatterns = [
    path('', include('backend.apps.home_page.urls')),
    path('about/', include('backend.apps.about.urls')),
    path('contacts/', include('backend.apps.contacts.urls')),
    path('privacy/', include('backend.apps.privacy.urls')),
    path('partnership/', include('backend.apps.partnership.urls')),
    path('catalog/', include('backend.apps.products.urls')),
]
