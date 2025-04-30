"""Модуль меню тэгов приложения."""
from collections import defaultdict

from django import template
from django.urls import reverse

from tags_menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('tags_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Рисует меню по имени (menu_name) на основе модели MenuItem.
    Контекст: текущий URL, url_name для определения активного пункта.
    """
    menu = MenuItem.objects.values('id', 'parent', 'title', 'url', 'named_url', 'menu__name'
                                   ).filter(menu__name=menu_name)
    menu_items = defaultdict(list)
    for entity in menu:
        if entity['url']:
            active = context['request'].path.startswith(entity['url'])
        else:
            active = context['request'].resolver_match.url_name.startswith(entity['named_url'])
        if entity['named_url']:
            item_named_url = reverse(f'displaying_app:{entity['named_url']}')
        else:
            item_named_url = None
        menu_item = {
                'item_id': entity['id'],
                'item': entity['title'],
                'item_url': entity['url'],
                'item_named_url': item_named_url,
                'active': active,
                'children': []
            }
        if entity['parent']:
            menu_items[entity['parent']].append(menu_item)
        else:
            menu_items[0].append(menu_item)
    for key in list(menu_items.keys())[::-1]:
        for key_2, value in list(menu_items.items())[::-1]:
            for index, entry in enumerate(value):
                if key == entry['item_id']:
                    for submenu in menu_items[key]:
                        if submenu['active']:
                            menu_items[key_2][index]['active'] = True
                    menu_items[key_2][index]['children'] = menu_items.pop(key)
    return {
        'menu': menu_name,
        'menu_items': menu_items[0],
    }
