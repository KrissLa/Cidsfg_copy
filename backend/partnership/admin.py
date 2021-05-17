from django.contrib import admin

# Register your models here.
from .models import CooperationApplication


@admin.register(CooperationApplication)
class CooperationApplicationAdmin(admin.ModelAdmin):
    """ Управление заявками на сотрудничество из админ панели """
    list_display = ('id', 'company_type', 'processed', 'created')
    list_display_links = ('id', 'company_type',)
    list_editable = ('processed',)
    readonly_fields = (
        'id', 'area_of_activity', 'company_type', 'company_name', 'firs_name', 'last_name', 'email', 'phone_number',
        'created')
    list_filter = ('processed', 'created', 'area_of_activity', 'company_type')
    search_fields = ('id', 'company_name', 'firs_name', 'last_name', 'email')

    def has_add_permission(self, request, obj=None):
        return False
