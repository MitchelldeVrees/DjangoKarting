from django.db import models
from drivers.models import Drivers

class Competition(models.Model):
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

    name = models.TextField(max_length=50)
    country = models.CharField(max_length=255, choices=choice)
    length = models.IntegerField(default=0)
    rounds = models.IntegerField(default=0)
    drivers = models.ManyToManyField(Drivers)