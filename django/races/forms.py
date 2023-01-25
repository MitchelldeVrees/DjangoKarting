from django.forms import ModelForm
from django import forms
from .models import Race


class raceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'laps': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longtitude': forms.TextInput(attrs={'class': 'form-control'}),
            'visitors': forms.TextInput(attrs={'class': 'form-control'}),

        }
