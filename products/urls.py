from django.contrib import admin
from django.urls import path

from products.views import get_products, ProductListAPIView

urlpatterns = [
    path('get-products/', get_products),
    path('get-products/ours/', ProductListAPIView.as_view())
]
