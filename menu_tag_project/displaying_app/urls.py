"""Модуль маршрутизаторов приложения."""
from django.urls import path
from . import views

app_name = 'displaying_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('cartoons/', views.cartoons, name='cartoons'),
    path('movies/', views.movies, name='movies'),
    path('plasticine/', views.cartoons, name='plasticine'),
    path('grey_wolf/', views.cartoons, name='grey_wolf'),
    path('plasticine_crow/', views.cartoons, name='plasticine_crow'),
    path('tatarski/', views.director, name='tatarski'),
    path('bardin/', views.director, name='bardin'),
    path('drawn/', views.cartoons, name='drawn'),
    path('melik_sarkisian/', views.production_designer, name='melik_sarkisian'),
    path('puppet/', views.cartoons, name='puppet'),
    path('kovalev/', views.production_designer, name='kovalev'),
    path('gladkov/', views.composer, name='gladkov'),
    path('drama/', views.drama, name='drama'),
    path('comedy/', views.comedy, name='comedy'),
    path('detective/', views.detective, name='detective'),
    path('series/', views.series, name='series'),
    path('shows/', views.shows, name='shows'),
    path('questions/', views.questions_contacts, name='questions'),
    path('contacts/', views.questions_contacts, name='contacts'),
]
