from django.urls import path
from .views import ProductDetailAPIView, ProductListCreateAPIView, ProductInfoApiView, OrderListAPIView, CategoryListAPIView

urlpatterns = [
    path('products/',ProductListCreateAPIView.as_view() , name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('orders/',OrderListAPIView.as_view(), name='orders'),
    path('products/info', ProductInfoApiView.as_view(), name='product-info'),
    path('category/',CategoryListAPIView.as_view() , name='categoty-list'),

]