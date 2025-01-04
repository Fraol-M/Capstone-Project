from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Max

from .serializers import ProductSerializer, OrderItemSerilizer, OrderSerilizer, ProductInfoSerilizer, CategorySerializer
from .models import Product, Order, OrderItem, Category
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny)
from rest_framework.decorators import api_view
from rest_framework.views import APIView






    
    
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related("category")
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]  
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()



class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
    

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]  
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

    
    
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items", "items__product")
    serializer_class = OrderSerilizer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)
    




class ProductInfoApiView(APIView):
    
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductInfoSerilizer({
        'product': product,
        'count': len(product),
        'max_price': product.aggregate(max_price = Max('price'))['max_price']
        
        
        })
    
        return Response(serializer.data)
        



class ProductCreateApiView(generics.ListCreateAPIView):
    model = Product.objects.all()
    serializer_class = ProductSerializer