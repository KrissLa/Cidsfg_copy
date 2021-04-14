from django.db import models
from backend.seo.models import SeoAbstract

# Create your models here.
from loguru import logger
from rest_framework.reverse import reverse


def generate_picture_path(instance, filename):
    url = 'images/home_decorations/%s/%s/' % (instance.name, filename)
    return url


class HomeDecorationCategory(SeoAbstract):
    """ Категории отделки """
    hd_name = models.CharField('Категория', max_length=255,
                               help_text='Название категории для отделки. Например: Внутренняя коммуникация')
    hd_slug = models.SlugField('Slug', help_text='Будет использован для формирования url. Максимум 50 символов.',
                               unique=True)
    hd_active = models.BooleanField('Отображать', default=True, help_text='Уберите, чтобы скрыть категорию.')
    hd_picture = models.ImageField('Картинка', upload_to='images/home_decorations/', null=True)

    class Meta:
        verbose_name = 'Категория отделки'
        verbose_name_plural = 'Категории отделки'
        ordering = ['id']

    def __str__(self):
        return f'{self.hd_name}'

    def get_absolute_url(self):
        return reverse('home_decorations_subcategories', args=[self.hd_slug])


class HomeDecorationSubCategory(SeoAbstract):
    """ Подкатегории отделки """
    name = models.CharField('Подкатегория', max_length=255)
    slug = models.SlugField('Slug')
    category = models.ForeignKey(HomeDecorationCategory, verbose_name='Категория', on_delete=models.SET_NULL,
                                 null=True, related_name='subcategories')
    active = models.BooleanField('Отображать', default=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        unique_together = ['slug', 'category']
        ordering = ['category', 'id']

    def __str__(self):
        return f'{self.category} - {self.name}'

    def get_absolute_url(self):
        return reverse('home_decorations_subcategory_detail', kwargs={'slug': self.slug, 'category_slug': self.category.hd_slug})


class HomeDecorationType(SeoAbstract):
    """ Модель вида отделки """
    name = models.CharField('Название вида отелки', max_length=255)
    slug = models.SlugField('Slug')
    sub_category = models.ForeignKey(HomeDecorationSubCategory, verbose_name='Подкатегория', on_delete=models.SET_NULL,
                                     null=True, related_name='types')
    active = models.BooleanField('Отображать', default=True)

    class Meta:
        verbose_name = 'Вид отделки'
        verbose_name_plural = 'Виды отделки'
        unique_together = ['slug', 'sub_category']
        ordering = ['sub_category', 'id']

    def __str__(self):
        return f'{self.sub_category} - {self.name}'

    def get_absolute_url(self):
        return reverse('home_decorations_type_detail', kwargs={'slug': self.slug,
                                                               'subcategory_slug': self.sub_category.slug,
                                                               'category_slug': self.sub_category.category.hd_slug})


class HomeDecoration(SeoAbstract):
    """ Модель отделки"""
    name = models.CharField('Название экземпляра отделки', max_length=255)
    slug = models.SlugField('Slug')
    type = models.ForeignKey(HomeDecorationType, verbose_name='Тип отделки', on_delete=models.SET_NULL, null=True,
                             related_name='home_decorations')
    picture = models.ImageField('Изображение', upload_to=generate_picture_path, null=True)
    active = models.BooleanField('Отображать', default=True)

    class Meta:
        verbose_name = 'Экземпляр отделки'
        verbose_name_plural = 'Экземпляры отделки'
        unique_together = ['slug', 'type']
        ordering = ['type', 'id']


    def __str__(self):
        return f'{self.type} - {self.name}'

    def get_absolute_url(self):
        return f'url_here'
