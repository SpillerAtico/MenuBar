from django import template
from django.utils.safestring import mark_safe
from menu_generator.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu_simple(context, menu_name):
    menu = Menu.objects.filter(name=menu_name).select_related('parent')
    path = context.request.get_full_path()

    return mark_safe(create_menu(menu, path))


@register.inclusion_tag('menu_generator/create_menu.html', takes_context=True)
def draw_menu_inclusion(context, menu_name):
    menu_items = Menu.objects.filter(name=menu_name).select_related('parent')
    path = context.request.get_full_path()

    return {'menu_items': menu_items,
            'path': path}


def create_menu(menu, path):
    menu_html = '<ul>'
    for item in menu:
        menu_html += '<li>'
        if item.slug in path:
            menu_html += f'<a class="selected" href="{item.get_absolute_url()}">{item.name}</a>'
        else:
            menu_html += f'<a href="{item.get_absolute_url()}">{item.name}</a>'
        if item.children.exists():
            menu_html += create_menu(item.children.all(), path)
        menu_html += '</li>'
    menu_html += '</ul>'

    return menu_html
