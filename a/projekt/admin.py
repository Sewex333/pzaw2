from django.contrib import admin
from .models import Club, Player, Comment

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'trophies')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'position', 'club')  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('player', 'user', 'content')
