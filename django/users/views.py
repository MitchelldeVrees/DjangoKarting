from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .forms import userForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['nameUser']
        password = request.POST['passwordUser']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in, try again!"))
            return redirect('login')

    else:  
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are logged out!"))
    return redirect('home')

def register_user(request):

    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = userForm()
    return render(request, 'register_user.html', {'form': form})

def forgot_password(request):
    return render(request, 'password_reset.html',{})

