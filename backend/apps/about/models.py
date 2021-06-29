from django.db import models

# Create your models here.
from stdimage import StdImageField

from backend.apps.seo.models import SeoAbstract


def generate_picture_path(instance, filename):
    path = 'pictures/about/%s' % (filename)
    return path


class About(SeoAbstract):
    """ Запись с информацией о производстве """
    about_company_title = models.CharField('Заголовок секции о компании', max_length=100, default='О КОМПАНИИ')
    about_company = models.TextField('О компании')
    about_company_picture = StdImageField('Изображение О компании', upload_to=generate_picture_path,
                                          variations={
                                              'w3000': (3000, 2000),
                                              'admin': (90, 60),
                                              'thumb': (15, 10),
                                          }, )
    about_factory_title = models.CharField('Заголовок секции о производстве', max_length=100, default='О ПРОИЗВОДСТВЕ')
    about_factory = models.TextField('О производстве')
    about_factory_picture = StdImageField('Изображение О производстве', upload_to=generate_picture_path,
                                          variations={
                                              'w3000': (3000, 2000),
                                              'w480': (480, 320),
                                              'admin': (90, 60),
                                              'thumb': (15, 10),
                                          }, )

    capacity_title = models.CharField('Заголовок секции "Производственные мощности"', max_length=100,
                                      default='ПРОИЗВОДСТВЕННЫЕ МОЩНОСТИ')
    capacity_sub_title = models.CharField('Подзаголовок секции "Производственные мощности"', max_length=600,
                                          default='Общая площадь производственных цехов составляет более 3 500 м² в том'
                                                  ' числе:')
    capacity_body = models.TextField('Текст секции "Производственные мощности"', null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Страница Производство'
        verbose_name_plural = 'Страница Производство'

    def __str__(self):
        return f'Страница Производство'
