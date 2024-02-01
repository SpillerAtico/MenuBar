from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu),  # http://127.0.0.1:8000/menu
    path('main/', views.main),
    path('articles/<int:art_id>', views.articles),
]


