from django.contrib import admin

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """ Управление страницей Завод из панели администратора """
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
        ('О компании', {
            'fields': (
                ('about_company',),
                ('about_company_picture',),
            )
        }),
        ('О производстве', {
            'fields': (
                ('about_factory',),
                ('about_factory_picture',),
            )
        }),
    )

    def has_add_permission(self, request, obj=None):
        if About.objects.all().count() >= 1:
            return False
        else:
            return True
