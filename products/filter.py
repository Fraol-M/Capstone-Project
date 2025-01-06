import django_filters 

from .models import Product
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