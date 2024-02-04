from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.menu, name='home'),  # http://127.0.0.1:8000/home
    path('news/', views.news, name='news'),
    path('account/', views.account, name='account'),

    path('friends/', views.show_friends, name='friends'),
    path('friends/<int:friend_id>/', views.show_friend, name='friend'),

    path('friends/added-friends/', views.show_added_friends, name='added_friends'),
    path('friends/subscribers/', views.show_subscribers, name='subscribers'),

]
