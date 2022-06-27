 
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('products/', LatestProductList.as_view()),
    path('products/search/', search),
    path('product/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('product/<slug:restaurant_slug>/', RestaurantAllProduct.as_view()),
    path('product/<slug:category_slug>/', CategoryDetail.as_view()),
    path('add-product/', ProductAdded.as_view()),
]
