from django.db import models
from backend.seo.models import SeoAbstract


# Create your models here.
from django.urls import reverse


class House(SeoAbstract):
    """ Моделль дома """
    house_name = models.CharField('Название', max_length=255, help_text='Полное название дома')
    house_category = models.ForeignKey('Category', verbose_name='Категория по этажам',
                                               on_delete=models.SET_NULL, null=True,
                                               help_text='Для сортировки и навигации по этажам. Если не выбрать, '
                                                         'дом не будет отображен')
    house_series = models.ForeignKey('Series', verbose_name='Серия', on_delete=models.SET_NULL, null=True,
                                     help_text='Для сортировки и навигации по сериям. Если не выбрать, дом не '
                                               'будет отображен.')
    house_slug = models.SlugField('SLUG',
                                  help_text='Формируется автоматически из названия. Можно изменить. '
                                            'Максимум 50 символов. Будет использован для построения адреса к дому.')
    house_active = models.BooleanField('Отображать', default=True,
                                       help_text='Уберите, чтобы скрыть дом с сайта.')

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return f'{self.id} - {self.house_name}'





class Category(SeoAbstract):
    """ Модель категорий по этажам """
    category_name = models.CharField('Название категории', max_length=255, help_text='Например: "Одноэтажные"')
    category_slug = models.SlugField('SLUG',
                                  help_text='Формируется автоматически из названия. Можно изменить. Максимум 50 символов. '
                                            'Будет использован для построения адреса к категории и домам.')
    category_active = models.BooleanField('Отображать', default=True,
                                       help_text='Уберите, чтобы скрыть категорию и расположенные в ней дома с сайта.')
    category_coming_soon = models.BooleanField('Скоро', default=False,
                                            help_text='Установите, чтобы отобразить категорию в меню с пометкой "Скоро"')

    class Meta:
        verbose_name = 'Категория по этажам'
        verbose_name_plural = 'Категории по этажам'

    def __str__(self):
        return f'{self.id}  - {self.category_name}'

    def get_absolute_url(self):
        return reverse('catalog_by_category', args=[self.category_slug])


class Series(SeoAbstract):
    """ Модель категорий по сериям """
    series_name = models.CharField('Название серии', max_length=255, help_text='Например: "Серия FR"')
    series_slug = models.SlugField('SLUG',
                                   help_text='Формируется автоматически из названия. Можно изменить. Максимум 50 символов. '
                                             'Будет использован для построения адреса к категории и домам.'
                                   )
    series_active = models.BooleanField('Отображать', default=True,
                                        help_text='Уберите, чтобы скрыть категорию и расположенные в ней дома с сайта.')
    series_coming_soon = models.BooleanField('Скоро', default=False,
                                             help_text='Установите, чтобы отобразить серию в меню с помоткой скоро')

    class Meta:
        verbose_name = 'Серия домов'
        verbose_name_plural = 'Серии домов'

    def __str__(self):
        return f'{self.id} - {self.series_name}'

    def get_absolute_url(self):
        return reverse('catalog_by_category', args=[self.series_slug])
