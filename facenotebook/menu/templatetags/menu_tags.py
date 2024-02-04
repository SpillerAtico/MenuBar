from django import template
import menu.views as views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.friends_category
