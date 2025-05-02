"""Модуль маршрутизаторов приложения."""
from django.urls import path
from . import views

app_name = 'displaying_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('cartoons/', views.cartoons, name='cartoons'),
    path('<slug:url>/', views.point, name='point'),
]
