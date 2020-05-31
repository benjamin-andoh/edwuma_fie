# render library for returning views to the browser
from django.shortcuts import render
# decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required
# import the user library
from pusher import Pusher
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# replace the xxx with your app_id, key and secret respectively
# instantate the pusher class
pusher = Pusher(app_id=u'1010520', key=u'd9ad078db72f04d870b8', secret=u'c5a16436827ad17fbd95')


# Create your views here.
# login required to access this page. will redirect to admin login page.
@login_required(login_url='/admin/login/')
def chat(request):
    return render(request, "chat.html");

@csrf_exempt
def broadcast(request):
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");