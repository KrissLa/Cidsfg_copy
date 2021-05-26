from django.contrib import admin

# Register your models here.
from .models import CooperationApplication, Partnership


@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    """ Управление страницей Сотрудничество из панели администратора """
    fieldsets = (
        ('SEO', {
            'fields': (
                ('seo_title',),
                ('seo_description',),
            )
        }),
    )

    def has_add_permission(self, request, obj=None):
        if Partnership.objects.all().count() >= 1:
            return False
        else:
            return True


@admin.register(CooperationApplication)
class CooperationApplicationAdmin(admin.ModelAdmin):
    """ Управление заявками на сотрудничество из админ панели """
    list_display = ('id', 'company_type', 'processed', 'created')
    list_display_links = ('id', 'company_type',)
    list_editable = ('processed',)
    readonly_fields = (
        'id', 'area_of_activity', 'company_type', 'company_name', 'firs_name', 'last_name', 'type_of_contact',
        'contact', 'created')
    list_filter = ('processed', 'created', 'area_of_activity', 'company_type', 'type_of_contact')
    search_fields = ('id', 'company_name', 'firs_name', 'last_name', 'email')

    def has_add_permission(self, request, obj=None):
        return False
