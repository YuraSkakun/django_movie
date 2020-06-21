from datetime import date

from django.db import models

# Create your models here.


class Movie(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1024, null=True, blank=True)
    poster = models.ImageField(default='default_movie.jpg', upload_to='covers')
    genre = models.CharField(max_length=64, null=True, blank=True)
    producer = models.CharField(max_length=64, null=True, blank=True)
    release_date = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text="in dollars")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('release_date',)
