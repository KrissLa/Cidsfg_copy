from django.contrib import admin

from .models import Contacts


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
