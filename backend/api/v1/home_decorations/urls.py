from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomeDecorationsListAPIView.as_view()),
]