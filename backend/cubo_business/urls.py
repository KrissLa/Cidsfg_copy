from django.urls import path

from . import views

urlpatterns = [
    path('', views.CuboBusinessView.as_view(), name='cubo_business'),
]