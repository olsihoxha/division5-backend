from products.models import Product
from django_filters.rest_framework import FilterSet, filters


class ProductsFilter(FilterSet):
    title = filters.CharFilter(lookup_expr='icontains', field_name='title')

    class Meta:
        model = Product
        fields = ['title']
