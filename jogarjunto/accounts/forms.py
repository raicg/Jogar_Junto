from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser
from django.forms import PasswordInput

class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'phone_number', 'first_name', 'last_name', 'password', 'avatar', )
        widgets = {
            'password': PasswordInput(),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user





class CustomPhotoForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('avatar', )

