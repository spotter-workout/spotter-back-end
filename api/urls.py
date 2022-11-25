from django.urls import path, include
from .views import HelloWorld

urlpatterns = [
    path("auth/", include("users.urls")),
]
