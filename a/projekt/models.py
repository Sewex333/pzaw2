from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trophies = models.TextField()
    logo = models.ImageField(upload_to='club_logos/', null=True, blank=True)  

    def __str__(self):
        return self.name

class Player(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()  
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.number})"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.player.name}"