from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Movie, Director, MovieInstance, Genre, Language
from django.views import generic

# Create your views here.


def index(request):
    """ Views function for Home page """
    num_movies = Movie.objects.all().count()
    num_instances = MovieInstance.objects.all().count()

    # available movies (status='a')
    num_instances_available = MovieInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default
    num_directors = Director.objects.count()
    genres = Genre.objects.count()
    action_movies = Movie.objects.filter(genre__name='Action').count()

    context = {
        'num_movies': num_movies,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_directors': num_directors,
        'genres': genres,
        'action_movies': action_movies,
    }
    return render(request, 'index.html', context)


class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 10


class MovieDetailView(generic.DetailView):
    model = Movie


def movie_detail_view(request, primary_key):
    movie = get_object_or_404(Movie, pk=primary_key)
    return render(request, 'catalog/movie_detail.html', context={'movie': movie})


class DirectorsListView(generic.ListView):
    model = Director
    paginate_by = 10


class DirectorDetailView(generic.DetailView):
    model = Director


def director_detail_view(request, primary_key):
    director = get_object_or_404(Director, pk=primary_key)
    return render(request, 'catalog/director_detail.html', context={'director': director})
