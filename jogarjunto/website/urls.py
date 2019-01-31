from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_list, name='game_list'),
    path('add-game/', views.add_game, name='add_game'),
    path('details/<int:pk>/', views.game_detail, name='game_details'),
]