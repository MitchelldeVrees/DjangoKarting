from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import driverForm


# Create your views here.
def driver_detail_view(request):
    obj = Drivers.objects.all

    return render(request, "drivers.html", {'all':obj})

def create_driver(request):
    form = driverForm()
    if request.method == 'POST':

            form = driverForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('/')

    return render(request, 'add_driver_form.html', {'form':form})

def update_driver(request, id):
        driver = Drivers.objects.get(id=id)
        form = driverForm(instance=driver)

        if request.method == "POST":
            form = driverForm(request.POST,instance=driver)
            if form.is_valid():
                form.save()
                return redirect("/")

        context = {'form':form}


        return render(request, 'add_driver_form.html', context)

def delete_driver(request, id):
    driver = Drivers.objects.get(id=id)
    if request.method == "POST":
        driver.delete()
        return redirect("/drivers")
       

    context = {'item': driver}

    return render(request, 'delete.html', context)
