from django.db import models


# Create your models here.


class SeoAbstract(models.Model):
    """Абстрактная модель для добавления метаданных на страницу"""
    seo_title = models.CharField('SEO title', help_text='Не больше 70 символов', max_length=70, blank=True,
                             default='CUBO')
    seo_description = models.CharField('SEO description', help_text='Не больше 150 символов', max_length=150, blank=True)

    class Meta:
        abstract = True
