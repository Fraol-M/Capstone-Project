from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Max

from .serializers import ProductSerializer, OrderItemSerilizer, OrderSerilizer, ProductInfoSerilizer, CategorySerializer
from .models import Product, Order, OrderItem, Category
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny)
from rest_framework.decorators import api_view
from rest_framework.views import APIView


from .filter import ProductFilter, InStockFilter, OrderFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action






class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    
    
    
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related("category")
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        InStockFilter
    ]
    search_fields = ['^name', 'price']
    ordering_fields = ['name','price', 'stock']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'size'
    pagination_class.max_page_size = 1000

   
    def get_permissions(self):
        self.permission_classes = [AllowAny]  
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()




    
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'
    
    

    
    def get_permissions(self):
        self.permission_classes = [AllowAny]  
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    



class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("items", "items__product")
    serializer_class = OrderSerilizer
    pagination_class = None
    permission_classes = [IsAuthenticated]

    filterset_class = OrderFilter
    filter_backends = [DjangoFilterBackend]
    
    
    
    def get_queryset(self):
        user = self.request.user  
        qs = super().get_queryset()
        if not user.is_staff:
            qs = qs.filter(user=user)
        return qs




    
    
class ProductInfoApiView(APIView):
    permission_classes = [AllowAny]

    
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductInfoSerilizer({
        'product': product,
        'count': len(product),
        'max_price': product.aggregate(max_price = Max('price'))['max_price']
        
        
        })
    
        return Response(serializer.data)