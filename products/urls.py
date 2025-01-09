from django.urls import path
from rest_framework import routers



from .views import ProductDetailAPIView, ProductListCreateAPIView, ProductInfoApiView,CategoryListAPIView, OrderViewSets

urlpatterns = [
    path('products/',ProductListCreateAPIView.as_view() , name='product-list'),
    path('products/id/<product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    # path('orders/',OrderListAPIView.as_view(), name='orders'),
    # path('user/orders/',UserOrderListAPIView.as_view(), name='user-orders'),
    path('products/info/', ProductInfoApiView.as_view(), name='product-info'),
    path('category/',CategoryListAPIView.as_view() , name='categoty-list'),

]

router = routers.DefaultRouter()
router.register("orders", OrderViewSets)
urlpatterns+=router.urls