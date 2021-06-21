from ckeditor.fields import RichTextField
from django.db import models
from stdimage import StdImageField
from backend.apps.seo.models import SeoAbstract

# Create your models here.
from django.urls import reverse


class TabBodyAbstract(models.Model):
    """Абстрактная модель, включающая описание"""
    body = models.TextField('Текст', null=True, blank=True)

    class Meta:
        abstract = True


class ActiveAbstract(models.Model):
    """Абстрактная модель, включающаястатус отображения"""
    active = models.BooleanField('Отображать', default=True, help_text='Уберите, чтобы не отображать')

    class Meta:
        abstract = True


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
    price_min = models.PositiveIntegerField('Стоимость комплектации "Поставка с завода"', default=0)
    price_medium = models.PositiveIntegerField('Стоимость комплектации "Под ключ"', default=0)
    price_full = models.PositiveIntegerField('Стоимость комплектации "Под ключ"', default=0)
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
    sort_number = models.PositiveSmallIntegerField('Номер в каталоге', unique=True,
                                                   help_text='Этот номер будет использован для построения домов в'
                                                             ' каталоге. (Дом с меньшим номером будет выше)',
                                                   blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ['sort_number', '-id']

    def __str__(self):
        return f'{self.id} - {self.name}'

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


def generate_picture_path(instance, filename):
    path = 'pictures/products/house_pictures/%s/%s/%s/%s' % (instance.house.category.name,
                                                             instance.house.series.name,
                                                             instance.house.name,
                                                             filename)
    return path


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


class Options(TabBodyAbstract, ActiveAbstract):
    """ Опции и дополнения дома """
    house = models.OneToOneField(House, verbose_name='Дом, к которому относятся опции', on_delete=models.CASCADE,
                                 related_name='options')

    class Meta:
        verbose_name = 'Опции и дополнения'
        verbose_name_plural = 'Опции и дополнения'

    def __str__(self):
        return f'{self.house}  - Опции и дополнения'


# "Под мебель"


class Turnkey(ActiveAbstract):
    """ Комплектация под мебель """
    house = models.OneToOneField(House, verbose_name='Дом, к которому относится комплектация', on_delete=models.CASCADE,
                                 related_name='turnkey')

    class Meta:
        verbose_name = 'Комплектация "Под мебель"'
        verbose_name_plural = 'Комплектация "Под мебель"'

    def __str__(self):
        return f'{self.house} - Комплектация "Под мебель"'


class NotIncludedInPriceTurnkey(TabBodyAbstract, ActiveAbstract):
    """ Вкладка  Не Включено в стоимость  ПОД мебель"""
    turnkey = models.OneToOneField(Turnkey, verbose_name='Комплектация "Под мебель"', on_delete=models.CASCADE,
                                   related_name='not_included')

    class Meta:
        verbose_name = 'Вкладка "Не включено в стоимость" "Под мебель"'
        verbose_name_plural = 'Вкладка "Не включено в стоимость" "Под мебель"'

    def __str__(self):
        return f'{self.turnkey.house} - Вкладка "Не включено в стоимость" "Под мебель"'


class IncludedInPriceTurnkey(ActiveAbstract):
    """ Вкладка Включено в стоимость  """
    turnkey = models.OneToOneField(Turnkey, verbose_name='Комплектация "Под мебель"', on_delete=models.CASCADE,
                                   related_name='included')

    class Meta:
        verbose_name = 'Вкладка "Включено в стоимость" "Под мебель"'
        verbose_name_plural = 'Вкладки "Включено в стоимость" "Под мебель"'

    def __str__(self):
        return f'{self.turnkey.house} - Вкладка "Включено в стоимость" "Под мебель"'

    def get_items(self):
        return self.items.filter(active=True)


class IncludedInPriceTurnkeyItem(TabBodyAbstract, ActiveAbstract):
    """ Пункт вкладки включено в стоимость """
    included_in_price = models.ForeignKey(IncludedInPriceTurnkey, verbose_name='Вкладка "Включено в стоимость"',
                                          on_delete=models.CASCADE, related_name='items')
    name = models.CharField('Название пункта', max_length=50)

    class Meta:
        verbose_name = 'Пункт вкладки "Включено в стоимость" "Под мебель"'
        verbose_name_plural = 'Пункты вкладки "Включено в стоимость" "Под мебель"'

    def __str__(self):
        return f'{self.included_in_price.turnkey.house} - Пункт вкладки "Включено в стоимость" "Под мебель"'


# "Под ключ"


class ForFinishing(ActiveAbstract):
    """ Комплектация ПОД ключ """
    house = models.OneToOneField(House, verbose_name='Дом, к которому относится комплектация', on_delete=models.CASCADE,
                                 related_name='for_finishing')

    class Meta:
        verbose_name = 'Комплектация "Под ключ"'
        verbose_name_plural = 'Комплектация "Под ключ"'

    def __str__(self):
        return f'{self.house} - Комплектация "Под ключ"'


class NotIncludedInPriceForFinishing(TabBodyAbstract, ActiveAbstract):
    """ Вкладка  Не Включено в стоимость  ПОД ключ """
    for_finishing = models.OneToOneField(ForFinishing, verbose_name='Комплектация "Под ключ"',
                                         on_delete=models.CASCADE, related_name='not_included')

    class Meta:
        verbose_name = 'Вкладка "Не включено в стоимость" "Под ключ"'
        verbose_name_plural = 'Вкладка "Не включено в стоимость" "Под ключ"'

    def __str__(self):
        return f'{self.for_finishing.house} - Вкладка "Не включено в стоимость" "Под ключ"'


class IncludedInPriceForFinishing(ActiveAbstract):
    """ Вкладка Включено в стоимость  ПОД ключ """
    for_finishing = models.OneToOneField(ForFinishing, verbose_name='Комплектация "Под ключ"',
                                         on_delete=models.CASCADE, related_name='included')

    class Meta:
        verbose_name = 'Вкладка "Включено в стоимость" "Под ключ"'
        verbose_name_plural = 'Вкладка "Включено в стоимость" "Под ключ"'

    def __str__(self):
        return f'{self.for_finishing.house} - Вкладка "Включено в стоимость" "Под ключ"'

    def get_items(self):
        return self.items.filter(active=True)


class IncludedInPriceForFinishingItem(TabBodyAbstract, ActiveAbstract):
    """ Пункт вкладки включено в стоимость ПОД ключ """
    included_in_price = models.ForeignKey(IncludedInPriceForFinishing,
                                          verbose_name='Вкладка "Включено в стоимость" "Под ключ"',
                                          on_delete=models.CASCADE, related_name='items')
    name = models.CharField('Название пункта', max_length=50)

    class Meta:
        verbose_name = 'Пункт вкладки "Включено в стоимость" "Под ключ"'
        verbose_name_plural = 'Пункты вкладки "Включено в стоимость" "Под ключ"'

    def __str__(self):
        return f'{self.included_in_price.for_finishing.house} - Пункт вкладки "Включено в стоимость" "Под ключ"'


# "Поставка с завода"


class Delivery(ActiveAbstract):
    """ Комплектация ПОСТАВКА С ЗАВОДА """
    house = models.OneToOneField(House, verbose_name='Дом, к которому относится комплектация', on_delete=models.CASCADE,
                                 related_name='delivery')

    class Meta:
        verbose_name = 'Комплектация "Поставка с завода"'
        verbose_name_plural = 'Комплектация "Поставка с завода"'

    def __str__(self):
        return f'{self.house} - Комплектация "Поставка с завода"'


class NotIncludedInPriceDelivery(TabBodyAbstract, ActiveAbstract):
    """ Вкладка  Не Включено в стоимость  ПОСТАВКА С ЗАВОДА"""
    delivery = models.OneToOneField(Delivery, verbose_name='Комплектация "Поставка с завода"',
                                    on_delete=models.CASCADE, related_name='not_included')

    class Meta:
        verbose_name = 'Вкладка "Не включено в стоимость ПОСТАВКА С ЗАВОДА"'
        verbose_name_plural = 'Вкладка "Не включено в стоимость ПОСТАВКА С ЗАВОДА"'

    def __str__(self):
        return f'{self.delivery.house} - Вкладка "Не включено в стоимость ПОСТАВКА С ЗАВОДА"'


class IncludedInPriceDelivery(ActiveAbstract):
    """ Вкладка Включено в стоимость "Поставка с завода" """
    delivery = models.OneToOneField(Delivery, verbose_name='Комплектация "Поставка с завода"',
                                    on_delete=models.CASCADE, related_name='included')

    class Meta:
        verbose_name = 'Вкладка "Включено в стоимость "Поставка с завода""'
        verbose_name_plural = 'Вкладка "Включено в стоимость "Поставка с завода""'

    def __str__(self):
        return f'{self.delivery.house} - Вкладка "Включено в стоимость "Поставка с завода""'

    def get_items(self):
        return self.items.filter(active=True)


class IncludedInPriceDeliveryItem(TabBodyAbstract, ActiveAbstract):
    """ Пункт вкладки включено в стоимость "Поставка с завода" """
    included_in_price = models.ForeignKey(IncludedInPriceDelivery,
                                          verbose_name='Вкладка "Включено в стоимость" "Поставка с завода"',
                                          on_delete=models.CASCADE, related_name='items')
    name = models.CharField('Название пункта', max_length=50)

    class Meta:
        verbose_name = 'Пункт вкладки включено в стоимость "Поставка с завода"'
        verbose_name_plural = 'Пункты вкладки включено в стоимость "Поставка с завода"'

    def __str__(self):
        return f'{self.included_in_price.delivery.house} - Пункт вкладки "Включено в стоимость" "Поставка с завода"'


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
    sort_number = models.PositiveSmallIntegerField('Номер в меню', unique=True,
                                                   help_text='Этот номер будет использован для построения категорий в'
                                                             ' меню. (Категория с меньшим номером будет выше)',
                                                   blank=True, null=True)

    class Meta:
        verbose_name = 'Категория по этажам'
        verbose_name_plural = 'Категории по этажам'

    def __str__(self):
        return f'{self.id}  - {self.name}'

    def get_series(self):
        return self.series.filter(active=True).order_by('sort_number')

    def get_absolute_url(self):
        # return reverse('catalog_by_category', args=[self.slug])
        return f'url_pass'


def generate_picture_to_series_path(instance, filename):
    path = 'pictures/products/series/%s/%s' % (instance.name,
                                               filename)
    return path


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
    sort_number = models.PositiveSmallIntegerField('Номер в меню', unique=True,
                                                   help_text='Этот номер будет использован для построения серий в'
                                                             ' меню. (Серия с меньшим номером будет выше)',
                                                   blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Серия домов'
        verbose_name_plural = 'Серии домов'

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_absolute_url(self):
        return reverse('houses_list_by_series', kwargs={'series_slug': self.slug})

    def get_houses(self):
        return self.houses.filter(active=True,
                                  category__active=True)


####


class ConsultationRequest(models.Model):
    """ Модель заявки на консультацию со страницы с подробным описанием дома """
    username = models.CharField('Имя пользователя', max_length=255)
    type_of_contact = models.CharField('Куда ответить', max_length=100, default='Мобильный')
    contact = models.CharField('Контакт', max_length=255, default='')
    message = models.TextField('Сообщение пользователя', blank=True, null=True)
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    house_name = models.CharField('Название модели дома, со страницы которого отправлена заявка', max_length=100)
    created = models.DateTimeField('Время отправки сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'

    def __str__(self):
        if self.processed:
            processed = ''
        else:
            processed = '(Новая!)'
        return f'Заявка на консультацию № {self.id} от пользователя {self.username}. {processed}'
