from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HousesListView.as_view(), name='houses_list'),
    path('<slug:category_slug>/<slug:series_slug>/<slug:slug>/', views.HouseDetailView.as_view(), name='house_detail'),
    path('<slug:series_slug>/', views.HousesListView.as_view(), name='houses_list_by_series'),

]
