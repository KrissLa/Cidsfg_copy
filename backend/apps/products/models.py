from ckeditor.fields import RichTextField
from django.db import models
from loguru import logger
from stdimage import StdImageField
from backend.apps.seo.models import SeoAbstract
from django.urls import reverse


class Catalog(SeoAbstract):
    """ Модель для настройки каталога """
    card_text = RichTextField(verbose_name='Текст для карточки для заказа индивидуального проекта', null=True,
                              blank=True)
    modal_text = RichTextField(verbose_name='Текст для модального окна для заказа индивидуального проекта',
                               null=True, blank=True)

    class Meta:
        verbose_name = 'Настройки каталога'
        verbose_name_plural = 'Настройки каталога'

    def __str__(self):
        return 'Настройки каталога'


class House(SeoAbstract):
    """ Моделль дома """
    name = models.CharField('Название', max_length=255, help_text='Полное название дома')
    category = models.ForeignKey('Category', verbose_name='Категория по этажам',
                                 on_delete=models.SET_NULL, null=True,
                                 help_text='Для сортировки и навигации по этажам. Если не выбрать, '
                                           'дом не будет отображен', related_name='houses')
    series = models.ForeignKey('Series', verbose_name='Серия', on_delete=models.SET_NULL, null=True,
                               help_text='Для сортировки и навигации по сериям. Если не выбрать, дом не '
                                         'будет отображен.', related_name='houses')
    slug = models.SlugField('SLUG',
                            help_text='Формируется автоматически из названия. Можно изменить. '
                                      'Максимум 50 символов. Будет использован для построения адреса к дому.',
                            unique=True)
    area = models.PositiveSmallIntegerField('Площадь дома', default=48)
    number_of_rooms = models.PositiveSmallIntegerField('Количество комнат', default=3)
    number_of_bathrooms = models.PositiveSmallIntegerField('Количество санузлов', default=1)
    area_of_buildings = models.PositiveSmallIntegerField('Площадь застройки', default=32)
    height = models.FloatField('Высота', default=4.90)
    width = models.FloatField('Ширина', default=6.60)
    length = models.FloatField('Длина', default=5.00)
    ceiling_height = models.CharField('Высота потлков', max_length=50, help_text='Например: 2.50-4.62',
                                      default='2.50-4.62')

    active = models.BooleanField('Отображать', default=True,
                                 help_text='Уберите, чтобы скрыть дом с сайта.')
    sort_number = models.PositiveSmallIntegerField('Номер в каталоге',
                                                   help_text='Этот номер будет использован для построения домов в'
                                                             ' каталоге. (Дом с меньшим номером будет выше)',
                                                   blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    catalog_price = models.PositiveIntegerField('Стоимость в каталоге', default=0)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ['sort_number', '-id']

    def __str__(self):
        return f'{self.id} - {self.name}'

    def save(self, *args, **kwargs):
        self.category = self.series.category
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('house_detail', kwargs={'category_slug': self.category.slug,
                                               'series_slug': self.series.slug,
                                               'slug': self.slug})

    def get_pictures(self):
        return self.house_pictures.filter(active=True)

    def get_main_picture(self):
        try:
            try:
                pic = self.house_pictures.filter(active=True, main=True)[0]
            except Exception:
                pic = self.house_pictures.filter(active=True)[0]
        except Exception:
            pic = None
        return pic

    def get_price(self):
        try:
            price = min([p['price'] for p in self.configurations.values('price') if p['price'] != 0])
            self.catalog_price = price
            logger.success(f'Для дома {self.name} установлена стоимость {price}')
        except ValueError:
            logger.error(f'в доме {self.name} для комлектаций не указаны цены.')
        self.save()


def generate_picture_path(instance, filename):
    return 'pictures/products/house_pictures/%s/%s/%s/%s' % (instance.house.category.name,
                                                             instance.house.series.name,
                                                             instance.house.name,
                                                             filename)


class HousePicture(models.Model):
    """ Изображения дома"""
    picture = StdImageField('Изображение', upload_to=generate_picture_path,
                            variations={
                                'w1000': (1000, 667),
                                'w720': (720, 480),
                                'w450': (450, 300),
                                'admin': (90, 60),
                                'thumb': (15, 10),
                            }, )
    house = models.ForeignKey(House, verbose_name='Дом, к которому относятся фотографии', on_delete=models.CASCADE,
                              related_name='house_pictures')
    active = models.BooleanField('Отображать', default=True, help_text='Уберите, чтобы не отображать')
    main = models.BooleanField('Картинка для каталога', default=False,
                               help_text='Установите, чтобы сделать картинкой каталога')
    alt = models.CharField('SEO alt', max_length=70, blank=True,
                           help_text='Используется в случае, если изображение не загрузилось или для скринридеров. '
                                     'Гугл может ругаться, если его не будет. Должно содержать краткое описание '
                                     'изображения. Например: "Дом BENT F48 Вид сбоку"')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['id', ]

    def __str__(self):
        return f'Изображение дома {self.house.name}'


class Options(models.Model):
    """ Опции и дополнения дома """
    house = models.OneToOneField(House, verbose_name='Дом, к которому относятся опции', on_delete=models.CASCADE,
                                 related_name='options')
    body = models.TextField('Текст', null=True, blank=True)
    active = models.BooleanField('Отображать', default=True, help_text='Уберите, чтобы не отображать')

    class Meta:
        verbose_name = 'Опции и дополнения'
        verbose_name_plural = 'Опции и дополнения'

    def __str__(self):
        return f'{self.house}  - Опции и дополнения'


class HouseAdditionCategory(models.Model):
    """ Катагория дополнительных штук, которые прилагаются к дому в зависимости от выбранной комплектации """
    name = models.CharField('Категория',
                            help_text='Название категории дополнительных штук, которые прилагаются к дому в '
                                      'зависимости от выбранной комплектации',
                            max_length=100,
                            unique=True)

    class Meta:
        verbose_name = 'Категория дополниния'
        verbose_name_plural = 'Категории дополниний'

    def __str__(self):
        return f'{self.id}. {self.name}'


class HouseAddition(models.Model):
    """ Дополнительные штуки, которые прилагаются к дому в зависимости от выбранной комплектации """
    category = models.ForeignKey(HouseAdditionCategory, verbose_name='Категория', on_delete=models.CASCADE)
    body = models.CharField('Дополнительная штука, которая прилагается к дому в зависимости от выбранной комплектации',
                            max_length=500, unique=True)

    class Meta:
        verbose_name = 'Дополнение'
        verbose_name_plural = 'Дополнения'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}. {self.body} ({self.category.name})'


