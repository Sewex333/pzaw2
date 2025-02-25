from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Track, Comment
from django.contrib.auth.decorators import login_required

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album})

def track_detail(request, track_id):
    track = get_object_or_404(Track, id=track_id)
    comments = track.comments.all()
    return render(request, 'track_detail.html', {'track': track, 'comments': comments})

@login_required
def add_comment(request, track_id):
    track = get_object_or_404(Track, id=track_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(user=request.user, track=track, content=content)
    return render(request, 'add_comment.html', {'track': track})
