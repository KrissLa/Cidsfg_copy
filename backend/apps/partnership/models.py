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
