from backend.orders.models import Order
from loguru import logger
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import OrderSerializer
from .services import send_notification


class OrderCreateAPIView(CreateAPIView):
    """ Добавление заявки """
    queryset = Order.objects.none()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_notification(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)