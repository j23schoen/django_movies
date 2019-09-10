from ..models import MovieList


def get_movie_lists():
    movie_lists = MovieList.objects.all()
    aggregate_list = []
    for movie_list in movie_lists:
        aggregate_list.append({
            'list': movie_list,
            'number_of_movies': movie_list.movies.count()
        })
    return aggregate_list


def get_movie_list(movie_list_id):
    movie_list = MovieList.objects.get(id=movie_list_id)
    movies = []
    for movie in movie_list.movies.all():
        rankings = movie.starranking_set.all()
        rating = 'This film has not yet been rated'
        if rankings:
            rating = sum([ranking.ranking for ranking in rankings]) / len(rankings)

        movies.append({
            'title': movie.name,
            'release_year': movie.release_year,
            'genre': movie.genre,
            'rating': rating
        })

    return {'list': movie_list, 'movies': movies}
