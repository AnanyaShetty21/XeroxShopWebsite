from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import StudentCredentials, CredentialList, OwnerCredentials

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
        model = StudentCredentials
        fields = ["regno", "password"]


        

    