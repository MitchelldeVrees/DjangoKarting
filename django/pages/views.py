from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, "home.html",{})

def drivers_view(request, *args, **kwargs):
    return render(request, "drivers.html",{})

def standing_view(request, *args, **kwargs):
    return render(request, "standings.html",{})
