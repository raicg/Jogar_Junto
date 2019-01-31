from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('user/<int:pk>/', views.user_detail, name='user_details'),
]