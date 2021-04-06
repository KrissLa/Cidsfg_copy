from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View


class PrivacyPageView(TemplateView):
    """Политика конфиденциальности страница"""
    template_name = 'privacy/privacy.html'