from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from backend.contacts.models import Message
from .serializers import MessageSerializer
from .services import send_notification


class MessageCreateAPIView(CreateAPIView):
    """ Добавление сообщения """
    queryset = Message.objects.none()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_notification(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
