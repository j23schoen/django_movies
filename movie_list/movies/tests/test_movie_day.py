from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Movie, StarRanking, MovieList
from ..dao.movie import rate_movie, get_movies_not_in_movie_list


class MovieTest(TestCase):

    def test_save_movie_rating(self):
        user = User()
        user.save()
        movie = Movie(name='billy madison', release_year='1999', genre='comedy')
        movie.save()

        rating = 5

        star_ranking = rate_movie(user.id, movie.id, rating)
        self.assertEqual(star_ranking.ranking, rating)

    def test_update_movie_rating(self):
        user = User()
        user.save()
        movie = Movie(name='billy madison', release_year=1999, genre='comedy')
        movie.save()

        original_rating = 3
        movie_ranking = StarRanking(ranking=original_rating, movie=movie, user=user)
        movie_ranking.save()

        new_rating = original_rating + 2
        star_ranking = rate_movie(user.id, movie.id, new_rating)
        self.assertEqual(star_ranking.ranking, new_rating)

    def test_get_movie_not_in_movie_list(self):
        user = User()
        user.save()

        movie_list = MovieList(name='funny', user=user)
        movie_list.save()

        wedding_singer = Movie(name='wedding singer', release_year=1998, genre='romance')
        wedding_singer.save()
        movie_list.movies.add(wedding_singer)

        billy = Movie(name='billy madison', release_year=1995, genre='comedy')
        billy.save()
        bouche = Movie(name='water boy', release_year=1998, genre='comedy')
        bouche.save()
        hippo = Movie(name='big daddy', release_year=1999, genre='comedy')
        hippo.save()

        expected_movie_ids = [movie.id for movie in [billy, bouche, hippo]]

        actual_available_movies = get_movies_not_in_movie_list(movie_list.id)
        actual_movie_ids = [movie.id for movie in actual_available_movies]
        self.assertEqual(sorted(expected_movie_ids), sorted(actual_movie_ids))
