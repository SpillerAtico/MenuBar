from django.contrib import admin

from menu_generator.models import Menu


@admin.register(Menu)
class MenuSettings(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'slug')

    prepopulated_fields = {
        'slug': ('name', ),
    }