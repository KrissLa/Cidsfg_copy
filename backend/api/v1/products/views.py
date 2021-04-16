from backend.products.models import House
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from .filters import CategoryFilter, SeriesFilter
from .serializers import HouseSerializer


class HouseListAPIView(ListAPIView):
    """ Список домов """
    queryset = House.objects.filter(active=True).order_by('id')
    model = House
    serializer_class = HouseSerializer
    filter_backends = [CategoryFilter, SeriesFilter, OrderingFilter]
    ordering_fields = ['id', ]
