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
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})

class HomePage075View(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home_075.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})

class HomePage1View(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home_1s.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})


class HomePageBlackView(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home_black.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})


class HomePageView2(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home_2_my.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})
