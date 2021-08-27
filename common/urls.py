from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from common.views import EmailTokenObtainPairView, UserDataListCreateAPIView

urlpatterns = [
    path('auth/knock-knock/', EmailTokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('user-data/', UserDataListCreateAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
