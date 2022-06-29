from asyncore import read
from ctypes import addressof
from distutils.command.upload import upload
from gzip import READ
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from pkg_resources import require
from .managers import CustomUserManager
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUser(AbstractBaseUser):
    username = None
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    is_varified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    # password = models.CharField(max_length=255, editable=False)
    mobile = models.CharField(max_length=13)
    avtar = models.ImageField(upload_to="images/avtar", default="images/avtar/User-Profile.png")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile"]

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email
    


