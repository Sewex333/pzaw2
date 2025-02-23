from django.shortcuts import render, get_object_or_404, redirect
from .models import Club, Player, Comment
from django.contrib.auth.decorators import login_required

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'club_list.html', {'clubs': clubs})

def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    return render(request, 'club_detail.html', {'club': club})

def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    comments = player.comments.all()
    return render(request, 'player_detail.html', {'player': player, 'comments': comments})


@login_required
def add_comment(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(user=request.user, player=player, content=content)
    return render(request, 'add_comment.html', {'player': player})


