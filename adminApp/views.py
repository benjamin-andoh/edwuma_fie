from django.shortcuts import render

# Create your views here.
def AdminHomePage(request):
    return render(request,'adminside/admindashboard.html')