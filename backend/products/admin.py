from django.contrib import admin
from .models import House, Category, Series


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Series)
class HouseAdmin(admin.ModelAdmin):
    """ Домами из панели администратора """
    prepopulated_fields = {"slug": ("name",)}
