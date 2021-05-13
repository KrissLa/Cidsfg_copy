from rest_framework import serializers

from backend.products.models import House, Category, Series, ConsultationRequest


class ConsultationRequestSerializer(serializers.ModelSerializer):
    """ Сериализация заявки на консультацию """
    class Meta:
        model = ConsultationRequest
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """ Сериализация модели категории дома """

    class Meta:
        model = Category
        fields = ('name', 'get_absolute_url')


class SeriesSerializer(serializers.ModelSerializer):
    """ Сериализация модели серии дома """

    class Meta:
        model = Series
        fields = ('name', 'get_absolute_url')



class HouseSerializer(serializers.ModelSerializer):
    """ Сериализация модели дома """
    category = CategorySerializer()
    series = SeriesSerializer()

    class Meta:
        model = House
        fields = ('id', 'name', 'category', 'series', 'slug', )
