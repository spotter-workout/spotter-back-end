from django.urls import path, include
from .views import RegisterView, LoginView, HelloWorld
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
    TokenVerifyView,
)

urlpatterns = [
    path("helloworld", HelloWorld.as_view()),
    path("register", RegisterView.as_view()),
    # path("login", LoginView.as_view()),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
]
