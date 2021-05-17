from django.db import models


# Create your models here.

class CooperationApplication(models.Model):
    """ Заявка на сотрудниччество """
    area_of_activity = models.CharField('Область деятельности', max_length=100)
    company_type = models.CharField('Частное лицо/Компания', max_length=50)
    company_name = models.CharField('Название компании', max_length=255, blank=True, null=True)
    firs_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    email = models.CharField('E-mail', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255, null=True, blank=True)
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    created = models.DateTimeField('Время отправки сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на сотрудничество'
        verbose_name_plural = 'Заявки на сотрудничество'

    def __str__(self):
        return f'Заявка на сотрудничество №{self.id}'
