"""Модуль класса приложения."""
from django.apps import AppConfig


class TagsMenuConfig(AppConfig):
    """Класс приложения."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tags_menu'

    verbose_name = 'Меню тегов'
