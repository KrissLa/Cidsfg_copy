from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View


class AboutView(TemplateView):
    """ Страница с каталогом отделок """
    template_name = 'about/about.html'
