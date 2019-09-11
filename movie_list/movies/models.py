from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=500)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MovieList(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name


class StarRanking(models.Model):
    ranking = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # there should be a unique constraint on (user_id, movie_id)

    def __str__(self):
        return "{movie_name}: {ranking} Star".format(movie_name=self.movie.name, ranking=self.ranking)
