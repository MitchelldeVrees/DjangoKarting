from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import competitionForm


# Create your views here.
def competition_detail_view(request):
    obj = Competitions.objects.all

    return render(request, "competition.html", {'all':obj})

def create_competition(request):
    form = competitionForm()
    if request.method == 'POST':

            form = competitionForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('/')

    return render(request, 'add_competition_form.html', {'form':form})