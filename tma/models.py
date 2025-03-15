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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    date=models.DateField(null=False)
    type=models.CharField(max_length=3, choices=type_choices, null=False)
    description=models.CharField(max_length=255)
    class Meta():
        verbose_name='event'
        verbose_name_plural='events'



"""
CORREGIR
"""
class Goals(models.Model):
    name=models.CharField(max_length=50, null=False)
    date=models.DateField(null=False)
    type_choices= [
        ('RUN', 'Running'),
        ('BIK', 'Ciclismo'),
        ('SWM', 'Natación'),
        ('TRI', 'Triatlon'),
        ('GYM', 'Gimnasio')
    ]
    type=models.CharField(max_length=3, choices=type_choices, null=False)

    class Meta():
        verbose_name='goal'
        verbose_name_plural='goals'

#MIRAR COMO CREAR LAS TABLAS DE LA ORGANIZACION DE MESOCICLOS
class Mesociclos(models.Model):
    pass