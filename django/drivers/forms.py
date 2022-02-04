from django.forms import ModelForm
from django import forms
from .models import Drivers

class driverForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.Select(attrs={'class': 'form-control'}),
            'summarry': forms.Textarea(attrs={'class': 'form-control'}),
            'wins': forms.TextInput(attrs={'class': 'form-control'})

        }

