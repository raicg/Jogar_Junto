from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_list, name='game_list'),
    path('add-game/', views.add_game, name='add_game'),
    path('details/<int:pk>/', views.game_detail, name='game_details'),
    path('details/<int:pk>/games/chat/', views.game_chat, name='game_chat'),
    path('details/<int:pk>/enter/team1/', views.enter_game_team1, name='enter_game_team1'),
    path('details/<int:pk>/enter/team2/', views.enter_game_team2, name='enter_game_team2'),
    path('details/<int:pk>/leave/team1/', views.leave_game_team1, name='leave_game_team1'),
    path('details/<int:pk>/leave/team2/', views.leave_game_team2, name='leave_game_team2'),
]