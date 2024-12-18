from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions, status

from .models import UserRegister


User = get_user_model()


class UserRegistrationSerializer(serializers.Serializer):
    is_view = False

    email = serializers.EmailField(min_length=10, max_length=254)
    password = serializers.CharField()
    company_name = serializers.CharField(min_length=5, max_length=100)
    accepted_rule = serializers.BooleanField()

    def create(self, validated_data):
        if not validated_data.get('accepted_rule'):
            raise exceptions.ValidationError(detail={'error': 'Accept the rules'}, code=status.HTTP_400_BAD_REQUEST)

        try:
            if not self.is_view:
                return UserRegister.objects.create(**validated_data)
            validated_data['user_active'] = True
            return User.objects.create_user(**validated_data)
        except Exception as e:
            raise exceptions.ValidationError(detail={'error': f'{e}'}, code=status.HTTP_400_BAD_REQUEST)


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)
    role = serializers.CharField(read_only=True)
    user_active = serializers.BooleanField(read_only=True)
    company_name = serializers.CharField(max_length=100)
    name = serializers.CharField(read_only=True)
    phone = serializers.CharField(max_length=20)
    telegram = serializers.BooleanField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    accepted_rule = serializers.BooleanField(read_only=True)

    def update(self, instance, validated_data, **kwargs):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.telegram = validated_data.get('telegram', instance.telegram)

        instance.save()

        return instance

