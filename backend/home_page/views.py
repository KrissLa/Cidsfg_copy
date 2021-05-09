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


class HomePageView5(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home_5x.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})

class HomePageView6(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home_6x.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})

class HomePageView7(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home_7x.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})

class HomePageView8(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home_8x.html'

    def get(self, request, *args, **kwargs):
        home_data = HomePage.objects.all().order_by('-id')[:1].values()[0]
        logger.info(home_data)
        return render(request, self.template_name, {'home_data': home_data})
