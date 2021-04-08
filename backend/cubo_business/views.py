from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View


class CuboBusinessView(TemplateView):
    """ Страница CUBO BUSINESS """
    template_name = 'cubo_business/cubo_business.html'