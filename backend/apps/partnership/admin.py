from django.contrib import admin

from .models import Partnership


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
