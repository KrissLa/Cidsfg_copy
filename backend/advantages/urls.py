from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdvantagesPageView.as_view(), name='advantages'),
]