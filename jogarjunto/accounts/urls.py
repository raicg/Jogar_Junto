from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.newUser, name='signup'),
    path('signup/success/', views.newUserSuccess, name='signupSuccess'),
    path('photo/success/', views.photoSuccess, name='photoSuccess'),
    path('add/photo/', views.addPhoto, name='addPhoto'),
    path('user/<int:pk>/', views.userDetail, name='userDetails'),
    path('login/successful', views.login, name='login_successful'),
    path('user/edit_name', views.editName, name='userEditName'),
    path('user/edit_email', views.editEmail, name='userEditEmail'),
    path('user/edit_phone_number', views.editPhoneNumber, name='userEditPhoneNumber'),
    path('user/edit_photo', views.addPhoto, name='userEditPhoto'),
] 