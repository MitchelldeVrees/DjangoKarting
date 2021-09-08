from django.forms import ModelForm
from django import forms
from .models import Competition

class  competitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'laps': forms.TextInput(attrs={'class': 'form-control'}),
            'Type': forms.Select(attrs={'class': 'form-control'}),
            'Driver': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }

