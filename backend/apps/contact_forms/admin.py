from django.contrib import admin
from .models import IndividualProjectRequest


@admin.register(IndividualProjectRequest)
class IndividualProjectRequestAdmin(admin.ModelAdmin):
    """ Управление заявками на индивидуальный проект из админ панели """
    list_display = ('id', 'username', 'processed', 'created')
    list_display_links = ('id', 'username',)
    list_editable = ('processed',)
    readonly_fields = ('id', 'number_of_floors', 'area', 'number_of_rooms', 'number_of_bathrooms', 'garage_is_needed',
                       'comment', 'username', 'type_of_contact', 'contact', 'created')
    list_filter = ('processed', 'created', 'type_of_contact')
    search_fields = ('id', 'username', 'message')

    def has_add_permission(self, request, obj=None):
        return False
