from django.db import models
from drivers.models import Drivers

# Create your models here.
class Competition(models.Model):
    choice = [
        ('Formule 1', 'Formule 1'),
        ('Formule 2', 'Formule 2'),
        ('Formule 3', 'Formule 3'),
        ('Porsche', 'Porsche '),
        ('W series', 'W series'),
    ]
    
    name = models.TextField(max_length=150)
    races = models.IntegerField(default=0)
    type = models.CharField(max_length=255, choices=choice)
    drivers = models.ForeignKey(Drivers, on_delete=models.CASCADE, default='NoDrivers')
