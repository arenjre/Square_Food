from django.urls import path
from .views import AddRestaurent

urlpatterns = [
    path("addrestaurent/",AddRestaurent.as_view()),
    
]