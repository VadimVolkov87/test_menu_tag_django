"""Модуль панели админа приложения."""
from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    """Класс для добавления модели в страницу модели Menu."""
    model = MenuItem
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    """Класс админки модели Menu."""
    inlines = [MenuItemInline]
    list_display = ('name',)

admin.site.register(Menu, MenuAdmin)
