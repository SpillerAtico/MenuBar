from django import template

register = template.Library()


@register.inclusion_tag('menu_generator/create_menu.html')
def draw_menu(menu_name):
    data_menu = [{'id': 1, 'name': menu_name},  # имя и айдишник вероятно будут уникальными
                 {'id': 2, 'name': 'google'}]

    data_menu_category = [
        {'id': 1, 'menu_id': 1, 'category_name': 'Главная', 'slug': 'glavnaya'},
        {'id': 2, 'menu_id': 1, 'category_name': 'О сайте', 'slug': 'osayte'},
        {'id': 3, 'menu_id': 2, 'category_name': 'Ближайшие города', 'slug': 'blijaishie'},
        {'id': 4, 'menu_id': 2, 'category_name': 'Поиск', 'slug': 'poisk'},
    ]

    return {
        'data_menu_category': data_menu_category,
        'data_menu': data_menu
    }
