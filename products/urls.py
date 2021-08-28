from django.contrib import admin
from django.urls import path

from products.views import get_products, ProductListAPIView, save_product, ProductSavedListAPIView

urlpatterns = [
    path('get-products/', get_products),
    path('save-product/', save_product),
    path('get-products/ours/', ProductListAPIView.as_view()),
    path('get-products/ours/saved/', ProductSavedListAPIView.as_view()),
]
