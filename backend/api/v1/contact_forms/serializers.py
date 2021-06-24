from rest_framework import serializers

from backend.apps.contact_forms.models import IndividualProjectRequest, Message


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