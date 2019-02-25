from django.shortcuts import render, redirect, get_object_or_404
from game.models import Game, Message_Chat
from accounts.models import MyUser
from django.contrib.auth import authenticate, login, logout
from .forms import AddGameForm, SendMessageChatForm
from django.utils import timezone





def gamesList(request):

    if request.method == 'POST':
        game = get_object_or_404(Game, pk=pk)
        game.delete()

    lista_de_games_futebol =  Game.objects.filter(game_type=1)
    lista_de_games_paintball = Game.objects.filter(game_type=2)
    lista_de_games_lol = Game.objects.filter(game_type=3)
    lista_de_games_dota = Game.objects.filter(game_type=4)

    return render(request, 'games/gamesList.html', {'games_futebol': lista_de_games_futebol, 'games_paintball': lista_de_games_paintball, 'games_lol': lista_de_games_lol, 'games_dota': lista_de_games_dota, })

def addGame(request):
    if request.method == "POST":
        form = AddGameForm(request.POST)
        if form.is_valid():
            Game = form.save(commit=False)
            Game.author = request.user
            Game.save()
            Game.players_team1.add(request.user)
            return redirect('gameList')
    else:
        form = AddGameForm()
    return render(request, 'games/addGame.html', {'form': form})

def gameDetail(request, pk):
    game_detail = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        formChat = SendMessageChatForm(request.POST)
        if formChat.is_valid():
            chat = formChat.save(commit=False)
            chat.author = request.user
            chat.game_id = game_detail
            chat.save()
    else:
        formChat = SendMessageChatForm()
    
    players_team1 = game_detail.players_team1.all()
    players_team2 = game_detail.players_team2.all()

    if request.user in players_team1 or request.user in players_team2:
        entered = 1
    else:
        entered = 0
    size_team1 = len(players_team1)
    size_team2 = len(players_team2)
    game_chat = Message_Chat.objects.filter(game_id = pk).order_by('-created_at')
    return render(request, 'games/details.html', {'game_detail': game_detail, 'players_team1': players_team1, 'players_team2': players_team2, 'size_team1' : size_team1, 'size_team2' : size_team2, 'game_chat' : game_chat, 'form' : formChat, 'entered' : entered, })

def gameChat(request, pk):
    game_chat = Message_Chat.objects.filter(game_id = pk).order_by('-created_at')
    return render(request, 'games/chat.html', {'game_chat': game_chat, })

def gameDelete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.delete()
    return redirect('gameList')

def enterGameTeam1(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.players_team1.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def enterGameTeam2(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.players_team2.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def leaveGameTeam1(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.players_team1.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def leaveGameTeam2(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.players_team2.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER'))