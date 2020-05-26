from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group 
from .models import *
from .forms import *
from .decorators import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# from django.contrib.auth.models import Group


# @login_required(login_url='login')
# @admin_only
def homePage(request):
    job = Job.objects.all()
    context = {job: 'job'}
    return render(request, 'index.html', context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='freelancer')
            user.groups.add(group)

            messages.success(request, 'account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or password incorrect')

    context = {}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'base/user.html', context)
