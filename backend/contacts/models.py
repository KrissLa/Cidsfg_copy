from django.db import models
from stdimage import StdImageField

from backend.seo.models import SeoAbstract


def generate_picture_path(instance, filename):
    path = 'pictures/contacts/%s/' % filename
    return path


class Contacts(SeoAbstract):
    """ Модель страницы с контактами """
    address = models.CharField('Адрес', max_length=255, blank=True, help_text="Чтобы не отображать, оставьте пустым")
    email = models.CharField('Email', max_length=255, blank=True, help_text="Чтобы не отображать, оставьте пустым")
    working_hours = models.CharField('Время работы', max_length=255, blank=True,
                                     help_text="Чтобы не отображать, оставьте пустым")
    map_picture = StdImageField('Изображение', upload_to=generate_picture_path,
                                variations={
                                    'w800': (800, 400),
                                    'w600': (600, 300),
                                    'w400': (400, 200),
                                    'admin': (90, 45),
                                    'thumb': (20, 10),
                                }, blank=True, help_text="Чтобы не отображать, оставьте пустым")
    map_link = models.URLField('Ссылка на расположение на карте', blank=True)
    alt_picture = models.CharField('Подпись к фотографии', default='Изображение расположения на карте', max_length=255,
                                   blank=True, help_text="Чтобы не отображать, оставьте пустым")

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f"Контакты"


class PhoneNumber(models.Model):
    """ Модель номера телефона """
    contacts = models.ForeignKey(Contacts, verbose_name='Номер телефона', related_name='phones',
                                 on_delete=models.CASCADE)
    phone_number = models.CharField('Номер телефона', max_length=15, help_text='Без знака +')

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефона'

    def __str__(self):
        return f'Номер телефона № {self.id} - {self.phone_number}'


class Message(models.Model):
    """ Модель сообщения, отправляемого через форму на странице контакты """
    username = models.CharField('Имя пользователя', max_length=255)
    email = models.CharField('E-mail пользователя', max_length=255)
    phone_number = models.CharField('Номер телефона пользователя', max_length=15)
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
