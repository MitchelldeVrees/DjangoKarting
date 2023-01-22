from django.db import models

from drivers.models import Drivers


class Competitions(models.Model):
    countries = [
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

    type = [
        ('Formula1','Formula1'),
        ('Formula2','Formula2'),
        ('Formula3','Formula3'),
        ('Karting','Karting'),
    ]

    name = models.TextField(max_length=50)
    country = models.CharField(max_length=255, choices=countries)
    numberOfRaces = models.IntegerField(default=0)
    type = models.CharField(max_length=255, choices=type)
    drivers = models.ForeignKey(Drivers,on_delete=models.CASCADE)

    def __str__(Competitions):
        return Competitions.name