from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('genres', views.GenreViewSet)
router.register('categories', views.CategoryViewSet)
router.register('titles', views.TitleViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
]
