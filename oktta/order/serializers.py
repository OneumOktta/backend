from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.Serializer):
    full_name = serializers.CharField(min_length=5, max_length=100, label='ФИО')
    email = serializers.EmailField(min_length=5, max_length=254, label='Почта')
    phone = serializers.CharField(min_length=11, max_length=20, label='Номер телефона')
    company_name = serializers.CharField(max_length=255, label='Название компании')
    site = serializers.URLField(max_length=255, label='Сайт')
    date_created = serializers.DateTimeField(read_only=True)
    status = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class OrderUpdateSerializer(serializers.Serializer):
    full_name = serializers.CharField(read_only=True, min_length=5, max_length=100, label='ФИО')
    email = serializers.EmailField(read_only=True, min_length=5, max_length=254, label='Почта')
    phone = serializers.CharField(read_only=True, min_length=11, max_length=20, label='Номер телефона')
    company_name = serializers.CharField(read_only=True, max_length=255, label='Название компании')
    site = serializers.URLField(read_only=True, max_length=255, label='Сайт')
    date_created = serializers.DateTimeField(read_only=True)
    status = serializers.BooleanField(required=True)

    def update(self, instance: Order, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
