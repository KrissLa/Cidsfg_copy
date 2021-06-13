from rest_framework import serializers

from backend.apps.contact_forms.models import IndividualProjectRequest


class IndividualProjectRequestSerializer(serializers.ModelSerializer):
    """ Сериализация заявок на индивидуальный проект """
    class Meta:
        model = IndividualProjectRequest
        fields = "__all__"