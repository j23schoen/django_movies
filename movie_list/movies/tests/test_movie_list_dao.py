from django.test import TestCase
from django.contrib.auth.models import User
from ..models import StarRanking, Movie, MovieList
from ..dao.movie_list import get_movie_list, add_movie_to_movie_list


class MovieListTest(TestCase):

    def test_get_average_movie_rating(self):
        user = User()
        user.save()
        movie_list = MovieList(name='Adam Sandler', user=user)
        movie_list.save()

        movie = Movie(name='billy madison', release_year=1999, genre='Comedy')
        movie.save()
        movie_list.movies.add(movie)

        my_rating = StarRanking(ranking=5, movie=movie, user=user)
        my_rating.save()

        ratings = self.create_movie_ratings(movie)
        ratings.append(my_rating.ranking)
        expected_average = sum(ratings) / len(ratings)
        movies = get_movie_list(movie_list.id, user.id)['movies']

        for item in movies:
            self.assertEqual(expected_average, item['average_rating'])
            self.assertEqual(my_rating.ranking, item['my_rating'])

        self.assertIsNotNone(movies)

    def test_add_movie_to_movie_list(self):
        user = User()
        user.save()
        movie_list = MovieList(name='Action Movies', user=user)
        movie_list.save()

        movie = Movie(name='Fast and Furious', release_year=2001, genre='action')
        movie.save()
        updated_movie_list = add_movie_to_movie_list(movie.id, movie_list.id)
        movie_list_movie_ids = [mv.id for mv in updated_movie_list.movies.all()]
        self.assertIn(movie.id, movie_list_movie_ids)

    def create_movie_ratings(self, movie):
        ratings = [1, 2, 3, 4, 5]
        for rating in ratings:
            user = User(username="{rating}{movie}".format(rating=rating, movie=movie))
            user.save()
            StarRanking(ranking=rating, movie=movie, user=user).save()

        return ratings
