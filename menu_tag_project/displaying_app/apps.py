"""Модуль класса приложения."""
from django.apps import AppConfig


class DisplayingAppConfig(AppConfig):
    """Класс приложения."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'displaying_app'
