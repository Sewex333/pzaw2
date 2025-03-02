from django.db import models
from django.contrib.auth.models import User
  

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_year = models.IntegerField()
    cover_image = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def average_rating(self):
        ratings = self.rating_set.all()
        if ratings:
            return sum(r.rating for r in ratings) / len(ratings)
        return None

    def total_ratings(self):
        return self.rating_set.count()

    def total_comments(self):
        return self.comment_set.count()
    

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=10) 

    def __str__(self):
        return f"{self.title} ({self.duration})"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    rating = models.IntegerField() 

    def __str__(self):
        return f"{self.user.username} ocenił {self.album.title} na {self.rating}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} skomentował {self.album.title}"
    

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.album.title}"