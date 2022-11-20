from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from users.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password
import jwt, datetime
import os

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "success"})


class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("404 - User does not exist")

        if not user.check_password(password):
            raise AuthenticationFailed("401 - Incorrect password")

        payload = {
            "username": user.username,
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")

        response = Response()

        response.data = {"jwt": token}

        return response
