from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model extending Django's built-in AbstractUser.

    Fields:
    - email (EmailField): The email address of the user. It is a unique identifier.

    Notes:
    - This model extends Django's AbstractUser, which includes all the standard fields
        like username, first_name, last_name, password, etc.
    - The email field is made unique to ensure that no two users can register with the same email address.
    """

    email = models.EmailField(unique=True)
