from django.contrib import admin

from .models import Contacts, Message


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """ Управление страницей Контакты из панели администратора """
    fieldsets = (
        ('SEO', {
            'fields': (
                ('seo_title',),
                ('seo_description',),
            )
        }),
        ('Карта', {
           'fields': (
               ('map_link',),
               ('map_picture',),
               ('alt_picture',),
               ('map_picture_footer',),
               ('alt_picture_footer',),
           )
        }),
        ('Производство', {
            'fields': (
                ('address',),
                ('email',),
                ('phone_number',),
                ('working_hours',),

            )
        }),
        ('Офис', {
            'fields': (
                ('address_office',),
                ('email_office',),
                ('phone_number_office',),
                ('working_hours_office',),

            )
        }),
    )

    def has_add_permission(self, request, obj=None):
        if Contacts.objects.all().count() >= 1:
            return False
        else:
            return True


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """ Управление сообщениями со страницы Контакты из админ панели """
    list_display = ('id', 'username', 'processed', 'created')
    list_display_links = ('id', 'username',)
    list_editable = ('processed',)
    readonly_fields = ('id', 'username', 'email', 'phone_number', 'message', 'created')
    list_filter = ('processed', 'created')
    search_fields = ('id', 'username', 'email', 'phone_number', 'message')

    def has_add_permission(self, request, obj=None):
        return False
