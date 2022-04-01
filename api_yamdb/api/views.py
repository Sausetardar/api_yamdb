from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers, filters
from reviews import models


class CreateListDestroy(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class GenreViewSet(CreateListDestroy):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    # permission_classes = [permissions.IsAdminOrReadOnly]

    lookup_field = 'slug'
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class CategoryViewSet(CreateListDestroy):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # permission_classes = [permissions.IsAdminOrReadOnly]

    lookup_field = 'slug'
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = models.Title.objects.all()
    # permission_classes = [permissions.IsAdminOrReadOnly]

    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.TitleFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.TitleDisplaySerializer
        return serializers.TitleCreateUpdateSerializer
