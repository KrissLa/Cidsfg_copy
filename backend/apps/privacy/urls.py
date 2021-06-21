from django.urls import path

from . import views


urlpatterns = [
    path("", views.PrivacyPageView.as_view(), name='privacy'),
]
