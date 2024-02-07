from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def base(request):
    data = {
        'title': 'Основная страница представления',
    }
    return render(request,
                  'menu_generator/base.html',
                  data)


def show_category(request, category_slug):
    data = {
        'title': 'Тест',
        'category_slug': category_slug,
    }

    return render(request,
                  'menu_generator/base.html',
                  data)
