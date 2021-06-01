from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View
from loguru import logger

from config.settings import SITE_DOMAIN
from .models import Privacy


# class PrivacyPageView(TemplateView):
#     """Политика конфиденциальности страница"""
#     template_name = 'privacy/privacy.html'


class PrivacyPageView(View):
    """ Политика конфиденциальности страница """
    model = Privacy
    template_name = 'privacy/privacy.html'

    def get(self, request, *args, **kwargs):
        num_data = 3
        try:
            privacy_data = Privacy.objects.all().order_by('-id')[0]
            if privacy_data.data.count():
                num_data = privacy_data.data.count()
        except Exception:
            privacy_data = None
        return render(request, self.template_name, {'privacy_data': privacy_data,
                                                    'site_domain': SITE_DOMAIN,
                                                    'num_data': num_data})
