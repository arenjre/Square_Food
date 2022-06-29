from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RestaurentOwnerSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class CreateRestaurentOwnerView(APIView):
    def get(self, request):
        queryset = CustomUser.objects.all()
        serializer = RestaurentOwnerSerializer(queryset,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RestaurentOwnerSerializer(data = request.data)
        if serializer.is_valid():
            new = serializer.save()
            new.set_password(new.password)
            new.is_staff = True
            new.is_active = True
            new.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



