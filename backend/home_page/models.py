from django.db import models
from backend.seo.models import SeoAbstract

# Create your models here.

class HomePage(SeoAbstract):
    """ Главная страница """


    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def __str__(self):
        return 'Главная страница'
