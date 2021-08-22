from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class  userForm(UserCreationForm):
    choice = [
            ('United Kingdom', 'United Kingdom'),
            ('Spain', 'Spain'),
            ('Netherlands', 'Netherlands'),
            ('Belgium', 'Belgium '),
            ('Germany', 'Germany'),
            ('United States', 'United States'),
            ('Brasil', 'Brasil '),
            ('Japan', 'Japan'),
            ('Australia', 'Australia'),

        ]

    name = forms.CharField(max_length=50)
    birthdate = forms.DateField()
    nationality= forms.CharField(max_length=255)
    email= forms.EmailField()
    password= forms.CharField()
    profilePic= forms.ImageField()

    
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'password2', 'birthdate', 'nationality','profilePic')
        # widgets = {
        #     'name': forms.TextInput(),
        #     'birthdate': forms.DateField(),
        #     'nationality': forms.Select(),
        #     'email': forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control'})),
        #     'password': forms.TextInput(),
        #     'profilePic': forms.ImageField()
        # }

