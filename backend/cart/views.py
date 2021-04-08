from django.views.generic import TemplateView


class CartView(TemplateView):
    """ Страница корзина """
    template_name = 'cart/cart.html'
