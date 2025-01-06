import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category__name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = {
            'price': ['lt', 'gt'],
            'name': ['exact', 'icontains'],
        }