from django.forms import ModelForm
from django import forms
from .models import Competition


class competitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'length': forms.TextInput(attrs={'class': 'form-control'}),
            'rounds': forms.TextInput(attrs={'class': 'form-control'}),
            'drivers': forms.SelectMultiple(attrs={'class': 'form-control'})
        }