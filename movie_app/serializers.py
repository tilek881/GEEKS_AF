from rest_framework import serializers
from .models import Movie, Director, Review

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
