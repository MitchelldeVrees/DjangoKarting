from django.db import models


class Race(models.Model):
    name = models.TextField(max_length=150)
    laps = models.IntegerField(default=0)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    visitors = models.IntegerField(default=0)
