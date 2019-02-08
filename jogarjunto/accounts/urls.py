from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.new_user, name='signup'),
    path('signup/success/', views.new_user_success, name='signup_success'),
    path('photo/success/', views.photo_success, name='photo_success'),
    path('add/photo/', views.add_photo, name='add_photo'),
    path('user/<int:pk>/', views.user_detail, name='user_details'),
    path('login/successful', views.login, name='login_successful'),
    path('user/edit_name', views.edit_name, name='user_edit_name'),
    path('user/edit_email', views.edit_email, name='user_edit_email'),
    path('user/edit_phone_number', views.edit_phone_number, name='user_edit_phone_number'),
    path('user/edit_photo', views.add_photo, name='user_edit_photo'),
]