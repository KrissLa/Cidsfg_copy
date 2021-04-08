from django.views.generic import TemplateView


class FavoritesView(TemplateView):
    """ Страница Избранное """
    template_name = 'favorites/favorites.html'