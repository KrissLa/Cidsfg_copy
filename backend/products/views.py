from django.shortcuts import render, get_object_or_404
from django.http import Http404
from itertools import groupby
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View
from loguru import logger

from .models import House, Category, Series


class HouseListView(ListView):
    """ Вывод всех доступных домов в каталог """
    model = House
    template_name = 'products/catalog.html'

    queryset = House.objects.filter(house_active=True).order_by('-id')
    context_object_name = 'houses_list'
    

class HousesListView(ListView):
    """"""
    model = House
    template_name = 'products/catalog.html'

    def get_queryset(self):
        logger.info(self.args)
        self.house_category = get_object_or_404(Category, category_slug=self.args[0])
        self.house_series = get_object_or_404(Series, series_slug=self.args[1])
        logger.info(self.house_category)
        logger.info(self.house_series)
        logger.info(House.objects.filter(house_category=self.house_category, house_series=self.house_series))
        return House.objects.filter(house_category=self.house_category, house_series=self.house_series)


def get_catalog_page(request, slug=None):
    """ Старница с каталогом домомов """
    category = None
    series = None
    houses = House.objects.filter(house_active=True).order_by('house_category', 'house_series')
    categories_list = Category.objects.filter(category_active=True).order_by('id')
    series_list = Series.objects.filter(series_active=True).order_by('id')
    if slug:
        try:
            category = get_object_or_404(Category, category_slug=slug)
        except Http404:
            logger.info('не нашел категорию, приступаю к поиску серии')
            series = get_object_or_404(Series, series_slug=slug)
            houses = houses.filter(house_series=series)
        else:
            houses = houses.filter(house_category=category)

    logger.info(slug)
    logger.info(houses)
    logger.info(categories_list)
    logger.info(series_list)
    logger.info(houses.count())

    return render(request, 'products/catalog.html', {'categories_list': categories_list,
                                                     'series_list': series_list,
                                                     'category': category,
                                                     'series': series,
                                                     'houses': houses})


class CatalogPageView(TemplateView):
    """ Страница с каталогом """
    template_name = 'products/catalog.html'


class ProductDetailPageView(TemplateView):
    """ Страница с детальной информацией о товаре """
    template_name = 'products/product_detail.html'
