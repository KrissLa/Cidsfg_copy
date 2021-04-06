from rest_framework import serializers

from backend.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """ Сериализация скидок """
    class Meta:
        model = Order
        fields = "__all__"