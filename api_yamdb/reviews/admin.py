from django.contrib import admin

<<<<<<< HEAD
from .models import User

admin.site.register(User)
=======
from .models import Genre, Title, Category

admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Category)
>>>>>>> 2ada3273cccb7227b9c8d6d87743abdddb22aad4
