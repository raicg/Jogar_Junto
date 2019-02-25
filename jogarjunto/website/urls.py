from django.urls import path
from . import views

urlpatterns = [
    path('', views.gamesList, name='gameList'),
    path('addGame/', views.addGame, name='addGame'),
    path('details/<int:pk>/', views.gameDetail, name='gameDetails'),
    path('details/<int:pk>/delete', views.gameDelete, name='gameDelete'),
    path('details/<int:pk>/games/chat/', views.gameChat, name='gameChat'),
    path('details/<int:pk>/enter/team1/', views.enterGameTeam1, name='enterGameTeam1'),
    path('details/<int:pk>/enter/team2/', views.enterGameTeam2, name='enterGameTeam2'),
    path('details/<int:pk>/leave/team1/', views.leaveGameTeam1, name='leaveGameTeam1'),
    path('details/<int:pk>/leave/team2/', views.leaveGameTeam2, name='leaveGameTeam2'),
]