from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Required. Enter your full name.')

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password1', 'password2')