from django.shortcuts import render, redirect, get_object_or_404
from game.models import Game
from accounts.models import MyUser
from django.contrib.auth import authenticate, login, logout
from .forms import AddGameForm

def games_list(request):
    lista_de_games_futebol =  Game.objects.filter(game_type=1)
    lista_de_games_paintball = Game.objects.filter(game_type=2)
    lista_de_games_lol = Game.objects.filter(game_type=3)
    lista_de_games_dota = Game.objects.filter(game_type=4)

    return render(request, 'games/games_list.html', {'games_futebol': lista_de_games_futebol, 'games_paintball': lista_de_games_paintball, 'games_lol': lista_de_games_lol, 'games_dota': lista_de_games_dota, })

def add_game(request):
    if request.method == "POST":
        form = AddGameForm(request.POST)
        if form.is_valid():
            Game = form.save(commit=False)
            Game.save()
            Game.players_team1.add(request.user)
            return redirect('game_list')
    else:
        form = AddGameForm()
    return render(request, 'games/add_game.html', {'form': form})

def game_detail(request, pk):
    game_detail = get_object_or_404(Game, pk=pk)
    players_team1 = game_detail.players_team1.all()
    players_team2 = game_detail.players_team2.all()
    size_team1 = len(players_team1)
    size_team2 = len(players_team2)
    return render(request, 'games/details.html', {'game_detail': game_detail, 'players_team1': players_team1, 'players_team2': players_team2, 'size_team1' : size_team1, 'size_team2' : size_team2, })
