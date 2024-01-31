from django.shortcuts import render
from rest_framework import viewsets, pagination
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class FlowerPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100


class FLowerViewset(viewsets.ModelViewSet):
    queryset = models.Flower.objects.all()
    serializer_class = serializers.FlowerSerializer
    pagination_class = FlowerPagination


class ReviewViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
