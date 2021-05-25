from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from nested_admin.nested import NestedTabularInline, NestedStackedInline, NestedModelAdmin

from .models import House, Category, Series, HousePicture, Options, Turnkey, IncludedInPriceTurnkey, \
    IncludedInPriceTurnkeyItem, NotIncludedInPriceTurnkey, NotIncludedInPriceForFinishing, \
    IncludedInPriceForFinishingItem, NotIncludedInPriceDelivery, IncludedInPriceDeliveryItem, \
    IncludedInPriceForFinishing, IncludedInPriceDelivery, Delivery, ForFinishing, ConsultationRequest


# Заявки на консультацию

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    """ Управление заявками на консультацию """
    list_display = ('id', 'username', 'processed', 'created')
    list_display_links = ('id', 'username',)
    list_editable = ('processed',)
    readonly_fields = ('id', 'username', 'email', 'phone_number', 'message', 'house_name', 'created', )
    list_filter = ('processed', 'created', 'house_name',)
    search_fields = ('id', 'username', 'email', 'phone_number', 'house_name', 'message')

    def has_add_permission(self, request, obj=None):
        return False

# Формы


class AdminCKEditorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())


class OptionsAdminForm(AdminCKEditorForm):
    class Meta:
        model = Options
        fields = '__all__'


## Turnkey


class IncludedInPriceItemTurnkeyAdminForm(AdminCKEditorForm):
    class Meta:
        model = IncludedInPriceTurnkeyItem
        fields = '__all__'


class NotIncludedInPriceTurnkeyAdminForm(AdminCKEditorForm):
    class Meta:
        model = NotIncludedInPriceTurnkey
        fields = '__all__'


## ForFinishing


class IncludedInPriceItemForFinishingAdminForm(AdminCKEditorForm):
    class Meta:
        model = IncludedInPriceForFinishingItem
        fields = '__all__'


class NotIncludedInPriceForFinishingAdminForm(AdminCKEditorForm):
    class Meta:
        model = NotIncludedInPriceForFinishing
        fields = '__all__'


## Delivery


class IncludedInPriceItemDeliveryAdminForm(AdminCKEditorForm):
    class Meta:
        model = IncludedInPriceDeliveryItem
        fields = '__all__'


class NotIncludedInPriceDeliveryAdminForm(AdminCKEditorForm):
    class Meta:
        model = NotIncludedInPriceDelivery
        fields = '__all__'


# ИНлайн

## Опции
class OptionsAdminInline(NestedStackedInline):
    """ Управление опциями дома  """
    model = Options
    form = OptionsAdminForm


## Pictures


class HousePictureAdminInline(NestedTabularInline):
    """добавление фотографий к дому"""
    model = HousePicture
    extra = 3
    readonly_fields = ('get_photo',)
    fieldsets = (
        ('Изображения', {
            'fields': ('picture', 'get_photo', 'house', 'active', 'main', 'alt')
        }),
    )

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.picture.admin.url} width="90">')

    get_photo.short_description = ''


## Turnkey


class NotIncludedInPriceTurnkeyAdminInline(NestedTabularInline):
    """ Управление вкладкой Не включено в стоимость комплектации ПОД мебель """
    model = NotIncludedInPriceTurnkey
    form = NotIncludedInPriceTurnkeyAdminForm


class IncludedInPriceItemTurnkeyAdminInline(NestedTabularInline):
    """ Управление пунктами вкладки Включено в стоимость комплектации ПОД мебель """
    model = IncludedInPriceTurnkeyItem
    form = IncludedInPriceItemTurnkeyAdminForm
    fields = ('name', 'body', 'active')
    extra = 1


class IncludedInPriceTurnkeyAdminInline(NestedStackedInline):
    """ Управление вкладкой Включено в стоимость комплектации ПОД мебель """
    model = IncludedInPriceTurnkey
    inlines = [IncludedInPriceItemTurnkeyAdminInline, ]


