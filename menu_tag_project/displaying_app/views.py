"""Модуль представлений приложения."""
from django.shortcuts import render


templates = {
    '/cartoons/': 'tags_menu/cartoons.html',
    '/movies/': 'tags_menu/movie.html',
    '/plasticine/': 'tags_menu/cartoons.html',
    '/grey_wolf/': 'tags_menu/cartoons.html',
    '/plasticine_crow/': 'tags_menu/cartoons.html',
    '/tatarski/': 'tags_menu/director.html',
    '/bardin/': 'tags_menu/director.html',
    '/drawn/': 'tags_menu/cartoons.html',
    '/melik_sarkisian/': 'tags_menu/production_designer.html',
    '/puppet/': 'tags_menu/cartoons.html',
    '/kovalev/': 'tags_menu/production_designer.html',
    '/gladkov/': 'tags_menu/composer.html',
    '/drama/': 'tags_menu/drama.html',
    '/comedy/': 'tags_menu/comedy.html',
    '/detective/': 'tags_menu/detective.html',
    '/series/': 'tags_menu/series.html',
    '/shows/': 'tags_menu/shows.html',
    '/questions/': 'tags_menu/questions_contacts.html',
    '/contacts/': 'tags_menu/questions_contacts.html',
    }


def index(request):
    """Функция представления главной страницы."""
    return render(request, 'tags_menu/index.html')


def point(request, url):
    """Функция представления страницы пункта меню."""
    return render(request, template_name=templates[request.path])


def cartoons(request):
    """Функция представления страницы мультфильмов."""
    return render(request, 'tags_menu/cartoons.html')
