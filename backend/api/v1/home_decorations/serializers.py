from rest_framework import serializers

from backend.apps.home_decorations.models import HomeDecoration, HomeDecorationType, HomeDecorationSubCategory, \
    HomeDecorationCategory


class HomeDecorationCategorySerializer(serializers.ModelSerializer):
    """ Сериализация подкатегорий отделки """

    class Meta:
        model = HomeDecorationCategory
        fields = ('hd_name', 'get_absolute_url')


class HomeDecorationSubCategorySerializer(serializers.ModelSerializer):
    """ Сериализация подкатегорий отделки """
    category = HomeDecorationCategorySerializer()
    class Meta:
        model = HomeDecorationSubCategory
        fields = ('name', 'get_absolute_url', 'category')


class HomeDecorationTypeSerializer(serializers.ModelSerializer):
    """ Сериализация видов отделки """
    sub_category = HomeDecorationSubCategorySerializer()

    class Meta:
        model = HomeDecorationType
        fields = ('name', 'get_absolute_url', 'sub_category')


class HomeDecorationSerializer(serializers.ModelSerializer):
    """ Сериализация вариантов отделок """
    type = HomeDecorationTypeSerializer()

    class Meta:
        model = HomeDecoration
        fields = ('name', 'get_absolute_url', 'type', 'picture',)
