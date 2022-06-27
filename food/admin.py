from django.contrib import admin
from .models import SubCategory, Category, Rating, Location, Restaurant, Food, Payment, Cart, Order # Register your models here.

admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Location)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(Order)