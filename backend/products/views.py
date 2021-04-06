from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View


class CatalogPageView(TemplateView):
    """ Страница с каталогом """
    template_name = 'products/catalog.html'


class ProductDetailPageView(TemplateView):
    """ Страница с детальной информацией о товаре """
    template_name = 'products/product_detail.html'