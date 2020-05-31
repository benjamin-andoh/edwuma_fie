from django.conf.urls import url
from django.contrib.auth import views as auth_views
from chat import views

urlpatterns = [
    url(r'^$', views.chat),
    url(r'^ajax/chat/$', views.broadcast),
]
