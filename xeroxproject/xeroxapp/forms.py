from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import Credentials, CredentialList

class LoginForm(forms.Form):
    username = forms.CharField(
        label='regno',
        widget=forms.TextInput(attrs={'placeholder': 'Enter registration number'}),
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
    )
    class Meta:
        model = Credentials
        fields = ["regno", "password"]


        

    