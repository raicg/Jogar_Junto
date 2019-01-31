from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Game(models.Model):
    players_team1 = models.ManyToManyField("accounts.MyUser", related_name='players_team1')
    players_team2 = models.ManyToManyField("accounts.MyUser", related_name='players_team2', blank = True)
    online = models.BooleanField()
    teamxteam = models.BooleanField()
    team_players = models.IntegerField()
    address = models.TextField(null = True, blank = True)
    url = models.URLField(null = True, blank = True)
    created_at = models.DateTimeField(
        default=timezone.now
    )
    when_date = models.DateField()
    when_time = models.TimeField()
    game_type = models.IntegerField()

