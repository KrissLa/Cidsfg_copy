from django.urls import path, include

urlpatterns = [
    path('contact_forms/', include('backend.api.v1.contact_forms.urls')),
]