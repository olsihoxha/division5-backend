from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from common.const import BASE_URL
from products.models import Product, SavedProducts


class ProductSerializer(serializers.ModelSerializer):
    image = SerializerMethodField()
    is_saved = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'asin', 'prices', 'reviews', 'is_saved']

    @staticmethod
    def get_image(obj):
        return BASE_URL + obj.image.url

    def get_is_saved(self, obj):
        user = self.context['request'].user
        is_saved = SavedProducts.objects.filter(user=user, product=obj).exists()
        return is_saved
