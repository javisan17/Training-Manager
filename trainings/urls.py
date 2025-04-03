from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('trainings/', views.trainings, name='trainings'),

]