from django.urls import path, include
from .views import HelloWorld
urlpatterns = [
    path('helloworld', HelloWorld.as_view()),
]