class Configuration(models.Model):
    """ Модель комплектации с дефолтными значениями """
    name = models.CharField('Название комплектации', max_length=100)
    description = models.TextField('Короткое описание комплектации')
    included_in_price = models.ManyToManyField(HouseAddition,
                                               verbose_name='Дополнительные штуки, которые входят в комплектацию',
                                               related_name='included_default', blank=True)
    not_included_in_price = models.ManyToManyField(HouseAddition,
                                                   verbose_name='Дополнительные штуки, которые не входят в '
                                                                'комплектацию',
                                                   related_name='not_included_default',
                                                   blank=True)

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'
        ordering = ['id']

    def __str__(self):
        return self.name


# комплектация


class ConfigurationInHouses(models.Model):
    """ Модель комплектации дома """
    house = models.ForeignKey(House, verbose_name='Комплектация', on_delete=models.CASCADE,
                              related_name='configurations')
    configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE, verbose_name='Комплектации')
    price = models.PositiveIntegerField('Стоимость комплектации', default=0)
    included_in_price = models.ManyToManyField(HouseAddition,
                                               verbose_name='Дополнительные штуки, которые входят в комплектацию',
                                               related_name='included', blank=True)
    not_included_in_price = models.ManyToManyField(HouseAddition,
                                                   verbose_name='Дополнительные штуки, которые не входят в '
                                                                'комплектацию',
                                                   related_name='not_included',
                                                   blank=True)

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'
        ordering = ['id']
        unique_together = ['house', 'configuration']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.house.get_price()

    def __str__(self):
        return f'Комплектация {self.configuration.name}'

    def get_included(self):
        result = []
        if self.included_in_price.count():
            res = self.included_in_price.values('category', 'category__name', 'body').order_by('category')
        else:
            res = self.configuration.included_in_price.values('category', 'category__name', 'body').order_by('category')
        for r in res:
            cat_is_not_exist = True
            for i in result:
                if result:
                    if r['category'] == i['id']:
                        i['body'].append(r['body'])
                        cat_is_not_exist = False
                        break
            if cat_is_not_exist:
                result.append({'id': r['category'], 'category_name': r['category__name'], 'body': [r['body']]})
        return result

    def get_not_included(self):
        if self.not_included_in_price.count():
            return self.not_included_in_price.order_by('category')
        else:
            return self.configuration.not_included_in_price.values('body').order_by('category')


