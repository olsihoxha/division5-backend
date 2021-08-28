from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

from common.views import UserSignUpAPIView, get_signed_in_user_data, update_user

urlpatterns = [
    path('auth/knock-knock/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('create-user/', UserSignUpAPIView.as_view()),
    path('get-my-data/', get_signed_in_user_data),
    path('update-my-data/', update_user),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
