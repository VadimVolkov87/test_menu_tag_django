"""Класс моделей приложения."""
from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """Класс модели Menu."""
    name = models.CharField(max_length=255, unique=True, verbose_name='Имя')

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Класс модели MenuItem."""
    menu = models.ForeignKey(
        Menu, related_name='items', on_delete=models.CASCADE, verbose_name='Меню'
    )
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children',
                               on_delete=models.CASCADE, verbose_name='Родитель')
    title = models.CharField('Название', max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True,
                           help_text='Формат ввода "/example"')
    named_url = models.CharField('Именованный URL', max_length=255, blank=True,
                                 null=True, help_text='Формат ввода "example"')

    def get_url(self):
        """Возвращает URL для пункта. Использует named_url, если задан."""
        if self.named_url:
            return reverse(self.named_url)
        return self.url or '#'

    class Meta:
        verbose_name = 'тег меню'
        verbose_name_plural = 'Теги меню'

    def __str__(self):
        return self.title
