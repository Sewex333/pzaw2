from django.contrib import admin
from .models import Album, Track, Rating, Comment

admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Rating)
admin.site.register(Comment)