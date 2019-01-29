from django.shortcuts import render, redirect
from games.models import Games
from accounts.models import MyUser
from django.contrib.auth import authenticate, login, logout
from .forms import AddGameForm

def games_list(request):
    lista_de_games_futebol =  Games.objects.filter(game_type=1)
    lista_de_games_paintball = Games.objects.filter(game_type=2)
    lista_de_games_lol = Games.objects.filter(game_type=3)
    lista_de_games_dota = Games.objects.filter(game_type=4)

    return render(request, 'games/games_list.html', {'games_futebol': lista_de_games_futebol, 'games_paintball': lista_de_games_paintball, 'games_lol': lista_de_games_lol, 'games_dota': lista_de_games_dota, })

def add_game(request):
    if request.method == "POST":
        form = AddGameForm(request.POST)
        if form.is_valid():
            Games = form.save(commit=False)
            Games.save()
            Games.players.add(request.user)
            return redirect('game_list')
    else:
        form = AddGameForm()
    return render(request, 'games/add_game.html', {'form': form})

