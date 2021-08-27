from django.db import models



class Product(models.Model):
    class Meta:
        db_table = 'division_product'
    title = models.CharField(max_length=80)
    image = models.ImageField()
    asin = models.CharField(max_length=80)
    prices = models.PositiveIntegerField()
    reviews = models.FloatField()
