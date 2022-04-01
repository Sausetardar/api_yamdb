from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

<<<<<<< HEAD
=======
router.register('genres', views.GenreViewSet)
router.register('categories', views.CategoryViewSet)
router.register('titles', views.TitleViewSet)

>>>>>>> 2ada3273cccb7227b9c8d6d87743abdddb22aad4

urlpatterns = [
    path('v1/', include(router.urls)),
]
