from django.forms import ModelForm
from django import forms
from .models import Competitions

class  competitionForm(forms.ModelForm):
    class Meta:
        model = Competitions
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'numberOfRaces': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'drivers': forms.Select(attrs={'class': 'form-control'}),

        }

