from django.shortcuts import render, redirect

from .models import *
from .forms import raceForm

def race_detail_view(request):
    obj = Race.objects.all

    return render(request, "competition.html", {'all': obj})


def create_race(request):
    form = raceForm()
    if request.method == 'POST':

        form = raceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('see_competition.html')

    return render(request, 'add_race_form.html', {'form': form})
