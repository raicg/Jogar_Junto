from django import forms

from game.models import Game, Message_Chat

class AddGameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('online', 'teamxteam', 'team_players', 'address', 'url', 'when_date', 'when_time', 'game_type',)

class SendMessageChatForm(forms.ModelForm):

    class Meta:
        model = Message_Chat
        fields = ('text', )