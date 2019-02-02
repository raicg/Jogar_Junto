from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomPhotoForm
from .models import MyUser
from game.models import Game
from PIL import Image

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
            user_edited.avatar.path.replace('.jpeg', '.png')
            imagem.save(user_edited.avatar.path, format='PNG')
            imagem = Image.open(user_edited.avatar.path)
            imagem = imagem.convert("RGBA")
            
        elif ".jpg" in user_edited.avatar.path:
            imagem = imagem.convert("RGB")
        else:
            imagem = imagem.convert("RGBA")
        
        imagem = imagem.resize((220, 220), Image.ANTIALIAS)
        imagem2 = Image.open('/home/raicg/Documents/jogarjunto/jogarjunto/website/static/avatars/image.png').convert("RGBA")
        mask = Image.open('/home/raicg/Documents/jogarjunto/jogarjunto/website/static/avatars/mask.png').convert("RGBA")
        Image.composite(imagem2, imagem, mask).save(user_edited.avatar.path)

        #imagem = Image.open(user_edited.avatar.path).convert("RGBA")
        #imagem = imagem.resize((220, 220), Image.ANTIALIAS)
        #imagem.save(user_edited.avatar.path)
        #imagem = Image.open(user_edited.avatar.path).convert("RGBA")
        #imagem2 = Image.open('/home/raicg/Documents/jogarjunto/jogarjunto/website/static/avatars/image.png').convert("RGBA")
        #Image.alpha_composite(imagem, imagem2).save(user_edited.avatar.path)
        #imagem.save(user_edited.avatar.path)

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
    return render(request, 'user/details.html', {'user_detail': user_detail, 'user_games': user_games, 'user_games2': user_games2})
