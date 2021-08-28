from django.contrib import admin
from django.urls import path

from products.urls import urlpatterns as product_urls
from common.urls import urlpatterns as common_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += product_urls
urlpatterns += common_urls
