from django.db import models
from loguru import logger


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

    @classmethod
    def get_new_count(cls):
        logger.info(cls.objects.filter(processed=False).count())
        return cls.objects.filter(processed=False).count()

    # def need_count(self):
    #     return True

    def __str__(self):
        return f'Заявка на индивидуальный проект № {self.id}'

    class Meta:
        verbose_name = 'Заявка на уникальный проект'
        verbose_name_plural = f'Заявки на уникальный проект'


class Message(models.Model):
    """ Модель сообщения, отправляемого через форму на странице контакты """
    username = models.CharField('Имя пользователя', max_length=255)
    type_of_contact = models.CharField('Куда ответить', max_length=100, default='Мобильный')
    contact = models.CharField('Контакт', max_length=255, default='')
    message = models.TextField('Сообщение пользователя')
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    created = models.DateTimeField('Время отправки сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение, отправленное через форму со страницы Контакты'
        verbose_name_plural = 'Сообщения отправленные через форму со страницы Контакты'

    def __str__(self):
        if self.processed:
            processed = ''
        else:
            processed = '(Новое сообщение!)'
        return f'Сообщение № {self.id} от пользователя {self.username}. {processed}'
