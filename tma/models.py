from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Crear las tablas de la parte del home
"""
class Events(models.Model):
    type_choices= [
        ('RUN', 'Running'),
        ('BIK', 'Ciclismo'),
        ('SWM', 'Natación'),
        ('TRI', 'Triatlon'),
        ('GYM', 'Gimnasio')
    ]

    #Crear los campos de la db
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    date=models.DateField(null=False)
    type=models.CharField(max_length=3, choices=type_choices, null=False)
    description=models.CharField(max_length=255, default='')
    class Meta():
        verbose_name='event'
        verbose_name_plural='events'

class Goals(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, null=False)
    date=models.DateField(null=False)
    class Meta():
        verbose_name='goal'
        verbose_name_plural='goals'

class Zones(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    type_choices= [
        ('Z1', 'Zona 1 Recovery'),
        ('Z2', 'Zona 2 Easy Run'),
        ('Z3', 'Zona 3 Tempo'),
        ('Z4', 'Zona 4 Umbral'),
        ('Z5a', 'Zona 5a VO2max'),
        ('Z5b', 'Zona 5b VO2max'),
        ('Z5c', 'Zona 5c Sprint')
    ]
    type=models.CharField(max_length=3, choices=type_choices, null=False)
    minValue=models.FloatField()
    maxValue=models.FloatField()
    class Meta():
        verbose_name='zone'
        verbose_name_plural='zones'