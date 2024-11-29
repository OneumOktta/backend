from os import access

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class CustomUsers(AbstractBaseUser):
    email = models.EmailField(unique=True),
    password = models.CharField(max_length=100),
    role = models.CharField(max_length=100)

class Manager(AbstractBaseUser):
    email = models.EmailField(unique=True),
    managers = models.CharField(max_length=250),
    is_active = models.BooleanField(default=True),
