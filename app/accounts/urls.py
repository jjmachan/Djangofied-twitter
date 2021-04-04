from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('signup', views.sign_up, name='sign-up'),
        path('login', views.login_request, name='login'),
        path('logout', views.logout_request, name='logout'),
        ]
