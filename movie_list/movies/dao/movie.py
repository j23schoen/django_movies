from ..models import StarRanking, MovieList, Movie


def rate_movie(user_id, movie_id, rating):
    star_ranking, created = StarRanking.objects.get_or_create(
        user_id=user_id, movie_id=movie_id, defaults={'ranking': rating})
    if not created:
        star_ranking.ranking = rating
        star_ranking.save()
    return star_ranking


def get_movies_not_in_movie_list(movie_list_id):
    movie_ids = [movie.id for movie in MovieList.objects.get(pk=movie_list_id).movies.all()]
    return Movie.objects.exclude(pk__in=movie_ids)
