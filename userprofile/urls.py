from django.urls import path
from .views import (CreateRestaurentOwnerView)

urlpatterns = [
    path("restaurentowner/",CreateRestaurentOwnerView.as_view()),
    
]