from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import MyUser
from game.models import Game

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def user_detail(request, pk):
    user_detail = get_object_or_404(MyUser, pk=pk)
    user_games = Game.objects.filter(players_team1 = user_detail)
    user_games2 = Game.objects.filter(players_team2 = user_detail)
    return render(request, 'user/details.html', {'user_detail': user_detail, 'user_games': user_games, 'user_games2': user_games2})
