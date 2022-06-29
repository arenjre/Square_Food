from dataclasses import field, fields
from rest_framework import serializers
from .models import ListedRestaurants

from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "address",
            "favorite",
            "get_absolute_url",
            "user",
        ]

class ListRestaurentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListedRestaurants
        fields = '__all__'