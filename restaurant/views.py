from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from userprofile.models import CustomUser
from rest_framework import status
from .serializers import ListRestaurentSerializer
from .models import Restaurant


# Create your views here.
class AddRestaurent(APIView):
    def post(self, request):
        user_obj = CustomUser.objects.filter(id=request.data.get('user')).first()
        restaurant_obj = Restaurant.objects.filter(id=request.data.get('restaurant')).first()
        if user_obj.is_superuser == True:
            serializer = ListRestaurentSerializer(data = request.data)
            if serializer.is_valid():
                restaurant_obj.Is_varified = True
                restaurant_obj.save()
                serializer.save()
                return Response(serializer.data,status = status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_404_NOT_FOUND)
        return Response({'message':'Invalid user'})

            