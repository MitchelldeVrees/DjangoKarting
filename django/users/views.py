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
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            messages.success(request,(' Registration succesful'))
            return redirect('home')
    else:
        form = userForm()

        return render(request, 'register_user.html', {'form': form })

