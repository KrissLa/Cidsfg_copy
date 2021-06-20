from django.shortcuts import render
from django.views import View

from .models import Partnership


class PartnershipView(View):
    """ Страничка сотрудничество """

    def get(self, request, *args, **kwargs):
        try:
            partnership = Partnership.objects.all()[0]
        except Exception:
            partnership = None
        return render(request, template_name='partnership/partnership.html', context={'partnership': partnership})
