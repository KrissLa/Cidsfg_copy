from django.views.generic import TemplateView


class ContactsView(TemplateView):
    """ Страница контакты """
    template_name = 'contacts/contacts.html'