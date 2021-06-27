from django.contrib import admin
from nested_admin.nested import NestedTabularInline, NestedStackedInline, NestedModelAdmin

from .models import Privacy, PrivacyData, PrivacyPurpose, PrivacyBasis


class PrivacyDataInline(NestedTabularInline):
    """ Управление данными, которые собираются на сайте """
    model = PrivacyData
    fields = ('item',)
    extra = 1


class PrivacyPurposeInline(NestedTabularInline):
    """ Управление целями сбора данных """
    model = PrivacyPurpose
    fields = ('item',)
    extra = 1


class PrivacyBasisInline(NestedTabularInline):
    """ Управление основаниями обработки персональных данных """
    model = PrivacyBasis
    fields = ('item',)
    extra = 1


@admin.register(Privacy)
class PrivacyAdmin(NestedModelAdmin):
    """ Управление политикой конфиденциальности из панели администратора """
    list_display = ('id', 'organization_name',)
    list_display_links = ('id', 'organization_name',)
    save_on_top = True
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
                'fields': ('organization_name', 'email')
            },
        ),
    )
    inlines = [PrivacyDataInline,
               PrivacyPurposeInline,
               PrivacyBasisInline]

    def has_add_permission(self, request, obj=None):
        if Privacy.objects.all().count() >= 1:
            return False
        else:
            return True
