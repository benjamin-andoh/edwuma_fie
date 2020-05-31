from django.shortcuts import render


# Create your views here.
from home.forms import UserProfileForm


def MainView(request):
    return render(request,'dashboard/dashboard.html')

def SettingView(request):
    return render(request,'dashboard/settings.html')

def PostView(request):
    return render(request,'dashboard/postjob.html')

def ProfileView(request):
    form = UserProfileForm()
    return render(request,'dashboard/profile.html',{'form':form})