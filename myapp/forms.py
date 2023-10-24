from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    
# in forms.py
from django import forms
class SignupForm(forms.Form):
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email_notification = forms.BooleanField(label='Receive Email Notifications', required=False)
    phone_notification = forms.BooleanField(label='Receive Phone Notifications', required=False)
    
    

   
