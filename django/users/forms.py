from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class  userForm(UserCreationForm):
    

    birthdate = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'birthdate', 'password1', 'password2')
       

