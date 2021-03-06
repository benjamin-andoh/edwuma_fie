from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from .models import *
from .forms import *
from .decorators import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utills import generate_token


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
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = User.object.all()
            login(request, user)
            return redirect('userprofile')
        else:
            messages.error(request, 'invalid entry')
    form = UserProfileForm()
    return render(request, 'account_profile.html', {'form': form})


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.is_active = False
            user.save()
            # send_mail(subject,message,from_email,to_list,fail_silently=True)

            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('activate.html',
                                       {
                                           'user': user,
                                           'domain': current_site.domain,
                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                           'token': generate_token.make_token(user)
                                       })
            email_message = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email]
            )
            email_message.send()
            return redirect('activatecheck')
            username = form.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + username)

    context = {'form': form}
    return render(request, 'base/register.html', context)


def loginPage(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.last_login == None:
                    login(request, user)
                    return redirect('profile')
                else:
                    login(request, user)
                    return redirect('dashboard')
            else:
                messages.ERROR('Invalid Username or password')
        else:
            messages.ERROR('Invalid username or password')

    return render(request, 'base/login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'base/user.html', context)


def ActivateAccountView(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as identifier:
        user = None
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    return render(request, 'activate_failed.html', status=401)


def Activate_check(request):
    return render(request, 'activate_check.html')


def CompleteProfile(request):
    return render(request, 'completeProfile.html')
