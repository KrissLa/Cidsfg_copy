from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import House, Series, Catalog, ConfigurationInHouses


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
    context_object_name = 'houses'

    def get_queryset(self, **kwargs):
        series_slug = self.kwargs.get('series_slug', '')
        if series_slug:
            series = get_object_or_404(Series, slug=series_slug, active=True)
            houses = House.objects.filter(category__active=True,
                                          series=series,
                                          active=True).order_by('sort_number')
        else:
            houses = House.objects.filter(category__active=True,
                                          series__active=True,
                                          active=True).order_by('sort_number')
        return houses

    def get_context_data(self, **kwargs):
        series_slug = self.kwargs.get('series_slug', '')
        series_list = Series.objects.filter(active=True)
        try:
            series = get_object_or_404(Series, slug=series_slug, active=True)
        except Exception:
            series = None
        try:
            catalog_settings = get_object_or_404(Catalog)
        except Exception:
            catalog_settings = None
        return {'catalog_settings': catalog_settings,
                'series_slug': series_slug,
                'series_list': series_list,
                'series': series,
                'all_houses': House.objects.filter(category__active=True,
                                                   series__active=True,
                                                   active=True).order_by('sort_number')}
