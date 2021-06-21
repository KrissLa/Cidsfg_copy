from django.urls import path

from . import views


urlpatterns = [
    path('', views.PartnershipView.as_view(), name='partnership'),
]
