from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    avatar = models.FileField(upload_to="website/static/avatars/", null=False, blank=True, default="avatars/anonymous.png")
    uploaded_avatar = models.BooleanField(default=False, blank=True)
    phone_number = models.CharField(max_length=15)
    created_games = models.ForeignKey("game.Game", related_name='created_games', on_delete=models.CASCADE, null=True, blank=True)
    avatar_static_path = models.TextField(default="avatars/anonymous.png")
    
    def __str__(self):
        return self.email
