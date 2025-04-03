from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.


@login_required
def trainings(request):
    return render(request, "trainings/trainings.html")

