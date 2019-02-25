from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import CustomUserCreationForm, CustomPhotoForm, ChangeNameForm, ChangeEmailForm, ChangePhoneNumberForm
from .models import MyUser
from game.models import Game
from PIL import Image, ImageDraw, ImageOps
from jogarjunto.settings import BASE_DIR
from django.core.files import File
import os
from django.http import HttpRequest

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def newUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('signupSuccess')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login(request):
    if request.user.uploaded_avatar == False:
        return redirect('addPhoto')
    else:
        return redirect('gameList')



def addPhoto(request):
    image_size = (220, 220)
    image_path = request.user.avatar.url.replace('website', '')
    if request.method == 'POST':
        form = CustomPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user_edited = form.save(commit=False)
            if ".jpeg" in user_edited.avatar.url or ".jpg" in user_edited.avatar.url or ".png" in user_edited.avatar.url:
                user_edited.id = request.user.id
                user_edited.username = request.user.username
                user_edited.first_name = request.user.first_name
                user_edited.last_name = request.user.last_name
                user_edited.uploaded_avatar = request.user.uploaded_avatar
                user_edited.email = request.user.email
                user_edited.phone_number = request.user.phone_number
                user_edited.password = request.user.password
                user_edited.save()

                imagem = Image.open(user_edited.avatar.path)
                if ".jpeg" in user_edited.avatar.url:
                    rgba = 0
                    new_avatar_url = user_edited.avatar.url.replace('.jpeg', '.png')
                    imagem.save(new_avatar_url)
                    image_converted = Image.open(new_avatar_url)
                    transparent_mask = Image.new('L', image_size, color=0)
                    draw = ImageDraw.Draw(transparent_mask)
                    not_transparent_area = (45, 45, 175, 175)
                    draw.rectangle(not_transparent_area, fill=255)
                    image_converted = imagem.resize((130,130), Image.ANTIALIAS)
                    image_converted = ImageOps.expand(image_converted,border=45,fill=0).save(new_avatar_url)
                    image_converted = Image.open(new_avatar_url)
                    image_converted.putalpha(transparent_mask)
                    image_converted.save(new_avatar_url)
                    image_converted = Image.open(new_avatar_url)
                    border = Image.open(BASE_DIR+"/website/static/avatars/image.png").convert("RGBA")
                    mask = Image.open(BASE_DIR+"/website/static/avatars/mask.png").convert("RGBA")
                    Image.alpha_composite(image_converted, border).save(new_avatar_url)
                    
                elif ".jpg" in user_edited.avatar.url:
                    rgba = 0
                    new_avatar_url = user_edited.avatar.url.replace('.jpg', '.png')
                    imagem.save(new_avatar_url)
                    image_converted = Image.open(new_avatar_url)
                    transparent_mask = Image.new('L', image_size, color=0)
                    draw = ImageDraw.Draw(transparent_mask)
                    not_transparent_area = (45, 45, 175, 175)
                    draw.rectangle(not_transparent_area, fill=255)
                    image_converted = imagem.resize((130,130), Image.ANTIALIAS)
                    image_converted = ImageOps.expand(image_converted,border=45,fill=0).save(new_avatar_url)
                    image_converted = Image.open(new_avatar_url)
                    image_converted.putalpha(transparent_mask)
                    image_converted.save(new_avatar_url)
                    image_converted = Image.open(new_avatar_url)
                    border = Image.open(BASE_DIR+"/website/static/avatars/image.png").convert("RGBA")
                    mask = Image.open(BASE_DIR+"/website/static/avatars/mask.png").convert("RGBA")
                    Image.alpha_composite(image_converted, border).save(new_avatar_url)
                elif ".png" in user_edited.avatar.url:
                    rgba = 1
                    new_avatar_url = user_edited.avatar.url
                    imagem = imagem.convert("RGBA")
                
                    image_converted = imagem.resize((130,130), Image.ANTIALIAS)
                    image_converted = ImageOps.expand(image_converted,border=45,fill='black').save(new_avatar_url)
                    image_converted = Image.open(new_avatar_url)
                    imagem2 = Image.open(BASE_DIR+"/website/static/avatars/image.png").convert("RGBA")
                    mask = Image.open(BASE_DIR+"/website/static/avatars/mask.png").convert("RGBA")
                    Image.composite(imagem2, image_converted, mask).save(new_avatar_url)

                else:
                    return HttpResponseRedirect(reverse('userDetails', args=(request.user.id,)))

                filename = new_avatar_url.replace("website/static/avatars/", "")
                content = open(BASE_DIR+"/website/static/avatars/"+filename, 'rb')
                avatar_file = File(content)

                if rgba == 0:
                    os.remove(user_edited.avatar.url)
                    os.remove(new_avatar_url)
                request.user.avatar.save(filename, avatar_file, save=True)
                request.user.uploaded_avatar = True
                request.user.avatar_static_path = "avatars/"+filename
                request.user.save()
                return redirect('photoSuccess')
            
            else:
                form = CustomPhotoForm()
                return render(request, 'user/editPhoto.html', {'form':form, 'image_path': image_path, }) 
        else:
            form = CustomPhotoForm()
            return render(request, 'user/editPhoto.html', {'form':form, 'image_path': image_path, })     
    else:
        form = CustomPhotoForm()
        return render(request, 'user/editPhoto.html', {'form':form, 'image_path': image_path, })

