# new s

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('user', views.userPage, name='user'),
    path('profile',views.accountProfile, name = 'profile'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView,name='activate'),
    path('activity_check/',views.Activate_check,name='activatecheck'),
    # path('completeprofile',views.accountProfile,name='completeprofile')

]
