from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Track, Comment
from .forms import CommentForm

def logout_view(request):
    logout(request)
    return redirect("home") 

def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    tracks = album.track_set.all()
    return render(request, 'album.html', {'album': album, 'tracks': tracks})

def track_detail(request, track_id):
    track = get_object_or_404(Track, id=track_id)
    comments = track.comment_set.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.track = track
            comment.user = request.user
            comment.save()
            return redirect('track_detail', track_id=track.id)
    else:
        form = CommentForm()

    return render(request, 'track.html', {'track': track, 'comments': comments, 'form': form})
@login_required
def protected_view(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


