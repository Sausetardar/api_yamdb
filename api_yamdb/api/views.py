from rest_framework import viewsets, mixins


from . import serializers, permissions
from reviews import models


class CreateListDestroy(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class GenreViewSet(CreateListDestroy):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    # permission_classes = [permissions.IsAdminOrReadOnly]


class CategoryViewSet(CreateListDestroy):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # permission_classes = [permissions.IsAdminOrReadOnly]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = models.Title.objects.all()
    serializer_class = serializers.TitleSerializer
    # permission_classes = [permissions.IsAdminOrReadOnly]
