from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("api-jwt-auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api-jwt-auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api-jwt-auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
