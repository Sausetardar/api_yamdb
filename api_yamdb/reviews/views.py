from rest_framework import viewsets, mixins, permissions


from . import serializers, models, permissions as review_permissions


class CreateListDestroy(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class GenreViewSet(CreateListDestroy):

    class Meta:
        model = models.Genre
        serializer_class = serializers.GenreSerializer
        permission_classes = [review_permissions.IsAdminOrReadOnly]


class CategoryViewSet(CreateListDestroy):

    class Meta:
        model = models.Category
        serializer_class = serializers.CategorySerializer
        permission_classes = [review_permissions.IsAdminOrReadOnly]


class TitleViewSet(viewsets.ModelViewSet):

    class Meta:
        model = models.Title
        serializer_class = serializers.TitleSerializer
        permission_classes = [review_permissions.IsAdminOrReadOnly]
