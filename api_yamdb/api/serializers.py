from rest_framework import serializers

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
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = models.Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'category',
                  'genre')

    def get_rating(self, obj):
        return 0  # TODO implement

    def create(self, validated_data):
        category = validated_data.pop('category')
        genre = validated_data.pop('genre')

        # creating title
        title = models.Title.objects.create(**validated_data)

        # creating category
        category_obj, created = models.Category.objects.get_or_create(
            name=category['name'], slug=category['slug'])
        title.category.add(category_obj)

        # creating genre
        for g in genre:
            genre_obj, created = models.Genre.objects.get_or_create(
                name=g['name'], slug=g['slug'])
            title.genre.add(genre_obj)

        return title
