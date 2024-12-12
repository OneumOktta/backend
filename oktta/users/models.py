from enum import unique
from tabnanny import verbose

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class ManagerBase(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            return ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):

        user = self.create_user(email, password=password)
        user.role = 'administrator'
        user.save(using=self._db)
        return user


class CustomUsers(AbstractBaseUser):

    CHOICES_ROLE = [('administrator', 'Администратор'),
                    ('business', 'Бизнес'),
                    ('manager', 'Менеджер')]

    CHOICES_ACTIVE = [(True, 'Активирован'),
                      (False, 'Не активирован')
                      ]

    email = models.EmailField(db_index=True, unique=True, max_length=254, verbose_name='Почта')
    role = models.CharField(db_index=True, max_length=15, choices=CHOICES_ROLE, default='business', verbose_name='Роль')
    user_active = models.BooleanField(choices=CHOICES_ACTIVE, default=False, verbose_name='Активирован')
    company_name = models.CharField(blank=True, max_length=100, verbose_name='Название компании')
    name = models.CharField(blank=True, max_length=100, verbose_name='Имя')
    phone = models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')
    telegram = models.BooleanField(db_index=True, default=False, verbose_name='Телеграм')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    accepted_rule = models.BooleanField(verbose_name='Политика конфиденциальности')

    objects = ManagerBase()

    REQUIRED_FIELDS = ['password', ]
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.email}'