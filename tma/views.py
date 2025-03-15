from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models


# Create your views here.


def home(request):
    user_events= models.Events.objects.filter(user=request.user)
    return render(request, "tma/home/home.html", {"events": user_events})

@login_required   
def add_events(request):
    if request.method == 'POST':
        form=forms.EventForm(request.POST)

        if form.is_valid():
            event=form.save(commit=False)
            event.user=request.user
            event.save()
            return redirect('home')
    else:
        form=forms.EventForm()
    
    return render(request, 'tma/home/events.html', {'form':form})


"""
@login_required
def rem_events(request, event_id):
    event=get_object_or_404(models.Events, id=event_id, user=request.user)
    
    if request.method == "POST":
        event.delete()
        return redirect('home')
    
    return redirect('home')
"""


@login_required
def trainings(request):
    return render(request, "tma/trainings.html")

@login_required
def atp(request):
    return render(request, "tma/atp.html")

