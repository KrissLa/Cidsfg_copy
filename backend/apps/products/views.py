from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from loguru import logger

from .models import House, Series, Catalog, ConfigurationInHouses
from .services.sorting import sort_series


class HouseDetailView(DetailView):
    """ Станица с детальной информацией о доме """
    model = House
    template_name = 'products/product_detail.html'

    category_slug = None
    series_slug = None
    slug = None
    house = None

    def get_object(self, **kwargs):
        self.category_slug = self.kwargs.get('category_slug', '')
        self.series_slug = self.kwargs.get('series_slug', '')
        self.slug = self.kwargs.get('slug', '')
        try:
            house = House.objects.prefetch_related('house_pictures', 'options').get(category__slug=self.category_slug,
                                                                                    category__active=True,
                                                                                    series__slug=self.series_slug,
                                                                                    series__active=True,
                                                                                    slug=self.slug,
                                                                                    active=True)
            self.house = house
            return house
        except House.DoesNotExist:
            raise Http404

    def get_context_data(self, **kwargs):
        data = ConfigurationInHouses.objects.select_related('house',
                                                            'configuration').prefetch_related(
            'configuration__included_in_price',
            'configuration__included_in_price__category',
            'configuration__not_included_in_price',
            'configuration__not_included_in_price__category',
            'included_in_price',
            'included_in_price__category',
            'not_included_in_price',
            'not_included_in_price__category').filter(house__category__slug=self.category_slug,
                                                      house__category__active=True,
                                                      house__series__slug=self.series_slug,
                                                      house__series__active=True,
                                                      house__slug=self.slug,
                                                      house__active=True)

        def get_included_in_price(item):
            if item.category.name not in control_list:
                temp_conf['included_in_price'].append({'addition_category': item.category.name,
                                                       'bodies': [item.body]})
                control_list.append(item.category.name)
            else:
                for i in temp_conf['included_in_price']:
                    if i['addition_category'] == item.category.name:
                        i['bodies'].append(item.body)

        configurations = []
        for conf in data:
            temp_conf = {'configuration_name': conf.configuration.name,
                         'configuration_description': conf.configuration.description,
                         'configuration_id': conf.id,
                         'included_in_price': []}
            if conf.included_in_price.all():
                control_list = []
                for addition in conf.included_in_price.all():
                    get_included_in_price(addition)
            else:
                control_list = []
                for addition in conf.configuration.included_in_price.all():
                    get_included_in_price(addition)
            configurations.append(temp_conf)

        return {'house': self.house,
                'data': data,
                'configurations': configurations}


class HousesListView(ListView):
    """ Страницы каталога с домами """
    model = House
    template_name = 'products/catalog.html'

    series_slug = None
    series_list = None
    series = None
    series_houses = None
    houses = None

    def get_queryset(self, **kwargs):
        self.series_slug = self.kwargs.get('series_slug', '')
        self.houses = House.objects.select_related('series', 'category', 'main_picture').filter(category__active=True,
                                                                                                series__active=True,
                                                                                                active=True).order_by(
            'sort_number').only('series__seo_title',
                                'series__seo_description',
                                'series__seo_og_title',
                                'series__seo_og_image',
                                'series__name',
                                'series__slug',
                                'series__sort_number',
                                'series__active_houses_count',

                                'main_picture__picture',
                                'main_picture__alt',

                                'category__name',
                                'category__slug',

                                'name',
                                'slug',
                                'area',
                                'catalog_price',

                                )
        if self.series_slug:
            self.series_houses = [house for house in self.houses if house.series.slug == self.series_slug]
            if self.series_houses:
                self.series = self.series_houses[0].series
            else:
                raise Http404
        self.series_list = list({house.series for house in self.houses})
        self.series_list = sort_series(self.series_list)
        return self.houses

    def get_context_data(self, **kwargs):
        try:
            catalog_settings = get_object_or_404(Catalog)
        except Http404:
            catalog_settings = None
        return {'catalog_settings': catalog_settings,
                'series_slug': self.series_slug,
                'series_list': self.series_list,
                'series': self.series,
                'all_houses': self.houses,
                'all_houses_count': len(self.houses)}
