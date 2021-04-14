from django.contrib import admin
from .models import House, Category, Series


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"house_slug": ("house_name",)}


@admin.register(Category)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"category_slug": ("category_name",)}


@admin.register(Series)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"series_slug": ("series_name",)}