class Category(models.Model):
    """ Модель категорий по этажам """
    name = models.CharField('Название категории', max_length=255, help_text='Например: "Одноэтажные"')
    slug = models.SlugField('SLUG',
                            help_text='Формируется автоматически из названия. Можно изменить. Максимум 50 символов. '
                                      'Будет использован для построения адреса к категории и домам.', unique=True)
    active = models.BooleanField('Отображать', default=True,
                                 help_text='Уберите, чтобы скрыть категорию и расположенные в ней дома с сайта.')
    coming_soon = models.BooleanField('Скоро', default=False,
                                      help_text='Установите, чтобы отобразить категорию в меню с пометкой "Скоро"')
    sort_number = models.PositiveSmallIntegerField('Номер в меню',
                                                   help_text='Этот номер будет использован для построения категорий в'
                                                             ' меню. (Категория с меньшим номером будет выше)',
                                                   blank=True, null=True)

    class Meta:
        verbose_name = 'Категория по этажам'
        verbose_name_plural = 'Категории по этажам'
        ordering = ['sort_number', 'id']

    def __str__(self):
        return f'{self.id}  - {self.name}'

    def get_series(self):
        return self.series.filter(active=True).order_by('sort_number')

    def get_absolute_url(self):
        # return reverse('catalog_by_category', args=[self.slug])
        return f'url_pass'


def generate_picture_to_series_path(instance, filename):
    return 'pictures/products/series/%s/%s' % (instance.name,
                                               filename)


class Series(SeoAbstract):
    """ Модель категорий по сериям """
    category = models.ForeignKey(Category, verbose_name='Категория дома', on_delete=models.SET_NULL, null=True,
                                 related_name='series')
    name = models.CharField('Название серии', max_length=255, help_text='Например: "FLAT"')
    slug = models.SlugField('SLUG',
                            help_text='Формируется автоматически из названия. Можно изменить. Максимум 50 символов. '
                                      'Будет использован для построения адреса к категории и домам.', unique=True
                            )

    picture = models.ImageField('Изображение серии дома', help_text="В формате png, максимальная ширина - 150px",
                                upload_to=generate_picture_to_series_path, null=True)

    active = models.BooleanField('Отображать', default=True,
                                 help_text='Уберите, чтобы скрыть категорию и расположенные в ней дома с сайта.')
    sort_number = models.PositiveSmallIntegerField('Номер в меню',
                                                   help_text='Этот номер будет использован для построения серий в'
                                                             ' меню. (Серия с меньшим номером будет выше)',
                                                   blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Серия домов'
        verbose_name_plural = 'Серии домов'
        ordering = ['sort_number', 'id']

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_absolute_url(self):
        return reverse('houses_list_by_series', kwargs={'series_slug': self.slug})

    def get_houses(self):
        return self.houses.filter(active=True,
                                  category__active=True)
