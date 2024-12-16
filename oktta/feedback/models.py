from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class FeedBack(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    feed = models.CharField(max_length=254, blank=True, verbose_name='Отзыв')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')