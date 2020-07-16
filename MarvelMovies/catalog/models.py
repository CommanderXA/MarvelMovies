from django.db import models
import uuid

# Create your models here.
from django.urls import reverse


class Genre(models.Model):
    #  fields
    name = models.CharField(max_length=200, help_text='Enter a movie genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the movie's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the movie')
    imdb = models.FloatField('IMDB', help_text='IMDB rating')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this movie')
    date = models.DateField(null=True, blank=True)  # it's not used in tutorial

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this movie."""
        return reverse('movie-detail', args=[str(self.id)])


class MovieInstance(models.Model):
    """Model representing a specific copy of a movie (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular movie across whole library')
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Movie availability',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.movie.title})'


class Director(models.Model):
    """ Model representing a director """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
