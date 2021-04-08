from django.views.generic import TemplateView


class PartnershipView(TemplateView):
    """ Страничка сотрудничество """
    template_name = 'partnership/partnership.html'