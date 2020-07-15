from django.contrib import admin
from .models import Genre, Director, Movie, MovieInstance, Language

# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)


class MoviesInline(admin.TabularInline):
    model = Movie
    extra = 0


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    inlines = [MoviesInline]


class MoviesInstanceInline(admin.TabularInline):
    model = MovieInstance
    extra = 0


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genre')
    inlines = [MoviesInstanceInline]


admin.site.register(Movie, MovieAdmin)


@admin.register(MovieInstance)
class MovieInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('movie', 'status', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('movie', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
