from django.shortcuts import render
from django.views import View
from loguru import logger

from .models import About


class AboutView(View):
    """ Страница с информацией о компании """
    model = About
    template_name = 'about/about.html'

    def get(self, request, *args, **kwargs):
        try:
            about = About.objects.all().order_by('-id')[0]
        except Exception:
            about = None
        return render(request, self.template_name, {'about': about})
