from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



class UserRegisterForm(UserCreationForm):
    error_css_class="error"

    first_name = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    email = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='',
                    widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

    password2 = forms.CharField(label='',
                    widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter password'}))
    class Meta:
        model = User
        fields=['first_name','last_name','username','password1','password2',"email"]
