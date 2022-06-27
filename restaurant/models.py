from ctypes import addressof
from django.db import models
from django.contrib.auth.models import User
from userprofile.models import UserProfile
# Create your models here.


class Restaurant(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    favorite = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        return f"http://127.0.0.1:8000/api/product/{self.slug}/"
    
