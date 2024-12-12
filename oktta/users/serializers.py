from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions, status


User = get_user_model()


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=10, max_length=254)
    password = serializers.CharField()
    company_name = serializers.CharField(min_length=5, max_length=100)
    accepted_rule = serializers.BooleanField()

    def create(self, validated_data):
        if not validated_data.get('accepted_rule'):
            raise exceptions.ValidationError(detail={'error': 'Accept the rules'}, code=status.HTTP_400_BAD_REQUEST)

        try:
            return User.objects.create_user(**validated_data)
        except Exception as e:
            raise exceptions.ValidationError(detail={'error': f'{e}'}, code=status.HTTP_400_BAD_REQUEST)
