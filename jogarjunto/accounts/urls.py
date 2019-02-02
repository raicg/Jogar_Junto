from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.new_user, name='signup'),
    path('signup/success/', views.new_user_success, name='signup_success'),
    path('photo/success/', views.photo_success, name='photo_success'),
    path('add/photo/', views.add_photo, name='add_photo'),
    path('user/<int:pk>/', views.user_detail, name='user_details'),
]