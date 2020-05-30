from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_rooms, name="all_rooms"),
    path(r'token$', views.token, name="token"),
    path(r'rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),
]
