from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.safestring import mark_safe
from nested_admin.nested import NestedTabularInline, NestedStackedInline, NestedModelAdmin

from .models import House, Category, Series, HousePicture, Options, Catalog, Configuration, \
    HouseAdditionCategory, HouseAddition, ConfigurationInHouses


# Формы
class SelectForm(forms.ModelForm):
    addition_queryset = HouseAddition.objects.all()
    included_in_price = forms.ModelMultipleChoiceField(required=False,
                                                       queryset=addition_queryset,
                                                       label='Входит в стоимость',
                                                       widget=FilteredSelectMultiple(
                                                           verbose_name='Дополнительные штуки', is_stacked=False))
    not_included_in_price = forms.ModelMultipleChoiceField(required=False,
                                                           queryset=addition_queryset,
                                                           label='Не входит в стоимость',
                                                           widget=FilteredSelectMultiple(
                                                               verbose_name='Дополнительные штуки', is_stacked=False))

    class Meta:
        model = Configuration
        fields = '__all__'


class AdminCKEditorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())


class OptionsAdminForm(AdminCKEditorForm):
    class Meta:
        model = Options
        fields = '__all__'


class CatalogAdminCKEditorForm(forms.ModelForm):
    card_text = forms.CharField(required=False,
                                widget=CKEditorWidget(), label='Текст для карточки для заказа индивидуального проекта')
    modal_text = forms.CharField(required=False,
                                 label='Текст для модального окна для заказа индивидуального проекта',
                                 widget=CKEditorWidget())

    class Meta:
        model = Catalog
        fields = ('card_text', 'modal_text')


class ConfigurationInHousesAdminInline(StackedInline):
    """ Управление комплектациями дома """
    model = ConfigurationInHouses
    sortable_options = ['id']
    extra = 0
    form = SelectForm


## Опции
class OptionsAdminInline(NestedStackedInline):
    """ Управление опциями дома  """
    model = Options
    form = OptionsAdminForm


## Pictures


class HousePictureAdminInline(NestedTabularInline):
    """Добавление фотографий к дому"""
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


@admin.register(House)
class HouseAdmin(NestedModelAdmin):
    """ Управление домами из панели администратора """
    list_display = ('id', 'name', 'active', 'sort_number')
    list_display_links = ('id', 'name',)
    list_editable = ('active', 'sort_number')
    save_on_top = True
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        ('SEO', {
            'fields': (
                ('seo_title',),
                ('seo_description',),
                ('seo_og_title',),
                ('seo_og_image',),
            )
        }),
        (
            'Общая информация', {
                'fields': ('name', 'slug', 'series')
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
               ConfigurationInHousesAdminInline]


@admin.register(Category)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Series)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    """ Управление каталогом из панели администратора """
    form = CatalogAdminCKEditorForm
    fieldsets = (
        ('SEO', {
            'fields': (
                ('seo_title',),
                ('seo_description',),
                ('seo_og_title',),
                ('seo_og_image',),
            )
        }),
        (
            'Уникальный проект', {
                'fields': ('card_text', 'modal_text')
            },
        ),
    )

    def has_add_permission(self, request, obj=None):
        if Catalog.objects.all().count() >= 1:
            return False
        else:
            return True


@admin.register(HouseAdditionCategory)
class HouseAdditionCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(HouseAddition)
class HouseAdditionAdmin(admin.ModelAdmin):
    pass


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    form = SelectForm
