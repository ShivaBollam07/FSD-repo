
from django.contrib import admin
from django.urls import path, include
from reji import views

urlpatterns = [
    path('new/', views.register, name='register'),
    path('login/', views.login, name='login')
]
