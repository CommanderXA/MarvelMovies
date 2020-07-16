from django.shortcuts import render
from .models import Movie, Director, MovieInstance, Genre

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
