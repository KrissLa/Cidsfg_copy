from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View


class HomeDecorationsListView(TemplateView):
    """ Страница с каталогом отделок """
    template_name = 'home_decorations/home_decorations_list.html'


class HomeDecorationsDetailView(TemplateView):
    """ Страница с подробным отписание об отделке """
    template_name = 'home_decorations/home_decorations_detail.html'