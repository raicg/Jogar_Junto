from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    avatar = models.FileField(upload_to="website/static/avatars/", null=True, blank=False)
    phone_number = models.CharField(max_length=15)
    created_games = models.ForeignKey("game.Game", related_name='created_games', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.email
