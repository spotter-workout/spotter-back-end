from dataclasses import field
import os
from rest_framework import serializers
from app.settings import SALT

from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=60)
    # id = serializers.CharField(max_length=36)
    # created_at = serializers.DateTimeField()
    # modified_at = serializers.DateTimeField()

    class Meta:
        model = User
        fields = ["id", "username", "password", "created_at", "modified_at"]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # hashing the password
            salt = SALT
            hashed_password = make_password(password, salt=salt, hasher="default")
            instance.password = hashed_password

        instance.save()
        return instance
