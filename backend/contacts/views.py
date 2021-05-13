from django.shortcuts import render
from django.views.generic import View

from .models import Contacts


class ContactsView(View):
    """ Страница контакты """

    def get(self, request, *args, **kwargs):
        contacts = Contacts.objects.all()[0]
        return render(request, template_name='contacts/contacts.html', context={'contacts': contacts})
