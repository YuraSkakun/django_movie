from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from movie.models import Movie


class MovieListView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movie_list'
    login_url = reverse_lazy('login')
    paginate_by = 4

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.order_by('release_date')

        if request.GET.get('title'):
            qs = qs.filter(title=request.GET.get('title'))

        if request.GET.get('genre'):
            qs = qs.filter(genre=request.GET.get('genre'))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Movie list'
        return context


class MovieDetailsView(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = 'movie_details.html'
    context_object_name = 'movie'
