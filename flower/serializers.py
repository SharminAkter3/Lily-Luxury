from rest_framework import serializers
from .models import Flower, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FlowerSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Flower
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    reviwer = serializers.StringRelatedField(many=False)
    flower = serializers.StringRelatedField(many=False)

    class Meta:
        model = Review
        fields = "__all__"
