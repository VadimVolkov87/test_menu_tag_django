"""Модуль представлений приложения."""
from django.shortcuts import render


def index(request):
    """Функция представления главной страницы."""
    return render(request, 'tags_menu/index.html')


def cartoons(request):
    """Функция представления страницы мультфильмов."""
    return render(request, 'tags_menu/cartoons.html')


def movies(request):
    """Функция представления страницы кинофильмов."""
    return render(request, 'tags_menu/movie.html')


def comedy(request):
    """Функция представления страницы триллеров."""
    return render(request, 'tags_menu/comedy.html')


def drama(request):
    """Функция представления страницы драм."""
    return render(request, 'tags_menu/drama.html')


def detective(request):
    """Функция представления страницы детективов."""
    return render(request, 'tags_menu/detective.html')


def composer(request):
    """Функция представления страницы композитора."""
    return render(request, 'tags_menu/composer.html')


def director(request):
    """Функция представления страницы режиссера."""
    return render(request, 'tags_menu/director.html')


def production_designer(request):
    """Функция представления страницы художника-постановщика."""
    return render(request, 'tags_menu/production_designer.html')


def series(request):
    """Функция представления страницы сериалов."""
    return render(request, 'tags_menu/series.html')


def shows(request):
    """Функция представления страницы шоу."""
    return render(request, 'tags_menu/shows.html')


def questions_contacts(request):
    """Функция представления страницы вопросов/контактов."""
    return render(request, 'tags_menu/questions_contacts.html')
