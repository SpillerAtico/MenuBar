from django.contrib import admin
from django.urls import path, include
from menu_generator.views import page_not_found

handler404 = page_not_found  # error post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu_generator.urls')),  # http://127.0.0.1:8000/menu
]
