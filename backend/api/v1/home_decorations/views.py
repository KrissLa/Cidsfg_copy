from backend.apps.home_decorations.models import HomeDecoration
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from .filters import HomeDecorationsFilter
from .serializers import HomeDecorationSerializer


class HomeDecorationsListAPIView(ListAPIView):
    """ Добавление заявки """
    queryset = HomeDecoration.objects.filter(active=True).order_by('type__id')
    model = HomeDecoration
    serializer_class = HomeDecorationSerializer
    filter_backends = [HomeDecorationsFilter, OrderingFilter]
    ordering_fields = ['type', 'id']
