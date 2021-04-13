from backend.home_decorations.models import HomeDecoration, HomeDecorationCategory, HomeDecorationSubCategory, \
    HomeDecorationType
from django.shortcuts import get_list_or_404
from loguru import logger
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .filters import HomeDecorationsFilter
from .serializers import HomeDecorationSerializer


class HomeDecorationsListAPIView(ListAPIView):
    """ Добавление заявки """
    queryset = HomeDecoration.objects.filter(active=True)
    model = HomeDecoration
    serializer_class = HomeDecorationSerializer
    filter_backends = [HomeDecorationsFilter, OrderingFilter]
    ordering_fields = ['type', 'id']




