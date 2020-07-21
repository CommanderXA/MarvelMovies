from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('directors/', views.DirectorsListView.as_view(), name='directors'),
    path('director/<int:pk>', views.DirectorDetailView.as_view(), name='director_detail'),
]

urlpatterns += [
    path('mymovies/', views.LoanedMoviesByUserListView.as_view(), name='my-borrowed'),
    path('allmovies_borrowed/', views.LoanedMoviesAllUsersListView.as_view(), name='all-borrowed')
]
