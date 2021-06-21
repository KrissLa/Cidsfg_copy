from loguru import logger

from django.contrib import admin
from .models import HomePage

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    """ Управление главной страницей из панели администратора """
    fieldsets = (
        ('SEO', {
            'fields': (
                ('seo_title',),
                ('seo_description',),
            )
        }),
    )

    def has_add_permission(self, request, obj=None):
        if HomePage.objects.all().count() >= 1:
            return False
        else:
            return True