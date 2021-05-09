from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('black/', views.HousesListBlackView.as_view(), name='houses_list'),
    path('', views.HousesListView.as_view(), name='houses_list'),
    path('black/<slug:category_slug>/<slug:series_slug>/<slug:slug>/', views.HouseDetailBlackView.as_view(),
         name='house_detail'),
    path('<slug:category_slug>/<slug:series_slug>/<slug:slug>/', views.HouseDetailView.as_view(), name='house_detail'),
    path('black/<slug:series_slug>/', views.HousesListBlackView.as_view(), name='houses_list_by_series'),
    path('<slug:series_slug>/', views.HousesListView.as_view(), name='houses_list_by_series'),

]
