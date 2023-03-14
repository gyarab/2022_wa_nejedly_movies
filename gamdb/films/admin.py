from django.contrib import admin

from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year']
    list_display_links = ['name']

admin.site.register(Movie, MovieAdmin)