from django.contrib import admin

# Register your models here.
from movie.models import Movie


class MovieAdminModel(admin.ModelAdmin):
    # fields =('title', 'description', 'poster', 'genre', 'release_date')
    list_display = ('title', 'genre', 'poster', 'release_date')


admin.site.register(Movie, MovieAdminModel)
