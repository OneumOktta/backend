from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Feedback


User = get_user_model()


class FeedbackSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    text = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)
