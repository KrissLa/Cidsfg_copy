from rest_framework import status
from rest_framework.response import Response

from backend.products.models import House, ConsultationRequest
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView

from .filters import CategoryFilter, SeriesFilter
from .serializers import HouseSerializer, ConsultationRequestSerializer
from .services import send_notification


class ConsultationRequestCreateAPIView(CreateAPIView):
    """ Добавление сообщения """
    queryset = ConsultationRequest.objects.none()
    serializer_class = ConsultationRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_notification(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class HouseListAPIView(ListAPIView):
    """ Список домов """
    queryset = House.objects.filter(active=True).order_by('id')
    model = House
    serializer_class = HouseSerializer
    filter_backends = [CategoryFilter, SeriesFilter, OrderingFilter]
    ordering_fields = ['id', ]
