from django.db import models
from backend.seo.models import SeoAbstract

# Create your models here.
from django.urls import reverse


class House(SeoAbstract):
    """ Моделль дома """
    name = models.CharField('Название', max_length=255, help_text='Полное название дома')
    category = models.ForeignKey('Category', verbose_name='Категория по этажам',
                                 on_delete=models.SET_NULL, null=True,
                                 help_text='Для сортировки и навигации по этажам. Если не выбрать, '
                                           'дом не будет отображен')
    series = models.ForeignKey('Series', verbose_name='Серия', on_delete=models.SET_NULL, null=True,
                               help_text='Для сортировки и навигации по сериям. Если не выбрать, дом не '
                                         'будет отображен.')
    slug = models.SlugField('SLUG',
                            help_text='Формируется автоматически из названия. Можно изменить. '
                                      'Максимум 50 символов. Будет использован для построения адреса к дому.')
    active = models.BooleanField('Отображать', default=True,
                                 help_text='Уберите, чтобы скрыть дом с сайта.')

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Category(SeoAbstract):
    """ Модель категорий по этажам """
    name = models.CharField('Название категории', max_length=255, help_text='Например: "Одноэтажные"')
    slug = models.SlugField('SLUG',
                            help_text='Формируется автоматически из названия. Можно изменить. Максимум 50 символов. '
                                      'Будет использован для построения адреса к категории и домам.')
    active = models.BooleanField('Отображать', default=True,
                                 help_text='Уберите, чтобы скрыть категорию и расположенные в ней дома с сайта.')
    coming_soon = models.BooleanField('Скоро', default=False,
                                      help_text='Установите, чтобы отобразить категорию в меню с пометкой "Скоро"')

    class Meta:
        verbose_name = 'Категория по этажам'
        verbose_name_plural = 'Категории по этажам'

    def __str__(self):
        return f'{self.id}  - {self.name}'

    def get_absolute_url(self):
        # return reverse('catalog_by_category', args=[self.slug])
        return f'url_pass'

class Series(SeoAbstract):
    """ Модель категорий по сериям """
    name = models.CharField('Название серии', max_length=255, help_text='Например: "Серия FR"')
    slug = models.SlugField('SLUG',
                            help_text='Формируется автоматически из названия. Можно изменить. Максимум 50 символов. '
                                      'Будет использован для построения адреса к категории и домам.'
                            )
    active = models.BooleanField('Отображать', default=True,
                                 help_text='Уберите, чтобы скрыть категорию и расположенные в ней дома с сайта.')
    coming_soon = models.BooleanField('Скоро', default=False,
                                      help_text='Установите, чтобы отобразить серию в меню с помоткой скоро')

    class Meta:
        verbose_name = 'Серия домов'
        verbose_name_plural = 'Серии домов'

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_absolute_url(self):
        # return reverse('catalog_by_category', args=[self.slug])
        return f'url_pass'