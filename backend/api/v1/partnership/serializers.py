from rest_framework import serializers

from backend.apps.partnership.models import CooperationApplication


class CooperationApplicationSerializer(serializers.ModelSerializer):
    """ Сериализация заявок на сотрудничество """
    class Meta:
        model = CooperationApplication
        fields = "__all__"