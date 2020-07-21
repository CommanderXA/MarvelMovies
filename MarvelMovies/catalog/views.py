from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Movie, Director, MovieInstance, Genre, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_movies': num_movies,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_directors': num_directors,
        'genres': genres,
        'action_movies': action_movies,
        'num_visits': num_visits,
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


class LoanedMoviesByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = MovieInstance
    template_name = 'catalog/movieinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return MovieInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedMoviesAllUsersListView(PermissionRequiredMixin, generic.ListView):
    model = MovieInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/movieinstance_list_all_borrowed.html'
    paginate_by = 10

    def get_queryset(self):
        return MovieInstance.objects.filter(status__exact='o').order_by('due_back')
