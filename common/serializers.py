from django.db.transaction import atomic
from django.forms import ModelForm
from rest_framework import serializers

from common.models import User


class UserSignUpWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'birthdate', 'phone_number', 'address', 'nickname']

    @atomic()
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super(UserSignUpWriteSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthdate', 'phone_number', 'address', 'nickname']
