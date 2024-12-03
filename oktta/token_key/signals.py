from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from .models import ApiToken

# TODO Во время создаваться пользователя, должен создаваться Токен
User = get_user_model()


@receiver(post_save, sender=User)
def create_api_token(sender, instance, created, **kwargs):
    pass
