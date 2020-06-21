from django.urls import path

from movie.views import MovieListView, MovieDetailsView

app_name = 'movie'

urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie_list'),
    path('details/<int:pk>', MovieDetailsView.as_view(), name='movie_details'),
]
