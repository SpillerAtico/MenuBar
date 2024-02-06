from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),  # http://127.0.0.1:8000/base
    path('category/<slug:category_slug>/', views.show_category, name='show_category'),
]
