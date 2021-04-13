from django.contrib import admin

from .models import HomeDecorationCategory, HomeDecorationSubCategory, HomeDecorationType, HomeDecoration


@admin.register(HomeDecorationCategory)
class HomeDecorationCategoryAdmin(admin.ModelAdmin):
    """ Управление отделкой и коммуникациями из панели администратора """
    prepopulated_fields = {"hd_slug": ("hd_name",)}


@admin.register(HomeDecorationSubCategory)
class HomeDecorationSubCategoryAdmin(admin.ModelAdmin):
    """ Управление отделкой и коммуникациями из панели администратора """
    prepopulated_fields = {"slug": ("name",)}


@admin.register(HomeDecorationType)
class HomeDecorationAdmin(admin.ModelAdmin):
    """ Управление отделкой и коммуникациями из панели администратора """
    prepopulated_fields = {"slug": ("name",)}

@admin.register(HomeDecoration)
class HomeDecorationAdmin(admin.ModelAdmin):
    """ Управление отделкой и коммуникациями из панели администратора """
    prepopulated_fields = {"slug": ("name",)}