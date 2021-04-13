from rest_framework import serializers

from backend.home_decorations.models import HomeDecoration


class HomeDecorationSerializer(serializers.ModelSerializer):
    """ Сериализация вариантов отделок """
    class Meta:
        model = HomeDecoration
        fields = "__all__"