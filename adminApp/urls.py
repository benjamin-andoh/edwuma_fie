from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminHomePage, name='adminhomepage'),
    path('newskills', views.NewSkill, name='newskill'),
    path('adminprofile', views.AdminProfile, name='adminprofile')
]
