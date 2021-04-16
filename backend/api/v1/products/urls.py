from django.urls import path

from . import views


urlpatterns = [
    path("", views.HouseListAPIView.as_view()),
]