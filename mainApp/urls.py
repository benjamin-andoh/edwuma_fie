from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView,name='dashboard'),
    path('settings/',views.SettingView, name="settings"),
    path('post_job/',views.PostView,name="postjob"),
    path('profile/',views.ProfileView, name="profile")
]