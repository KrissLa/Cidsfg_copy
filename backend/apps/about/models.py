from django.db import models

# Create your models here.
from stdimage import StdImageField

from backend.apps.seo.models import SeoAbstract


def generate_picture_path(instance, filename):
    path = 'pictures/about/%s' % (filename)
    return path


class About(SeoAbstract):
    """ Запись с информацией о производстве """
    about_company = models.TextField('О компании')
    about_company_picture = StdImageField('Изображение О компании', upload_to=generate_picture_path,
                                          variations={
                                              'w3000': (3000, 2000),
                                              'admin': (90, 60),
                                              'thumb': (15, 10),
                                          }, )
    about_factory = models.TextField('О производстве')
    about_factory_picture = StdImageField('Изображение О производстве', upload_to=generate_picture_path,
                                          variations={
                                              'w3000': (3000, 2000),
                                              'admin': (90, 60),
                                              'thumb': (15, 10),
                                          }, )
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Страница Производство'
        verbose_name_plural = 'Страница Производство'

    def __str__(self):
        return f'Страница Производство'
