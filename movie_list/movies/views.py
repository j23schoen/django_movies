from django.shortcuts import render
from .models import MovieList
from .dao.movie_list import get_movie_lists, get_movie_list


def index(request):
    return render(request, 'movie_list/index.html', {'movie_lists': get_movie_lists()})


def view(request, movie_list_id):
    return render(request, 'movie_list/view.html', {'movie_list': get_movie_list(movie_list_id)})


def new_movie_list(request):
    return render(request, 'movie_list/new_movie_list.html', {})


def create(request):
    movie_list = MovieList(name=request.POST['name'])
    movie_list.save()
    return view(request, movie_list.id)
