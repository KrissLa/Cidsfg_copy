from django.contrib import admin

from .models import CounterForSite, SearchSystem


@admin.register(SearchSystem)
class ConnectSSModelAdmin(admin.ModelAdmin):
    """Поисковые системы"""
    list_display = ("name", 'active')
    list_editable = ('active',)


@admin.register(CounterForSite)
class CounterForSiteAdmin(admin.ModelAdmin):
    """Счечики и аналитика для сайта"""
    list_display = ("name", "active")
    list_editable = ('active',)