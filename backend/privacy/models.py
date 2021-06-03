from django.db import models

from backend.seo.models import SeoAbstract


class Privacy(SeoAbstract):
    """ Страница с политикой обработки персональных данных пользователей """
    organization_name = models.CharField('Название организации', max_length=255, default='CUBO ДОМ')
    email = models.EmailField('Email оператора персональных данных для связи', default='ask@cubodom.ru')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Политика конфиденциальности'

    def __str__(self):
        return 'Страница с политикой конфиденциальности'


class PrivacyData(models.Model):
    """ Данные которые собираются на сайте """
    privacy = models.ForeignKey(Privacy, verbose_name='Политика конфиденцальности', on_delete=models.CASCADE,
                                related_name='data')
    item = models.CharField('Пункт данных, которые собираются', max_length=300,
                            help_text='Например "Фамилия, имя, итчество" или "Номер телефона"')

    class Meta:
        verbose_name = 'Пункт собираемых данных'
        verbose_name_plural = 'Пункты собираемых данных'
        ordering = ['id', ]

    def __str__(self):
        return f'Пункт собираемых данных {self.id} - {self.item}'


class PrivacyPurpose(models.Model):
    """ Цель сбора данных """
    privacy = models.ForeignKey(Privacy, verbose_name='Политика конфиденцальности', on_delete=models.CASCADE,
                                related_name='purpose')
    item = models.CharField('Цель сбора данных', max_length=600,
                            help_text='Например "информирование Пользователя посредством отправки электронных писем"')

    class Meta:
        verbose_name = 'Цель сбора данных'
        verbose_name_plural = 'Цели сбора данных'
        ordering = ['id', ]

    def __str__(self):
        return f'Цель {self.id} - {self.item}'


class PrivacyBasis(models.Model):
    """ Правовые основания обработки персональных данных данных """
    privacy = models.ForeignKey(Privacy, verbose_name='Политика конфиденцальности', on_delete=models.CASCADE,
                                related_name='basis')
    item = models.CharField('Правовое основание обработки персональных данных', max_length=600,
                            help_text='Например "уставные (учредительные) документы Оператора')

    class Meta:
        verbose_name = 'Правовое основание обработки персональных данных'
        verbose_name_plural = 'Правовые основания обработки персональных данных'
        ordering = ['id', ]

    def __str__(self):
        return f'Основание {self.id} - {self.item}'
