from django.shortcuts import render, redirect

from .models import *
from .forms import competitionForm

# Create your views here.
def competition_detail_view(request):
    obj = Competition.objects.all

    return render(request, "competition.html", {'all':obj})

def create_competition(request):
    form = competitionForm()
    if request.method == 'POST':

            form = competitionForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('competition.html')

    return render(request, 'add_competition_form.html', {'form':form})

def see_competition(request):
    obj = Competition.objects.all

    return render(request, 'see_competition.html',{'all',obj})


# def update_competition(request, id):
#         driver = Drivers.objects.get(id=id)
#         form = competitionForm(instance=driver)
#
#         if request.method == "POST":
#             form = competitionForm(request.POST,instance=driver)
#             if form.is_valid():
#                 form.save()
#                 return redirect("/")
#
#         context = {'form':form}
#
#
#         return render(request, 'add_driver_form.html', context)
#
# def delete_competition(request, id):
#     driver = Drivers.objects.get(id=id)
#     if request.method == "POST":
#         driver.delete()
#         return redirect("/drivers")
#
#
#     context = {'item': driver}
#
#     return render(request, 'delete.html', context)

