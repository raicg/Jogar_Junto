from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

class Game(models.Model):
    title = models.CharField(max_length = 80)
    author = models.ForeignKey("accounts.MyUser", on_delete=models.CASCADE)
    players_team1 = models.ManyToManyField("accounts.MyUser", related_name='players_team1')
    players_team2 = models.ManyToManyField("accounts.MyUser", related_name='players_team2', blank = True)
    online = models.BooleanField()
    teamxteam = models.BooleanField()
    team_players = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    address = models.TextField(null = True, blank = True)
    url = models.URLField(null = True, blank = True)
    created_at = models.DateTimeField(
        default=timezone.now
    )
    when_date = models.DateField()
    when_time = models.TimeField()
    game_type = models.IntegerField()

class Message_Chat(models.Model):
    author = models.ForeignKey("accounts.MyUser", on_delete=models.CASCADE)
    text = models.TextField(max_length = 400)
    created_at = models.DateTimeField(default = timezone.now)
    game_id = models.ForeignKey("game.Game", on_delete=models.CASCADE)

