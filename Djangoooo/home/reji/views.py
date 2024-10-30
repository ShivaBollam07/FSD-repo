from django.shortcuts import render, HttpResponse

# Create your views here.

def register(req):
    return HttpResponse("This is page for /register/new/");

def login(req):
    return HttpResponse("This is page for /register/login/");