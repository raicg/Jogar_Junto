from django import forms

from game.models import Game

class AddGameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('online', 'teamxteam', 'team_players', 'address', 'url', 'when_date', 'when_time', 'game_type',)