from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', default=1)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'Review for {self.movie.title}'
