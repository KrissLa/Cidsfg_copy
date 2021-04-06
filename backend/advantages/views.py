from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View


class AdvantagesPageView(TemplateView):
    """Главная страница"""
    template_name = 'advantages/advantages.html'
