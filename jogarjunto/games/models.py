from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Games(models.Model):
    players = models.ManyToManyField("accounts.MyUser", related_name='players')
    online = models.BooleanField()
    teamxteam = models.BooleanField()
    team_players = models.IntegerField()
    address = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now
    )
    when = models.DateTimeField()
    game_type = models.IntegerField()

