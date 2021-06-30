from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from backend.apps.contact_forms.models import IndividualProjectRequest, Message, ConsultationRequest, \
    CooperationApplication
from .serializers import IndividualProjectRequestSerializer, MessageSerializer, ConsultationRequestSerializer, \
    CooperationApplicationSerializer
from ..services.telegram.notifications import send_notification
from ..services.telegram.data_transformation import unique_project_update_data, contact_message_update_data, \
    consultation_request_update_data, partnership_update_data

from ..services.texts.notifications import unique_project_text, contact_message_text, consultation_request_text, \
    partnership_text


class CreateSendNotificationAPIView(CreateAPIView):
    """ Добавляем отправку оповещения в метод create """
    message_text = None
    data_validator = None

    def send_notification(self, data):
        send_notification(data, self.message_text, self.data_validator)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        self.send_notification(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class IndividualProjectRequestCreateAPIView(CreateSendNotificationAPIView):
    """ Создание заявки на индивидуальный проект """
    queryset = IndividualProjectRequest.objects.none()
    serializer_class = IndividualProjectRequestSerializer
    message_text = unique_project_text
    data_validator = unique_project_update_data


class MessageCreateAPIView(CreateSendNotificationAPIView):
    """ Добавление сообщения """
    queryset = Message.objects.none()
    serializer_class = MessageSerializer
    message_text = contact_message_text
    data_validator = contact_message_update_data


class ConsultationRequestCreateAPIView(CreateSendNotificationAPIView):
    """ Добавление заявки на консультацию """
    queryset = ConsultationRequest.objects.none()
    serializer_class = ConsultationRequestSerializer
    message_text = consultation_request_text
    data_validator = consultation_request_update_data


class CooperationApplicationCreateAPIView(CreateSendNotificationAPIView):
    """ Добавление заявки на сотрудничество """
    queryset = CooperationApplication.objects.none()
    serializer_class = CooperationApplicationSerializer
    message_text = partnership_text
    data_validator = partnership_update_data
