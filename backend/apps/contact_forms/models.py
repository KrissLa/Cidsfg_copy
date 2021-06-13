from django.db import models


class IndividualProjectRequest(models.Model):
    """
    Модель заявки на индивидуальный проект
    """
    number_of_floors = models.PositiveSmallIntegerField('Количество этажей')
    area = models.PositiveSmallIntegerField('Площадь')
    number_of_rooms = models.PositiveSmallIntegerField('Количество комнат')
    number_of_bathrooms = models.PositiveSmallIntegerField('Количество санузлов')
    garage_is_needed = models.BooleanField('Нужен гараж')
    comment = models.TextField('Другие пожелания', blank=True, null=True)
    username = models.CharField('Имя пользователя', max_length=255)
    type_of_contact = models.CharField('Куда ответить', max_length=100, default='Мобильный')
    contact = models.CharField('Контакт', max_length=255, default='')
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    created = models.DateTimeField('Время отправки заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на уникальный проект'
        verbose_name_plural = 'Заявки на уникальный проект'

    def __str__(self):
        return f'Заявка на индивидуальный проект № {self.id}'
