from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def menu(request):
    return HttpResponse('Основная страница представления')


def main(request):
    return HttpResponse('Ты нажал на кнопку "Главная"')


def articles(request, art_id):
    if art_id > 15:
        raise Http404()
    return HttpResponse(f'<h1>Ты нажал на кнопку "Статьи"</h1> <p>id: {art_id}</p>')
