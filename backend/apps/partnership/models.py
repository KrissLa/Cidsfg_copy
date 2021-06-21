from django.db import models
from backend.apps.seo.models import SeoAbstract


class Partnership(SeoAbstract):
    """ Модель страницы Сотрудничество"""
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сотрудничество'
        verbose_name_plural = 'Сотрудничество'

    def __str__(self):
        return f"Сотрудничество"


class CooperationApplication(models.Model):
    """ Заявка на сотрудниччество """
    area_of_activity = models.CharField('Область деятельности', max_length=100)
    company_type = models.CharField('Частное лицо/Компания', max_length=50)
    company_name = models.CharField('Название компании', max_length=255, blank=True, null=True)
    firs_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    type_of_contact = models.CharField('Куда ответить', max_length=100, default='Мобильный')
    contact = models.CharField('Контакт', max_length=255, default='')
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    created = models.DateTimeField('Время отправки сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на сотрудничество'
        verbose_name_plural = 'Заявки на сотрудничество'

    def __str__(self):
        return f'Заявка на сотрудничество №{self.id}'
