from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserData(models.Model):
    class Meta:
        db_table = 'division_data'
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    birthdate = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    nickname = models.CharField(max_length=60)
    user = models.ForeignKey(User, related_name='user_data', on_delete=models.CASCADE)
