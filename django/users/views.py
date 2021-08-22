from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages 

# Create your views here.
def sign_up_view(request):

    return render(request, "signup.html", {})

def login_user(request):

    return render(request, "login.html", {})