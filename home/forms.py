# from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# this is a form for creating a User
class CreateUserForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control','placeholder': 'First name','required':'required'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last name' ,'required':'required'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id':'userPassword','class': 'form-control userPassword validate', 'placeholder': 'Password' ,'required':'required'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id':'userConfirmPassword','class': 'form-control userPassword validate', 'placeholder': 'Confirm Password' ,'required':'required'}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email' ,'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

