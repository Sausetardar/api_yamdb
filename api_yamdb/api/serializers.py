from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from reviews import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=models.Category.objects.all())
    genre = serializers.SlugRelatedField(
        slug_field='slug', queryset=models.Genre.objects.all(), many=True)

    class Meta:
        model = models.Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'category',
                  'genre')
        required_fields = ('name', 'year', 'category', 'genre')

    def get_rating(self, obj):
        return 0  # TODO implement

    def create(self, validated_data):
        category = validated_data.pop('category')
        genres = validated_data.pop('genre')

        # create title
        title = models.Title.objects.create(**validated_data)

        # set category
        title.category = category

        # add genres
        for genre in genres:
            title.genre.add(genre)

        return title
