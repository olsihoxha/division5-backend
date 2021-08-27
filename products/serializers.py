
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from common.const import BASE_URL
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'asin', 'prices', 'reviews']

    @staticmethod
    def get_image(obj):
        return BASE_URL + obj.image.url
