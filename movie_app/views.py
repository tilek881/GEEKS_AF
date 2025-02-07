from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer


@api_view(['GET'])
def director_list_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(instance=directors, many=True).data
    return Response(data=data)


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
def review_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request, id):
    review = get_object_or_404(Review, id=id)
    data = ReviewSerializer(review).data
    return Response(data=data)
