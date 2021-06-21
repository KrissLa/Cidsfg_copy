from django.db import models
from stdimage import StdImageField

from backend.apps.seo.models import SeoAbstract


def generate_picture_path(instance, filename):
    path = 'pictures/contacts/%s/' % filename
    return path


class Contacts(SeoAbstract):
    """ Модель страницы с контактами """
    address = models.CharField('Адрес производства', max_length=255, blank=True,
                               help_text="Чтобы не отображать, оставьте пустым")
    address_office = models.CharField('Адрес офиса', max_length=255, blank=True,
                                      help_text="Чтобы не отображать, оставьте пустым")
    phone_number = models.CharField('Номер телефона производства', max_length=15,
                                    help_text='Без знака +. Чтобы не отображать, оставьте пустым', blank=True, )
    phone_number_office = models.CharField('Номер телефона офиса', max_length=15,
                                           help_text='Без знака +. Чтобы не отображать, оставьте пустым', blank=True)
    email = models.CharField('Email производства', max_length=255, blank=True,
                             help_text="Чтобы не отображать, оставьте пустым")
    email_office = models.CharField('Email офиса', max_length=255, blank=True,
                                    help_text="Чтобы не отображать, оставьте пустым")
    working_hours = models.CharField('Время работы производства', max_length=255, blank=True,
                                     help_text="Чтобы не отображать, оставьте пустым")
    working_hours_office = models.CharField('Время работы офиса', max_length=255, blank=True,
                                            help_text="Чтобы не отображать, оставьте пустым")
    map_picture = StdImageField('Изображение для страницы контакты', upload_to=generate_picture_path,
                                variations={
                                    'w800': (800, 400),
                                    'w600': (600, 300),
                                    'w400': (400, 200),
                                    'admin': (90, 45),
                                    'thumb': (20, 10),
                                }, blank=True, help_text="Чтобы не отображать, оставьте пустым")
    map_picture_footer = StdImageField('Изображение для футера (1х1)', upload_to=generate_picture_path,
                                       variations={
                                           'w800': (800, 800),
                                           'w600': (600, 600),
                                           'w400': (400, 400),
                                           'admin': (90, 90),
                                           'thumb': (20, 20),
                                       }, blank=True, help_text="Чтобы не отображать, оставьте пустым")
    map_link = models.URLField('Ссылка на расположение на карте', blank=True)
    alt_picture = models.CharField('Подпись к фотографии на странице контакты',
                                   default='Изображение расположения на карте', max_length=255,
                                   blank=True, help_text="Чтобы не отображать, оставьте пустым")
    alt_picture_footer = models.CharField('Подпись к фотографии в футере',
                                          default='Изображение расположения на карте', max_length=255,
                                          blank=True, help_text="Чтобы не отображать, оставьте пустым")
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f"Контакты"


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
