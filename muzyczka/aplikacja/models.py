from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=100)
    excluded = models.BooleanField(default=False)

User = get_user_model()

class Game(models.Model):
    players = models.ManyToManyField(User)  
    created_at = models.DateTimeField(auto_now_add=True)
    current_turn = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="current_turn")
    finished = models.BooleanField(default=False)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="winner")

    def __str__(self):
        return f"Gra #{self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    answer = models.TextField()
    points = models.IntegerField()
    used = models.BooleanField(default=False)


