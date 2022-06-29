from ctypes import addressof
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Restaurant(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    favorite = models.BooleanField(default=False)
    slug = models.SlugField()
    Is_varified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        return f"http://127.0.0.1:8000/api/product/{self.slug}/"
    
class ListedRestaurants(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.restaurant.name
