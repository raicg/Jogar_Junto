from django import forms

from games.models import Games

class AddGameForm(forms.ModelForm):

    class Meta:
        model = Games
        fields = ('online', 'teamxteam', 'team_players', 'address', 'url', 'when_date', 'when_time', 'game_type',)