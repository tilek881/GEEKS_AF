from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer

@api_view(['GET'])
def director_list_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data)


@api_view(['GET'])
def director_detail_view(request, id):
    director = get_object_or_404(Director, id=id)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def movie_reviews_list_view(request):
    movies = Movie.objects.prefetch_related('reviews').all()
    movies_data = []

    for movie in movies:
        reviews = movie.reviews.all()
        reviews_data = ReviewSerializer(reviews, many=True).data
        avg_rating = movie.average_rating or "Нет комментариев"

        movies_data.append({
            "id": movie.id,
            "title": movie.title,
            "reviews": reviews_data,
            "average_rating": avg_rating
        })

    return Response(movies_data)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request, id):
    review = get_object_or_404(Review, id=id)
    data = ReviewSerializer(review).data
    return Response(data=data)

@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.select_related('director').prefetch_related('reviews').all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data={'list': data})
