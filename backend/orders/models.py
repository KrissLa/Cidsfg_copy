from django.db import models


# Create your models here.
from loguru import logger


class Order(models.Model):
    """ Модель заказа """
    username = models.CharField('Имя пользователя', max_length=255);
    phone_number = models.PositiveBigIntegerField("Номер телефона пользователя")

    class Meta:
        verbose_name = 'Заявка пользователя'
        verbose_name_plural = 'Заявки пользователей'

    def __str__(self):
        return f'Заявка № {self.id} от пользователя {self.username}'
