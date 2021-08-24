from django.contrib import admin
from django.urls import path

from products.views import get_products


urlpatterns = [
    path('get-products/', get_products),
]
