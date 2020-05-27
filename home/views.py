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


def homePage(request):
    job = Job.objects.all()
    context = {job: 'job'}
    return render(request, 'index.html', context)


@login_required(login_url='login')
@unauthenticated_user
def dashboard(request):
    pass


# @admin_only
def accountProfile(request):
    return render(request, 'account_profile.html')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')

            # user who registers must be assigned to a group
            group = Group.objects.get(name='freelancer')

            # adding a user to a group
            user.groups.add(group)

            # show a success message
            messages.success(request, 'account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)


def loginPage(request):
    # check if there info on the form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if the user has registered
        user = authenticate(request, username=username, password=password)

        # allow registered user to see the dashboard
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'base/user.html', context)
