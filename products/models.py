from django.db import models

from common.models import User


class Product(models.Model):
    class Meta:
        db_table = 'division_product'

    title = models.CharField(max_length=80)
    image = models.ImageField()
    asin = models.CharField(max_length=80)
    prices = models.PositiveIntegerField()
    reviews = models.FloatField()


class SavedProducts(models.Model):
    class Meta:
        db_table = 'division_saved_products'

    user = models.ForeignKey(User, related_name='saved_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='saved_products', on_delete=models.CASCADE)
