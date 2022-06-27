from ctypes import addressof
from distutils.command.upload import upload
from django.db import models
from django.comtrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    avtar = models.ImageField(upload_to="images/avtar", default="images/avtar/User-Profile.png")
    
    def __str__(self):
        return self.user.username

