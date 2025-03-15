from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.add_events, name='events'),
    path('remove-event/<int:event_id>/', views.rem_events, name='remove_event'),
    

    path('trainings/', views.trainings, name='trainings'),
    path('atp/', views.atp, name='atp'),


]
