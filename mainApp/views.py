from django.shortcuts import render

# Create your views here.

def MainView(request):
    return render(request,'dashboard/dashboard.html')

def SettingView(request):
    return render(request,'dashboard/settings.html')

def PostView(request):
    return render(request,'dashboard/postjob.html')