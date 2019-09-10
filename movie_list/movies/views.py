from django.contrib.auth import authenticate, login as log_user_in
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            log_user_in(request, user)
            return redirect('/')

    form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})
