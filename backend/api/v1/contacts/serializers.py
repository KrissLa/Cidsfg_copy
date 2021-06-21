from rest_framework import serializers

from backend.apps.contacts.models import Message


class MessageSerializer(serializers.ModelSerializer):
    """ Сериализация сообщений со страницы контакты """
    class Meta:
        model = Message
        fields = "__all__"