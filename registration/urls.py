from django.contrib import admin
from django.urls import path, include

import hoster
from . import views
from .views import UserRegisterView, UserLoginView, Logout_view


urlpatterns = [
    path('login/', UserLoginView, name='login'),
    path('register/', UserRegisterView, name='register'),
    path('logout/', Logout_view, name='logout'),
]

