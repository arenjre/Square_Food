from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from uuid import uuid4


def generateUUID():
    return str(uuid4())

cat_choice = (
    ("veg", "Veg"),
    ("vegan", "Vegan"),
    ("non-veg", "Non-veg")
)
class SubCategory(models.Model):
    name = models.CharField(choices=cat_choice, max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class Rating(models.Model):
    rate = models.IntegerField(default=0)

class Location(models.Model):
    lng = models.CharField(max_length=20, blank=True, null=True)
    lat = models.CharField(max_length=20, blank=True, null=True)

class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Food(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)

t_choice = (
    ("offline", "COD"),
    ("online", "Online"),
)
class Payment(models.Model):
    cost = models.IntegerField(default=0)
    transaction_type = models.CharField(choices=t_choice, max_length=255)
    transaction_id = models.UUIDField(default=generateUUID, editable=False)
    transaction_status = models.BooleanField(default=False)



class Order(models.Model):
    item = models.ManyToManyField(Food, related_name="order")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    
    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        # save original values, when model is loaded from database,
        # in a separate attribute on the model
        instance._loaded_values = dict(zip(field_names, values))
        
        return instance

class Cart(models.Model):
    user = models.ForeignKey(User, related_name="cart", on_delete=models.CASCADE)
    items = models.ManyToManyField(Order)
    total_cost = models.IntegerField()

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        # save original values, when model is loaded from database,
        # in a separate attribute on the model
        instance._loaded_values = dict(zip(field_names, values))
        
        return instance
