from rest_framework import serializers
from .models import Movie, Director, Review
from .models import CustomUser
from django.contrib.auth import authenticate


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ["id", "name", "movies_count"]

    def get_movies_count(self, obj):
        return obj.movies.count()

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "director", "average_rating"]

    def get_average_rating(self, obj):
        return obj.average_rating

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive number.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = ["id", "text", "stars", "movie"]

    def validate_stars(self, value):
        if value not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError("Stars must be between 1 and 5.")
        return value



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.is_active = False
        user.save()
        return user

class ConfirmUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = CustomUser.objects.get(username=data["username"], confirmation_code=data["confirmation_code"])
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Неверный код подтверждения.")
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Неверное имя пользователя или пароль.")
        if not user.is_active:
            raise serializers.ValidationError("Аккаунт не подтвержден.")
        return {"user": user}