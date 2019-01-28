from django.shortcuts import render
from games.models import Games
from django.contrib.auth import authenticate, login, logout

def games_list(request):
    lista_de_games_futebol =  Games.objects.filter(game_type=1)
    lista_de_games_paintball = Games.objects.filter(game_type=2)
    lista_de_games_lol = Games.objects.filter(game_type=3)

    return render(request, 'games/games_list.html', {'games_futebol': lista_de_games_futebol, 'games_paintball': lista_de_games_paintball, 'games_lol': lista_de_games_lol})