def photoSuccess(request):
    if request.method == 'GET':
        return render(request, 'registration/photoSuccess.html',)

def editName(request):
    if request.method == 'POST':
        form = ChangeNameForm(request.POST)
        if form.is_valid():
            user_edited = form.save(commit=False)
            user_edited.id = request.user.id
            user_edited.username = request.user.username
            user_edited.avatar = request.user.avatar
            user_edited.uploaded_avatar = request.user.uploaded_avatar
            user_edited.avatar_static_path = request.user.avatar_static_path
            user_edited.email = request.user.email
            user_edited.phone_number = request.user.phone_number
            user_edited.password = request.user.password
            user_edited.save()
            return HttpResponseRedirect(reverse('userDetails', args=(request.user.id,)))
    else:
        form = ChangeNameForm()
        return render(request, 'user/editName.html', {'form':form,})


def editEmail(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            user_edited = form.save(commit=False)
            user_edited.id = request.user.id
            user_edited.username = request.user.username
            user_edited.avatar = request.user.avatar
            user_edited.uploaded_avatar = request.user.uploaded_avatar
            user_edited.avatar_static_path = request.user.avatar_static_path
            user_edited.first_name = request.user.first_name
            user_edited.last_name = request.user.last_name
            user_edited.phone_number = request.user.phone_number
            user_edited.password = request.user.password
            user_edited.save()
            return HttpResponseRedirect(reverse('userDetails', args=(request.user.id,)))
    else:
        form = ChangeEmailForm()
        return render(request, 'user/editEmail.html', {'form':form,})


def editPhoneNumber(request):
    if request.method == 'POST':
        form = ChangePhoneNumberForm(request.POST)
        if form.is_valid():
            user_edited = form.save(commit=False)
            user_edited.id = request.user.id
            user_edited.username = request.user.username
            user_edited.avatar = request.user.avatar
            user_edited.uploaded_avatar = request.user.uploaded_avatar
            user_edited.avatar_static_path = request.user.avatar_static_path
            user_edited.first_name = request.user.first_name
            user_edited.last_name = request.user.last_name
            user_edited.email = request.user.email
            user_edited.password = request.user.password
            user_edited.save()
            return HttpResponseRedirect(reverse('userDetails', args=(request.user.id,)))
    else:
        form = ChangePhoneNumberForm()
        return render(request, 'user/editPhoneNumber.html', {'form':form,})



def newUserSuccess(request):
    if request.method == 'GET':
        return render(request, 'registration/signupSuccess.html',)


def userDetail(request, pk):
    user_detail = get_object_or_404(MyUser, pk=pk)
    if user_detail == request.user:
        permission=1
    else:
        permission=0
    user_games = Game.objects.filter(players_team1 = user_detail)
    user_games2 = Game.objects.filter(players_team2 = user_detail)
    return render(request, 'user/details.html', {'user_detail': user_detail, 'user_games': user_games, 'user_games2': user_games2, 'permission': permission, })
