from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    flower = serializers.StringRelatedField(many=False)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Order
        fields = "__all__"
