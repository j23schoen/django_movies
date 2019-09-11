from django.contrib.auth import authenticate, logout, login as log_user_in
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import MovieList, Movie
from .dao.movie_list import get_movie_lists, get_movie_list, add_movie_to_movie_list
from .dao.movie import get_movies_not_in_movie_list


def index(request):
    if request.user.is_authenticated:
        return render(request, 'movie_list/index.html', {'movie_lists': get_movie_lists(request.user.id)})
    return render(request, 'movie_list/index.html')


def view(request, movie_list_id):
    available_movies = get_movies_not_in_movie_list(movie_list_id)
    return render(request, 'movie_list/view.html', {
        'movie_list': get_movie_list(movie_list_id, request.user.id),
        'available_movies': available_movies
    })


def new_movie_list(request):
    return render(request, 'movie_list/new_movie_list.html')


def new_movie_form(request):
    return render(request, 'movie/new_movie_form.html')


@login_required
def create_movie(request):
    movie = Movie(name=request.POST['name'], release_year=request.POST['release_year'], genre=request.POST['genre'])
    movie.save()
    return redirect('/movies')


@login_required
def create_movie_list(request):
    movie_list = MovieList(name=request.POST['name'], user=request.user)
    movie_list.save()
    return view(request, movie_list.id)


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            log_user_in(request, user)
            return redirect('/movies')

    form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def log_user_out(request):
    logout(request)
    return redirect('/movies')


@login_required()
def add_movie_to_list(request):
    print('HELLOOOO*****' + request.POST['movie_list_id'])
    add_movie_to_movie_list(request.POST['movie_id'], request.POST['movie_list_id'])
    return view(request, request.POST['movie_list_id'])


@login_required
def rate_movie(request, movie_id, rating):
    return
