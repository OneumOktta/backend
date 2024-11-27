from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class CustomUsers(BaseUserManager):

    def create_user(self,
                    id = models.IntegerField,
                    email = models.EmailField(unique=True),
                    password = models.CharField(max_length=100),
                    role = models.CharField(max_length=250),
                    managers = models.CharField(max_length=250),
                    managers_accept = models.BooleanField(default=False),
                    managers_email = models.EmailField):
        return self.create_user(id,
                                email,
                                password,
                                role,
                                managers,
                                managers_accept,
                                managers_email)