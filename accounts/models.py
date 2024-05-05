from django.db import models

# расширение встроенной модели пользователя
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")

    # Список имен полей, которые будут запрашиваться при создании пользователя с помощью команды управления createsuperuser
    REQUIRED_FIELDS = ["email", "phone", "full_name"]

    def __str__(self):
        return self.username
