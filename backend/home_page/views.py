from django.shortcuts import render
from django.views import View
from loguru import logger

from .models import HomePage


class HomePageView(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        return render(request, self.template_name, {'home_data': home_data})
