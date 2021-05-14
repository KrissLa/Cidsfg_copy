from django.shortcuts import render
from django.views.generic import View

from .models import Contacts


class ContactsView(View):
    """ Страница контакты """

    def get(self, request, *args, **kwargs):
        try:
            contacts = Contacts.objects.all()[0]
        except Exception:
            contacts = None
        return render(request, template_name='contacts/contacts.html', context={'contacts': contacts})
