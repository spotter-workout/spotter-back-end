from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=128)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    last_login = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
