
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import routers
from .views import ProductListCreateAPIView, ProductDetailAPIView, ProductInfoApiView, CategoryListAPIView, OrderViewSets

router = routers.DefaultRouter()
router.register("orders", OrderViewSets)

class CustomAPIRootView(APIView):
    def get(self, request, *args, **kwargs):
        sample_product_id = 1  # test value to show for product_id
        return Response({
            "products": request.build_absolute_uri("products/"),
            "product_detail": request.build_absolute_uri(f"products/id/{sample_product_id}/"),
            "categories": request.build_absolute_uri("category/"),
            "product_info": request.build_absolute_uri("products/info/"),
            "orders": request.build_absolute_uri("orders/"),
        })



urlpatterns = [
    path('', CustomAPIRootView.as_view(), name='api-root'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/id/<product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/info/', ProductInfoApiView.as_view(), name='product-info'),
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('router/', include(router.urls)),  
]
urlpatterns+=router.urls


    
