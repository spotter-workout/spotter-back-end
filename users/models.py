from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):  # type: ignore
    """UserManager class."""

    # type: ignore
    def create_user(self, username: str, password: str = None) -> "User":
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError("Users must have a username.")

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username: str, password: str) -> "User":  # type: ignore
        """Create and return a `User` with superuser (admin) permissions."""
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=128)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    last_login = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()
