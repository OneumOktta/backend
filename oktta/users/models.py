from enum import unique

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class ManagerBase(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            return ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):

        user = self.create_user(email, password=password)

        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUsers(AbstractBaseUser):
    # CHOICES_ROLE = [
    #     (admin, 'AD')
    # ]

    email = models.EmailField(unique=True, max_length=254, verbose_name='email')
    password = models.CharField(max_length=75, verbose_name='password')
    role = models.CharField(max_length=100, verbose_name='role')

    objects = ManagerBase()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False


class UserApiKey(models.Model):
    STATUS = [
        (True, 'Подтвержден'),
        (False, 'Не подтвержден')
    ]

    is_active = models.BooleanField(default=False, choices=STATUS, verbose_name='Подтверждение почты')
    email = models.EmailField(unique=True, verbose_name='email')

