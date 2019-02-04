from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomPhotoForm
from .models import MyUser
from game.models import Game
from PIL import Image, ImageDraw
from jogarjunto.settings import BASE_DIR
from django.core.files import File
import os

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def new_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('signup_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def add_photo(request):
    image_size = (220, 220)
    image_path = request.user.avatar.url.replace('website', '')
    if request.method == 'POST':
        form = CustomPhotoForm(request.POST, request.FILES)
        user_edited = form.save(commit=False)
        user_edited.id = request.user.id
        user_edited.username = request.user.username
        user_edited.first_name = request.user.first_name
        user_edited.last_name = request.user.last_name
        user_edited.email = request.user.email
        user_edited.phone_number = request.user.phone_number
        user_edited.password = request.user.password
        user_edited.save()

        imagem = Image.open(user_edited.avatar.path)
        if ".jpeg" in user_edited.avatar.path:
            new_avatar_url = user_edited.avatar.url.replace('.jpeg', '.png')
            imagem.save(new_avatar_url)
            image_converted = Image.open(new_avatar_url)
            transparent_mask = Image.new('L', image_size, color=0)
            draw = ImageDraw.Draw(transparent_mask)
            not_transparent_area = (45, 45, 177, 177)
            draw.rectangle(not_transparent_area, fill=255)
            image_converted = imagem.resize(image_size, Image.ANTIALIAS)
            image_converted.putalpha(transparent_mask)
            image_converted.save(new_avatar_url)
            image_converted = Image.open(new_avatar_url)
            border = Image.open(BASE_DIR+"/website/static/avatars/image.png").convert("RGBA")
            mask = Image.open(BASE_DIR+"/website/static/avatars/mask.png").convert("RGBA")
            Image.alpha_composite(image_converted, border).save(new_avatar_url)
            
        elif ".jpg" in user_edited.avatar.url:
            new_avatar_url = user_edited.avatar.url.replace('.jpg', '.png')
            imagem.save(new_avatar_url)
            image_converted = Image.open(new_avatar_url)
            transparent_mask = Image.new('L', image_size, color=0)
            draw = ImageDraw.Draw(transparent_mask)
            not_transparent_area = (45, 45, 177, 177)
            draw.rectangle(not_transparent_area, fill=255)
            image_converted = imagem.resize(image_size, Image.ANTIALIAS)
            image_converted.putalpha(transparent_mask)
            image_converted.save(new_avatar_url)
            image_converted = Image.open(new_avatar_url)
            border = Image.open(BASE_DIR+"/website/static/avatars/image.png").convert("RGBA")
            mask = Image.open(BASE_DIR+"/website/static/avatars/mask.png").convert("RGBA")
            Image.alpha_composite(image_converted, border).save(new_avatar_url)
        else:
            imagem = imagem.convert("RGBA")
        
            image_converted = imagem.resize(image_size, Image.ANTIALIAS)
            imagem2 = Image.open(BASE_DIR+"/website/static/avatars/image.png").convert("RGBA")
            mask = Image.open(BASE_DIR+"/website/static/avatars/mask.png").convert("RGBA")
            Image.composite(imagem2, image_converted, mask).save(new_avatar_url)

        filename = new_avatar_url.replace("website/static/avatars/", "")
        content = open(BASE_DIR+"/website/static/avatars/"+filename, 'rb')
        avatar_file = File(content)
        request.user.avatar.save(filename, avatar_file, save=True)
        os.remove(user_edited.avatar.url)
        os.remove(new_avatar_url)

        return redirect('photo_success')
    else:
        form = CustomPhotoForm()
        return render(request, 'registration/photo.html', {'form':form, 'image_path': image_path, })

def photo_success(request):
    if request.method == 'GET':
        return render(request, 'registration/photo_success.html',)

def new_user_success(request):
    if request.method == 'GET':
        return render(request, 'registration/signup_success.html',)


def user_detail(request, pk):
    user_detail = get_object_or_404(MyUser, pk=pk)
    user_games = Game.objects.filter(players_team1 = user_detail)
    user_games2 = Game.objects.filter(players_team2 = user_detail)
    avatar_static_path =  user_detail.avatar.url.replace("website/static/", "")
    return render(request, 'user/details.html', {'user_detail': user_detail, 'user_games': user_games, 'user_games2': user_games2, 'avatar_static_path': avatar_static_path, })
