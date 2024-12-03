import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


def time_expired():
    return timezone.now() + timezone.timedelta(days=1)


class UserActivationToken(models.Model):
    token = models.CharField(default=uuid.uuid4, max_length=36, verbose_name='Токен для активации')
    expired = models.DateTimeField(default=time_expired, verbose_name='Дата истечения токена')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания токена')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.user.email}'


class ApiToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Идентификатор')
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название токена')
    token_limit = models.PositiveIntegerField(default=50000, verbose_name='Лимит токенов')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    last_used = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Последнее использование')
    token_active = models.BooleanField(default=True, db_index=True, verbose_name='Активный токен')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.user.email} - {self.id}'
