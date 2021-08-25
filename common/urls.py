from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from common.views import EmailTokenObtainPairView

urlpatterns = [
    path('auth/knock-knock/', EmailTokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
]
