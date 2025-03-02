from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Track, Rating, Comment
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    albums = Album.objects.all()
    return render(request, 'ap/home.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    tracks = Track.objects.filter(album=album)
    return render(request, 'ap/album_detail.html', {'album': album, 'tracks': tracks})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'ap/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'ap/login.html', {'error': 'Nieprawidłowa nazwa użytkownika lub hasło'})
    return render(request, 'ap/login.html')


def rate_album(request, album_id):
    if request.method == 'POST':
        album = get_object_or_404(Album, id=album_id)
        rating = int(request.POST['rating'])
        Rating.objects.update_or_create(
            user=request.user,
            album=album,
            defaults={'rating': rating}
        )
    return redirect('album_detail', album_id=album_id)

def add_comment(request, album_id):
    if request.method == 'POST':
        album = get_object_or_404(Album, id=album_id)
        text = request.POST['text']
        Comment.objects.create(user=request.user, album=album, text=text)
    return redirect('album_detail', album_id=album_id)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'ap/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'ap/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')