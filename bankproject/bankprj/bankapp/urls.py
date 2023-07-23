from django.urls import path
from . import views, admin

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('newpage',views.newpage,name='newpage'),
    path('forms',views.forms,name='forms'),
    ]