from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from .models import User
import random
from .forms import SettingsForm  
from .models import Game
from .models import Category
from .models import Question



def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def stats(request):
    users = User.objects.all()
    return render(request, 'stats.html', {'users': users})

def settings_view(request):
    if request.method == "POST":
        form = SettingsForm(request.POST)
        if form.is_valid():
            request.session['category_count'] = form.cleaned_data['category_count']
            request.session['excluded_categories'] = list(form.cleaned_data['excluded_categories'].values_list('id', flat=True))
            return redirect('home')
    else:
        form = SettingsForm()
    return render(request, 'settings.html', {'form': form})


def start_game(request):
    logged_users = request.session.get('logged_users', [])
    if len(logged_users) < 2:
        return redirect('home')

    game = Game.objects.create()
    players = User.objects.filter(id__in=logged_users)
    game.players.set(players)
    
    first_player = random.choice(players)
    game.current_player = first_player
    game.save()

    return redirect('game', game_id=game.id)


def game_view(request, game_id):
    game = Game.objects.get(id=game_id)
    categories = Category.objects.exclude(id__in=request.session.get('excluded_categories', []))
    selected_categories = random.sample(list(categories), request.session.get('category_count', 3))

    questions = {}
    for category in selected_categories:
        questions[category] = list(Question.objects.filter(category=category, used=False))

    return render(request, 'game.html', {
        'game': game,
        'questions': questions,
        'players': game.players.all(),
    })


def question_view(request, game_id, question_id):
    game = Game.objects.get(id=game_id)
    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        action = request.POST.get('action')
        if action == "add":
            game.current_player.games_played += question.points
        elif action == "remove":
            game.current_player.games_played -= question.points
        game.current_player.save()
        question.used = True
        question.save()

        next_player = list(game.players.all()).index(game.current_player) + 1
        if next_player >= game.players.count():
            next_player = 0
        game.current_player = game.players.all()[next_player]
        game.save()

        return redirect('game', game_id=game.id)

    return render(request, 'question.html', {'question': question})
