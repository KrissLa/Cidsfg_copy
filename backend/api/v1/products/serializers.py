from rest_framework import serializers

from backend.apps.products.models import House, Category, Series


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
        fields = ('id', 'name', 'category', 'series', 'slug',)
