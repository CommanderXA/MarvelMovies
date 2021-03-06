from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

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
    language = models.ManyToManyField(Language)

    class Meta:
        get_latest_by = 'date'

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def display_language(self):
        return ', '.join(language.movie_language for language in self.language.all())

    display_language.short_description = 'Language'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this movie."""
        return reverse('movie_detail', args=[str(self.id)])


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

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.movie.title})'

    class Meta:
        permissions = (("can_mark_returned", "Set book as returned"),)


class Director(models.Model):
    """ Model representing a director """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['first_name']

    def get_absolute_url(self):
        return reverse('director_detail', args=[str(self.id)])

    def __str__(self):
        return f' {self.first_name} {self.last_name}'
