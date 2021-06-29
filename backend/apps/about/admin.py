from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import About


class CapacityBodyAdminCKEditorForm(forms.ModelForm):
    capacity_body = forms.CharField(required=False, widget=CKEditorWidget(),
                                    label='Текст секции "Производственные мощности"')

    class Meta:
        model = About
        fields = ('capacity_body',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """ Управление страницей Завод из панели администратора """
    save_on_top = True
    form = CapacityBodyAdminCKEditorForm
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
                ('about_company_title',),
                ('about_company',),
                ('about_company_picture',),
            )
        }),
        ('О производстве', {
            'fields': (
                ('about_factory_title',),
                ('about_factory',),
                ('about_factory_picture',),
            )
        }),
        ('Производственные мощности', {
            'fields': (
                ('capacity_title',),
                ('capacity_sub_title',),
                ('capacity_body',),
            )
        }),
    )

    def has_add_permission(self, request, obj=None):
        if About.objects.all().count() >= 1:
            return False
        else:
            return True
