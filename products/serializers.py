from dataclasses import field, fields
from itertools import product
from rest_framework import serializers
from restaurant.serializers import RestaurantSerializer
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer() 
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
            "restaurant"
        ]
class RestaurantProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
        ]

class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True) 

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            'product',
        )