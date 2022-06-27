from ctypes import addressof
from distutils.command.build_scripts import first_line_re
import email
from itertools import product
from ssl import create_default_context
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return self.first_name

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    rate = models.IntegerField(default=0)

    def __str__(self) -> str:
        return "%s" % self.id
    
