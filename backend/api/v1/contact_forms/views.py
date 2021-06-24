from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from backend.apps.contact_forms.models import IndividualProjectRequest, Message, ConsultationRequest
from .serializers import IndividualProjectRequestSerializer, MessageSerializer, ConsultationRequestSerializer
from .services import send_notification, send_notification_message, send_notification_consultation


class IndividualProjectRequestCreateAPIView(CreateAPIView):
    """ Создание заявки на индивидуальный проект """
    queryset = IndividualProjectRequest.objects.none()
    serializer_class = IndividualProjectRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_notification(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MessageCreateAPIView(CreateAPIView):
    """ Добавление сообщения """
    queryset = Message.objects.none()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_notification_message(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ConsultationRequestCreateAPIView(CreateAPIView):
    """ Добавление заявки на консультацию """
    queryset = ConsultationRequest.objects.none()
    serializer_class = ConsultationRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_notification_consultation(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
