from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from common.models import UserData
from common.serializers import CustomTokenObtainPairSerializer, UserDataSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserDataListCreateAPIView(ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer