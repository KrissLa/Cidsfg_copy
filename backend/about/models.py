from django.db import models

# Create your models here.
from stdimage import StdImageField

from backend.seo.models import SeoAbstract


def generate_picture_path(instance, filename):
    path = 'pictures/about/%s' % (filename)
    return path


class About(SeoAbstract):
    """ Запись с информацией о нам """
    youtube_url = models.CharField('Часть ссылки на видео на YouTube', max_length=100, default='ccuQoF0vKYU')
    about_company = models.TextField('О компании')
    about_company_picture = StdImageField('Изображение О компании', upload_to=generate_picture_path,
                                          variations={
                                              'w3000': (3000, 2000),
                                              'admin': (90, 60),
                                              'thumb': (15, 10),
                                          }, )
    about_factory = models.TextField('О заводе')
    about_factory_picture = StdImageField('Изображение О заводе', upload_to=generate_picture_path,
                                          variations={
                                              'w3000': (3000, 2000),
                                              'admin': (90, 60),
                                              'thumb': (15, 10),
                                          }, )
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Страница Завод'
        verbose_name_plural = 'Страница Завод'

    def __str__(self):
        return f'Страница Завод'
