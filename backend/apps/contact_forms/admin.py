from django.contrib import admin
from .models import IndividualProjectRequest, Message, ConsultationRequest, CooperationApplication


@admin.register(IndividualProjectRequest)
class IndividualProjectRequestAdmin(admin.ModelAdmin):
    """ Управление заявками на индивидуальный проект из админ панели """
    list_display = ('id', 'username', 'processed', 'created')
    list_display_links = ('id', 'username',)
    list_editable = ('processed',)
    readonly_fields = ('id', 'number_of_floors', 'area', 'number_of_rooms', 'number_of_bathrooms', 'garage_is_needed',
                       'credit_is_needed', 'credit_amount',
                       'comment', 'username', 'type_of_contact', 'contact', 'created')
    list_filter = ('processed', 'created', 'type_of_contact', 'credit_is_needed')
    search_fields = ('id', 'username', 'message')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """ Управление сообщениями со страницы Контакты из админ панели """
    list_display = ('id', 'username', 'processed', 'created')
    list_display_links = ('id', 'username',)
    list_editable = ('processed',)
    readonly_fields = ('id', 'username', 'type_of_contact', 'contact', 'message', 'created')
    list_filter = ('processed', 'created', 'type_of_contact')
    search_fields = ('id', 'username', 'message')

    def has_add_permission(self, request, obj=None):
        return False


# Заявки на консультацию

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    """ Управление заявками на консультацию """
    list_display = ('id', 'username', 'processed', 'created')
    list_display_links = ('id', 'username',)
    list_editable = ('processed',)
    readonly_fields = (
        'id', 'username', 'type_of_contact', 'contact', 'credit_is_needed', 'credit_amount', 'message', 'house_name',
        'created')
    list_filter = ('processed', 'created', 'house_name', 'type_of_contact', 'credit_is_needed')
    search_fields = ('id', 'username', 'contact', 'house_name', 'message')

    def has_add_permission(self, request, obj=None):
        return False


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
