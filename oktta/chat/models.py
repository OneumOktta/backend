from django.db import models

from token_key.models import ApiToken


class ChatCustomization(models.Model):
    icon = models.CharField(max_length=255)
    icon_mime_type = models.CharField(max_length=255)
    greeting = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    header_color = models.CharField(max_length=255)
    header_text_color = models.CharField(max_length=255)
    background_color = models.CharField(max_length=255)
    user_color = models.CharField(max_length=255)
    user_text_color = models.CharField(max_length=255)
    bot_color = models.CharField(max_length=255)
    bot_text_color = models.CharField(max_length=255)
    custom_css = models.CharField(max_length=255)


class Chat(models.Model):
    MODE_CHOICES = [
        ('bot', 'Бот'),
        ('human', 'Человек'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, verbose_name='Режим')
    is_close = models.BooleanField(default=False, verbose_name='Закрыт')

    api_key = models.ForeignKey(ApiToken, on_delete=models.CASCADE, verbose_name='Токен')


class Message(models.Model):
    ROLE_CHOICES = [
        ('user', 'Пользователь'),
        ('assistant', 'Ассистент'),
        ('human', 'Человек')
    ]

    content = models.TextField(verbose_name='Текст')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name='Роль')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
