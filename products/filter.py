import django_filters 

from .models import Product, Order
from rest_framework import filters



class InStockFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(stock__gt=0)

class ProductFilter(django_filters.FilterSet):
    category__name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = {
            'price': ['lt', 'gt'],
            'name': ['exact', 'icontains'],
        }
        
        
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'status': ['exact'],
            'created_at' : ['lt', 'gt','exact']    
        }