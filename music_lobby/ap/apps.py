from django.apps import AppConfig
from django.db.models.signals import post_migrate

def load_initial_data(sender, **kwargs):
    from .models import Album
    if not Album.objects.exists():
        albums = [
            {"title": "The Eminem Show", "artist": "Eminem", "release_year": 2001, "cover_image": "media/TES.jpg"},
            {"title": "The Dark Side of the Moon", "artist": "Pink Floyd", "release_year": 1973, "cover_image": "https://upload.wikimedia.org/wikipedia/en/3/3b/Dark_Side_of_the_Moon.png"},
            {"title": "Thriller", "artist": "Michael Jackson", "release_year": 1982, "cover_image": "https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png"},
        ]
        for album in albums:
            Album.objects.create(**album)

class ApConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ap'

    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(load_initial_data, sender=self)