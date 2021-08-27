from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from common.models import UserData


class EmailTokenObtainSerializer(TokenObtainSerializer):
    username_field = User.EMAIL_FIELD


def authenticate(email, password):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email=email)
    except UserModel.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None


class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = {}

        self.user = authenticate(email=attrs['email'], password=attrs['password'])

        if self.user is None:
            raise ValidationError('Ju lutem kontrolloni email dhe password')

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data



class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['first_name', 'last_name', 'birthdate', 'phone_number', 'address', 'nickname']

    def create(self, validated_data):
        return super(UserDataSerializer, self).create(validated_data)