class TurnkeyAdminInline(NestedStackedInline):
    """ Управление комплектацией под мебель """
    model = Turnkey
    inlines = [IncludedInPriceTurnkeyAdminInline, NotIncludedInPriceTurnkeyAdminInline]


## ForFinishing


class NotIncludedInPriceForFinishingAdminInline(NestedTabularInline):
    """ Управление вкладкой Не включено в стоимость комплектации ПОД ключ """
    model = NotIncludedInPriceForFinishing
    form = NotIncludedInPriceForFinishingAdminForm


class IncludedInPriceItemForFinishingAdminInline(NestedTabularInline):
    """ Управление пунктами вкладки Включено в стоимость комплектации ПОД ключ """
    model = IncludedInPriceForFinishingItem
    form = IncludedInPriceItemForFinishingAdminForm
    fields = ('name', 'body', 'active')
    extra = 1


class IncludedInPriceForFinishingAdminInline(NestedStackedInline):
    """ Управление вкладкой Включено в стоимость комплектации ПОД ключ """
    model = IncludedInPriceForFinishing
    inlines = [IncludedInPriceItemForFinishingAdminInline, ]


class ForFinishingAdminInline(NestedStackedInline):
    """ Управление комплектацией ПОД ключ """
    model = ForFinishing
    inlines = [IncludedInPriceForFinishingAdminInline, NotIncludedInPriceForFinishingAdminInline]


## Delivery


class NotIncludedInPriceDeliveryAdminInline(NestedTabularInline):
    """ Управление вкладкой Не включено в стоимость комплектации ПОСТАВКА С ЗАВОДА  """
    model = NotIncludedInPriceDelivery
    form = NotIncludedInPriceDeliveryAdminForm


class IncludedInPriceItemDeliveryAdminInline(NestedTabularInline):
    """ Управление пунктами вкладки Включено в стоимость комплектации ПОСТАВКА С ЗАВОДА """
    model = IncludedInPriceDeliveryItem
    form = IncludedInPriceItemDeliveryAdminForm
    fields = ('name', 'body', 'active')
    extra = 1


class IncludedInPriceDeliveryAdminInline(NestedStackedInline):
    """ Управление вкладкой Включено в стоимость комплектации ПОСТАВКА С ЗАВОДА """
    model = IncludedInPriceDelivery
    inlines = [IncludedInPriceItemDeliveryAdminInline, ]


class DeliveryAdminInline(NestedStackedInline):
    """ Управление комплектацией ПОСТАВКА С ЗАВОДА """
    model = Delivery
    inlines = [IncludedInPriceDeliveryAdminInline, NotIncludedInPriceDeliveryAdminInline]




# Вывод


@admin.register(House)
class HouseAdmin(NestedModelAdmin):
    """ Управление домами из панели администратора """
    list_display = ('id', 'name', 'active', 'sort_number')
    list_display_links = ('id', 'name',)
    list_editable = ('active', 'sort_number')
    save_on_top = True
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (
            'SEO', {
                'fields': ('seo_title', 'seo_description')
            },
        ), (
            'Общая информация', {
                'fields': ('name', 'slug', 'category', 'series')
            },
        ), (
            'Стоимость', {
                'fields': ('price_min', 'price_medium', 'price_full')
            },
        ), (
            'Параметры', {
                'fields': (
                    'area', 'area_of_buildings', 'number_of_rooms', 'number_of_bathrooms', 'height', 'width',
                    'length', 'ceiling_height'
                ),
            },
        ), (
            'Настройка в каталоге', {
                'fields': ('active', 'sort_number')
            },
        ),
    )
    inlines = [HousePictureAdminInline,
               OptionsAdminInline,
               TurnkeyAdminInline,
               ForFinishingAdminInline,
               DeliveryAdminInline]


@admin.register(Category)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Series)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"slug": ("name",)}
