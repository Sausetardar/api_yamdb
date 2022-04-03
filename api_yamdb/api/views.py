from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Avg

from . import serializers, filters, permissions
from reviews import models


class CreateListDestroy(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class GenreViewSet(CreateListDestroy):
    queryset = models.Genre.objects.all().order_by('-id')
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

    lookup_field = 'slug'
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class CategoryViewSet(CreateListDestroy):
    queryset = models.Category.objects.all().order_by('-id')
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

    lookup_field = 'slug'
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = models.Title.objects.all().order_by('-id').annotate(
        mean_score=Avg('reviews__score')
    )
    permission_classes = [permissions.IsAdminOrReadOnly]

    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.TitleFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.TitleDisplaySerializer
        return serializers.TitleCreateUpdateSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.ReviewCommentPermission]

    def get_queryset(self):
        title = get_object_or_404(models.Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(models.Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.ReviewCommentPermission]

    def get_queryset(self):
        review = get_object_or_404(
            models.Review,
            pk=self.kwargs.get('review_id')
        )
        # Проверяем, соответствует ли отзыв произведению.
        if review.title.id != int(self.kwargs.get('title_id')):
            raise Http404('Отзыв относится к другому произведению.')
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            models.Review,
            pk=self.kwargs.get('review_id')
        )
        # Проверяем, соответствует ли отзыв произведению.
        if review.title.id != int(self.kwargs.get('title_id')):
            raise Http404('Отзыв относится к другому произведению.')
        serializer.save(author=self.request.user, review=review)
