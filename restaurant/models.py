from ctypes import addressof
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    addressof = models.CharField(max_length=255)
    favorite = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        return f"/{self.slug}/"
    
