from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HouseListView.as_view(), name='products_catalog'),
    path('<slug:category_slug>/<slug:series_slug>/<slug:slug>/', views.HouseDetailView.as_view(), name='house_detail'),
    # url('<slug:house_category>/<slug:house_series>/', views.HousesListView.as_view(), name='catalog_by_category_and_series'),
    url(r'^([\w-]+)/([\w-]+)/$', views.HousesListView.as_view(), name='catalog_by_category_and_series'),
    # path('<slug:slug>/', views.get_catalog_page, name='catalog_by_category'),
    path('vr_185/', views.ProductDetailPageView.as_view(), name='products_detail'),
    # path('<slug:slug>/', views.),
]
