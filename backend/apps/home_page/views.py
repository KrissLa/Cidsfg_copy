from django.shortcuts import render
from django.views import View

from .models import HomePage


class HomePageView(View):
    """Главная страница"""
    model = HomePage
    template_name = 'home_page/home.html'

    def get(self, request, *args, **kwargs):
        try:
            home_data = HomePage.objects.last()
        except Exception:
            home_data = None
        return render(request, self.template_name, {'home_data': home_data})
