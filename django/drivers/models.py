from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Drivers(models.Model):
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
    name = models.TextField(max_length=100)
    age = models.IntegerField(default=18, validators=[MaxValueValidator(99), MinValueValidator(18)])
    nationality = models.CharField(max_length=255, choices=choice)
    summarry = models.TextField(default='', max_length=100)
    wins = models.IntegerField(default=0, validators=[MaxValueValidator(999), MinValueValidator(0)])

    def __str__(Drivers):
        return Drivers.name