from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomeDecorationsListView.as_view(), name='home_decorations_list'),
    path("deco/", views.HomeDecorationsDetailView.as_view(), name='home_decorations_detail'),
]