from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

bar = [
    {'title': 'News', 'url_name': 'news'},
    {'title': 'Friends', 'url_name': 'friends'},
    {'title': 'Account', 'url_name': 'account'},

]

data_db = [
    {'id': 1, 'name': 'Василий Пупкинов', 'content': 'Страница Василия Пупкина', 'is_friend': True},
    {'id': 2, 'name': 'Стасян Голубок', 'content': 'Страница Стасяна Голубок', 'is_friend': False},
    {'id': 3, 'name': 'Дымок Чёкавоизачем', 'content': 'Страница Дымок Чёкавоизачем', 'is_friend': True},
]

friends_category = [
    {'id': 1, 'name': 'Добавленные друзья', 'url_name': 'added_friends'},
    {'id': 2, 'name': 'Подписчики', 'url_name': 'subscribers'},
]


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def menu(request):
    data = {
        'title': 'Основная страница представления',
        'bar': bar,
    }
    return render(request,
                  'menu/home.html',
                  data)


def show_friend(request, friend_id):
    return HttpResponse(f'Отображение друга с id = {friend_id}')


def show_added_friends(request):
    data = {
        'title': 'Добавленные друзья',
        'bar': bar,
        'friends': data_db,
    }
    return render(request,
                  'menu/added_friends.html',
                  data)


def show_subscribers(request):
    data = {
        'title': 'Подписчики',
        'bar': bar,
        'friends': data_db,
    }
    return render(request,
                  'menu/subscribers.html',
                  data)


def show_friends(request):
    data = {
        'title': 'Друзья и подписчики',
        'bar': bar,
        'friends': data_db,
    }
    return render(request,
                  'menu/friends.html',
                  data)


def news(request):
    data = {
        'title': 'Страница с новостями',
        'bar': bar,
    }
    return render(request,
                  'menu/news.html',
                  data)


def account(request):
    data = {
        'title': 'Аккаунт',
        'bar': bar,
    }
    return render(request,
                  'menu/account.html',
                  data)
