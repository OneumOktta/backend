from django.db import models


class Order(models.Model):
    """Модель для заявок на демонстрацию сервиса"""

    STATUS_CHOICES = [
        (True, 'Активен'),
        (False, 'Неактивен')
    ]

    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(db_index=True, unique=True, max_length=254, verbose_name='Почта')
    phone = models.CharField(unique=True, max_length=20, verbose_name='Номер телефона')
    company_name = models.CharField(max_length=255, verbose_name='Название компании')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    status = models.BooleanField(default=True, choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return f'{self.full_name} - {self.email}({self.phone})'
