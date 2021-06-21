from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import House, Series, Catalog


class HouseDetailView(DetailView):
    """ Станица с детальной информацией о доме """
    model = House
    template_name = 'products/product_detail.html'
    context_object_name = 'house'

    def get_object(self, **kwargs):
        category_slug = self.kwargs.get('category_slug', '')
        series_slug = self.kwargs.get('series_slug', '')
        slug = self.kwargs.get('slug', '')
        house = get_object_or_404(House,
                                  category__slug=category_slug,
                                  category__active=True,
                                  series__slug=series_slug,
                                  series__active=True,
                                  slug=slug,
                                  active=True)
        return house


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
