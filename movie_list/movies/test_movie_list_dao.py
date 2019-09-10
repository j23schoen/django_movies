from django.test import TestCase
from .models import StarRanking, Movie, MovieList
from .dao.movie_list import get_movie_list


class MovieListTest(TestCase):

    def testGetAverageMovieRating(self):
        movie_list = MovieList(name='Adam Sandler')
        movie_list.save()

        movie = Movie(name='billy madison', release_year=1999, genre='Comedy')
        movie.save()
        movie_list.movies.add(movie)

        ratings = [1, 2, 3, 4, 5]
        bulk_create_ratings = []
        for rating in ratings:
            bulk_create_ratings.append(StarRanking(ranking=rating, movie_id=movie.id))
        movie.starranking_set.bulk_create(bulk_create_ratings)

        expected_average = sum(ratings) / len(ratings)
        movies = get_movie_list(movie_list.id)['movies']

        for item in movies:
            self.assertEqual(expected_average, item['rating'])

        self.assertIsNotNone(movies)
