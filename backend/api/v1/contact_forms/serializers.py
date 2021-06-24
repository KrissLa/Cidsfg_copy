from rest_framework import serializers

from backend.apps.contact_forms.models import IndividualProjectRequest, Message, ConsultationRequest


class IndividualProjectRequestSerializer(serializers.ModelSerializer):
    """ Сериализация заявок на индивидуальный проект """
    class Meta:
        model = IndividualProjectRequest
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    """ Сериализация сообщений со страницы контакты """
    class Meta:
        model = Message
        fields = "__all__"


class ConsultationRequestSerializer(serializers.ModelSerializer):
    """ Сериализация заявки на консультацию """
    class Meta:
        model = ConsultationRequest
        fields = "__all__"
