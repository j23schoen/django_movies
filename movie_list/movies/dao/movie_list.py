from ..models import MovieList, Movie


def get_movie_lists(user_id):
    movie_lists = MovieList.objects.filter(user_id=user_id)
    aggregate_list = []
    for movie_list in movie_lists:
        aggregate_list.append({
            'list': movie_list,
            'number_of_movies': movie_list.movies.count()
        })
    return aggregate_list


def get_movie_list(movie_list_id, user_id):
    movie_list = MovieList.objects.get(id=movie_list_id)
    movies = []
    for movie in movie_list.movies.all():
        rankings = movie.starranking_set.all()
        my_rating = 'I have not rated this movie yet.'
        my_rating_record = movie.starranking_set.filter(user_id=user_id).first()
        if my_rating_record:
            my_rating = my_rating_record.ranking

        rating = 'This film has not yet been rated'
        if rankings:
            rating = sum([ranking.ranking for ranking in rankings]) / len(rankings)

        movies.append({
            'title': movie.name,
            'release_year': movie.release_year,
            'genre': movie.genre,
            'average_rating': rating,
            'my_rating': my_rating
        })

    return {'list': movie_list, 'movies': movies}


def add_movie_to_movie_list(movie_id, movie_list_id):
    movie_list = MovieList.objects.get(pk=movie_list_id)
    movie_list.movies.add(Movie.objects.get(pk=movie_id))
    movie_list.save()
    return movie_list
