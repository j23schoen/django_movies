from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=500)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MovieList(models.Model):
    name = models.CharField(max_length=200, unique=True)

    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name


class StarRanking(models.Model):
    ranking = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return "{ranking} Star".format(ranking=self.ranking)
