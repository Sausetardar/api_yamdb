from django.contrib import admin

from .models import Genre, Title, Category

admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Category)
