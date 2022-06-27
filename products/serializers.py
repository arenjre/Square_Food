from dataclasses import field, fields
from itertools import product
from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
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