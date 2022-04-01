from django.contrib import admin

from .models import User, Genre, Title, Category

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Category)
