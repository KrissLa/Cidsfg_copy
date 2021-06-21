from django.db import models
from backend.apps.seo.models import SeoAbstract

# Create your models here.

class HomePage(SeoAbstract):
    """ Главная страница """
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def __str__(self):
        return 'Главная страница'
