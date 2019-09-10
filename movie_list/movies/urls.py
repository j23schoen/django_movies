from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'movie_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie_list/<int:movie_list_id>/', views.view, name='view'),
    path('movie_list/new', views.new_movie_list, name='new'),
    path('movie_list/create', views.create, name='create'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('sign_up/', views.sign_up, name='sign_up')
]
