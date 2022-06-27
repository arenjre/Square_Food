from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny



# Create your views here.

class LatestProductList(APIView):
    def get(self, request, format=None):
        product = Product.get_all_products()[0:4]
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug = category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data) 

class RestaurantAllProduct(APIView):
    def get_object(self, restaurant_slug):
        try:
            return Product.objects.filter(restaurant__slug = restaurant_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, restaurant_slug, format=None):
        product = self.get_object(restaurant_slug)
        serializer = RestaurantProductSerializer(product, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug = category_slug)
        except Category.DoesNotExist:
            raise Http404 
        
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)

        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(["POST"])
def search(request):
    query = request.data.get('query', "")
    if query:
        products = Product.get_all_products().filter(
                Q(name__icontains=query) | Q(description__icontains=query) 
              | Q(restaurant__name__icontains=query) | Q(category__slug__icontains=query) | Q(sub_category__name__icontains=query))
              
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    else:
        return Response({"products":[]})


class ProductAdded(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.user.is_staff == True:
            pass




        

