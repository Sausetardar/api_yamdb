from rest_framework import serializers
from reviews import models
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('name', 'slug')


class TitleDisplaySerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    category = CategorySerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = models.Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'category',
                  'genre')
        required_fields = ('name', 'year', 'category', 'genre')

    def get_rating(self, obj):
        return 0  # TODO implement


class TitleCreateUpdateSerializer(serializers.ModelSerializer):
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
        return 0  # always 0 for new titles

    def create(self, validated_data):
        genres = validated_data.pop('genre')

        # create title
        title = models.Title.objects.create(**validated_data)

        # add genres
        for genre in genres:
            title.genre.add(genre)

        return title

    def update(self, instance, validated_data):
        genres = validated_data.pop('genre')

        instance.genre.clear()

        for genre in genres:
            instance.genre.add(genre)

        return instance


class GetTokenSerializer(serializers.Serializer):

    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.CharField()

    class Meta:
        model = models.User
        fields = ('email',)


class UserInfoSerializer(serializers.ModelSerializer):
    bio = serializers.CharField()

    class Meta:
        model = models.User
        fields = (
            'bio', 'first_name', 'last_name',
            'username', 'email', 'role'
        )
        read_only_fields = ('role',)


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=models.User.objects.all())]
    )

    class Meta:
        model = models.User
        fields = (
            'first_name', 'last_name',
            'username', 'bio', 'email', 'role'
        )


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Нельзя создать пользователя с username = "me"')
        return value
