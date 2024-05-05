from django.db import models
from accounts.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=50, default="Название товара", verbose_name="Товар"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    available = models.IntegerField( verbose_name="В наличии")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=30, default='Новое', verbose_name="Название статуса")

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"

    def __str__(self):
        return self.name


class Order(models.Model):
    quantity = models.IntegerField( verbose_name="Количество")
    address = models.CharField(
        max_length=100, verbose_name="Адрес"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.address
