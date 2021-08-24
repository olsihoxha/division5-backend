from rest_framework_simplejwt.views import TokenViewBase

from common.serializers import TokenObtainPairSerializer


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer
