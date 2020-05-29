# from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# this is a form for creating a User
class CreateUserForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Username'}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-user','placeholder': 'First name'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Last name'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Confirm Password'}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
