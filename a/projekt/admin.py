from django.contrib import admin
from .models import Album, Track, Comment

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'album')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('track', 'user', 'content', 'created_at')