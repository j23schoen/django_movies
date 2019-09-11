from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'movie_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie_list/<int:movie_list_id>/', views.view, name='view'),
    path('movie_list/new', views.new_movie_list, name='new'),
    path('movie_list/create', views.create_movie_list, name='create'),
    path('movie/new', views.new_movie_form, name='new_movie'),
    path('movie/create', views.create_movie, name='create_movie'),
    path('movie/add_to_list', views.add_movie_to_list, name='add_movie_to_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_out', views.log_user_out, name='log_out')
]
