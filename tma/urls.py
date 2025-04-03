from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.add_events, name='events'),
    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('goals/', views.add_goals, name='goals'),
    path('delete-goal/<int:goal_id>/', views.delete_goal, name='delete_goal'),



    path('atp/', views.atp, name='atp'),
]
