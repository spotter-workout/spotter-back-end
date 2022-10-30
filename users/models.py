from enum import unique
from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=128)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
