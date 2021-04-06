from django.urls import path

from . import views


urlpatterns = [
    path("", views.CatalogPageView.as_view(), name='products_catalog'),
    path("vr_185/", views.ProductDetailPageView.as_view(), name='products_detail'),
]