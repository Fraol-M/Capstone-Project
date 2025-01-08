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
    



# class OrderListAPIView(generics.ListAPIView):
#     queryset = Order.objects.prefetch_related("items", "items__product")
#     serializer_class = OrderSerilizer
    
    
# class UserOrderListAPIView(generics.ListAPIView):
#     queryset = Order.objects.prefetch_related("items", "items__product")
#     serializer_class = OrderSerilizer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         user = self.request.user
#         qs = super().get_queryset()
#         return qs.filter(user=user)

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("items", "items__product")
    serializer_class = OrderSerilizer
    pagination_class = None
    filterset_class = OrderFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated],


    @action(detail=False, 
            methods=['get'],
            url_path= 'user'
        )
    def user_order(self, request):
        user = request.user
        orders = self.get_queryset().filter(user=user)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)

    


    
    
class ProductInfoApiView(APIView):
    
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductInfoSerilizer({
        'product': product,
        'count': len(product),
        'max_price': product.aggregate(max_price = Max('price'))['max_price']
        
        
        })
    
        return Response(serializer.data)